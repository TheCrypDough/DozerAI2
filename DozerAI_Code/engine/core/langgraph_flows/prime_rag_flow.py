# C:\Dozers\DozerAI_Code\engine\core\langgraph_flows\prime_rag_flow.py
from langgraph.graph import StateGraph, END
from typing import TypedDict, List, Optional, Any
import os # Added for LANGFUSE_PUBLIC_KEY access
import google.generativeai as genai
from langfuse import Langfuse

# Assuming KennelClient and Schemas are accessible from this path
# Adjust import paths if necessary based on your project structure
from engine.core.kennel_client import KennelClient 
from engine.core.schemas import DozerPrimeQueryInput, RetrievedChunkContext, DozerPrimeRAGOutput

# --- Langfuse Setup ---
LANGFUSE_PUBLIC_KEY = os.getenv("LANGFUSE_PUBLIC_KEY")
LANGFUSE_SECRET_KEY = os.getenv("LANGFUSE_SECRET_KEY")
LANGFUSE_HOST = os.getenv("LANGFUSE_HOST", "https://cloud.langfuse.com")
langfuse_client_for_flow: Optional[Langfuse] = None
if LANGFUSE_PUBLIC_KEY and LANGFUSE_SECRET_KEY:
    try:
        langfuse_client_for_flow = Langfuse(
            public_key=LANGFUSE_PUBLIC_KEY,
            secret_key=LANGFUSE_SECRET_KEY,
            host=LANGFUSE_HOST
        )
        print("Langfuse client initialized for prime_rag_flow.")
    except Exception as e_lf:
        print(f"Error initializing Langfuse in prime_rag_flow: {e_lf}")
        langfuse_client_for_flow = None

# Define the State for our RAG Graph
class PrimeRAGState(TypedDict):
    query_input: DozerPrimeQueryInput
    query_embedding: Optional[List[float]]
    retrieved_chunk_objects: List[RetrievedChunkContext]
    context_for_llm: str
    llm_response_text: str
    final_output: Optional[DozerPrimeRAGOutput]
    error_message: Optional[str]
    # For passing Langfuse trace object if needed, or use client directly
    langfuse_trace: Optional[Any] # Represents an active Langfuse trace/span

# Nodes for the graph
async def embed_query_node(state: PrimeRAGState) -> PrimeRAGState:
    print("--- Node: Embed Query ---")
    kennel_client: KennelClient = state['kennel_client'] # type: ignore
    langfuse_trace = state.get('langfuse_trace')
    
    lf_span = None
    if langfuse_client_for_flow and langfuse_trace and hasattr(langfuse_trace, 'span'):
        lf_span = langfuse_trace.span(
            name="embed-query-node", 
            input={"query": state["query_input"].query}
        )
    
    query_text = state["query_input"].query
    # Assuming KennelClient's _get_query_embedding is compatible and available
    embedding = await kennel_client._get_query_embedding(query_text)

    if embedding:
        if lf_span: lf_span.end(output={"embedding_generated": True, "embedding_dim": len(embedding)})
        return {**state, "query_embedding": embedding, "error_message": None} # type: ignore
    else:
        err_msg = "Failed to generate query embedding."
        if lf_span: lf_span.end(output={"embedding_generated": False}, level="ERROR", status_message=err_msg)
        return {**state, "query_embedding": None, "error_message": err_msg} # type: ignore

async def retrieve_chunks_node(state: PrimeRAGState) -> PrimeRAGState:
    print("--- Node: Retrieve Chunks ---")
    kennel_client: KennelClient = state['kennel_client'] # type: ignore
    langfuse_trace = state.get('langfuse_trace')

    lf_span = None
    if langfuse_client_for_flow and langfuse_trace and hasattr(langfuse_trace, 'span'):
        lf_span = langfuse_trace.span(
            name="retrieve-chunks-node", 
            input={"query_embedding_present": state.get("query_embedding") is not None}
        )

    if not state.get("query_embedding"):
        err_msg = "Cannot retrieve chunks, query embedding is missing."
        if lf_span: lf_span.end(output={}, level="ERROR", status_message=err_msg)
        return {**state, "retrieved_chunk_objects": [], "context_for_llm": "", "error_message": err_msg} # type: ignore

    embedding_model_in_db = "text-embedding-004"
    top_k_retrieval = 5 
    
    raw_retrieved_chunks: List[Dict] = await kennel_client.semantic_search_chunks(
        query_text=state["query_input"].query,
        top_k=top_k_retrieval,
        embedding_model_in_db=embedding_model_in_db,
        parent_observation=lf_span # Pass span as parent
    )
    
    retrieved_chunk_objects = [RetrievedChunkContext(**chunk) for chunk in raw_retrieved_chunks]

    context_str = ""
    if retrieved_chunk_objects:
        context_str = "\n\n---\n\n".join([
            f"Source Document: {chunk.document_title}\nContextual Summary: {chunk.contextual_summary if chunk.contextual_summary else 'N/A'}\nContent:\n{chunk.chunk_text}"
            for chunk in retrieved_chunk_objects
        ])
    
    print(f"Retrieved {len(retrieved_chunk_objects)} chunks. Combined context length for LLM: {len(context_str)} chars.")
    if lf_span: lf_span.end(output={"retrieved_chunk_count": len(retrieved_chunk_objects), "context_length": len(context_str)})
    return {**state, "retrieved_chunk_objects": retrieved_chunk_objects, "context_for_llm": context_str, "error_message": None} # type: ignore

async def generate_response_node(state: PrimeRAGState) -> PrimeRAGState:
    print("--- Node: Generate Response (Dozer Prime LLM) ---")
    prime_llm_client: genai.GenerativeModel = state['prime_llm_client'] # type: ignore
    langfuse_trace = state.get('langfuse_trace')
    
    lf_generation = None
    if langfuse_client_for_flow and langfuse_trace and hasattr(langfuse_trace, 'generation'):
        lf_generation = langfuse_trace.generation(
            name="dozer-prime-rag-generation",
            model="gemini-2.5-pro-preview-05-06", 
            input={"query": state["query_input"].query, "context": state.get("context_for_llm")},
            model_parameters={"temperature": 0.7}
        )

    if state.get("error_message"):
        if lf_generation: lf_generation.end(level="ERROR", status_message=state["error_message"])
        return {**state, "llm_response_text": ""} # type: ignore

    if not state.get("context_for_llm") and not state.get("retrieved_chunk_objects"):
        print("  No context retrieved. Generating response based on query only (or providing 'no info' message).")
        no_context_response = "I couldn't find specific information in 'The Kennel' to answer that question based on the current query. Could you try rephrasing or providing more details?"
        if lf_generation: lf_generation.end(output={"response": no_context_response}, level="WARNING", status_message="No context retrieved for RAG")
        return {**state, "llm_response_text": no_context_response} # type: ignore

    prompt = f"""
    You are Dozer Prime, CEO Anthony Pierce's AI Best Friend in Business, a hilarious genius assistant for "Dozer's Wild & Woof'derful Bar'k & Grrr'ill".
    You have access to "The Kennel," the business's central knowledge base.
    Answer the user's query based on your knowledge and the provided context from "The Kennel".
    If the context is insufficient, state that clearly. Be insightful and helpful.

    User Query: "{state["query_input"].query}"

    Retrieved Context from "The Kennel":
    ---
    {state.get("context_for_llm")}
    ---

    Your Answer:
    """
    
    try:
        print(f"  Calling LLM gemini-2.5-pro-preview-05-06 for Dozer Prime's response...")
        response = await prime_llm_client.generate_content_async(prompt, generation_config={"max_output_tokens": 2000})

        generated_text = ""
        # Check for parts and text attribute robustly
        if hasattr(response, 'parts') and response.parts:
            generated_text = "".join(part.text for part in response.parts if hasattr(part, 'text')).strip()
        elif hasattr(response, 'text') and response.text:
             generated_text = response.text.strip()
        
        if not generated_text and hasattr(response, 'prompt_feedback') and response.prompt_feedback:
            print(f"    WARN: Prime LLM returned no text. Feedback: {response.prompt_feedback}")
            generated_text = "Dozer Prime pondered but found no words for that precise query with the given context."
            if lf_generation: lf_generation.end(output={"response": generated_text}, level="WARNING", status_message=f"Empty LLM response, feedback: {response.prompt_feedback}")
            return {**state, "llm_response_text": generated_text} # type: ignore

        print(f"  LLM Response generated (length {len(generated_text)} chars).")
        if lf_generation: lf_generation.end(output={"response": generated_text})
        return {**state, "llm_response_text": generated_text, "error_message": None} # type: ignore

    except Exception as e:
        err_msg = f"Error during LLM call for Dozer Prime: {e}"
        print(f"  {err_msg}")
        if lf_generation: lf_generation.end(level="ERROR", status_message=str(e))
        return {**state, "llm_response_text": "Dozer Prime encountered a glitch trying to answer that. Please try again.", "error_message": err_msg} # type: ignore

def format_output_node(state: PrimeRAGState) -> PrimeRAGState:
    print("--- Node: Format Output ---")
    langfuse_trace = state.get('langfuse_trace')
    final_output = DozerPrimeRAGOutput(
        llm_response=state.get("llm_response_text", "Error: No response generated."),
        retrieved_contexts=state.get("retrieved_chunk_objects", []),
        search_query_embedding=state.get("query_embedding"),
        langfuse_trace_id=langfuse_trace.id if langfuse_client_for_flow and langfuse_trace and hasattr(langfuse_trace, 'id') else None
    )
    return {**state, "final_output": final_output} # type: ignore

# Define the graph builder
def build_prime_rag_graph():
    workflow = StateGraph(PrimeRAGState)

    workflow.add_node("embed_query", embed_query_node)
    workflow.add_node("retrieve_chunks", retrieve_chunks_node)
    workflow.add_node("generate_response", generate_response_node)
    workflow.add_node("format_output", format_output_node)

    workflow.set_entry_point("embed_query")
    workflow.add_edge("embed_query", "retrieve_chunks")
    workflow.add_edge("retrieve_chunks", "generate_response")
    workflow.add_edge("generate_response", "format_output")
    workflow.add_edge("format_output", END)

    app = workflow.compile()
    print("Dozer Prime RAG LangGraph app compiled.")
    return app

# To be used by DozerPrimeAgent:
# The compiled_app expects the initial state to contain 'kennel_client' and 'prime_llm_client'
# and 'langfuse_trace' if tracing is active.
# These will be passed in the `configurable` argument when invoking the graph.
# Example:
# config = {"configurable": {"kennel_client": kennel_client_instance, 
#                            "prime_llm_client": prime_llm_model_instance,
#                            "langfuse_trace": current_langfuse_trace_object}}
# compiled_app.invoke(initial_state_dict, config=config) 