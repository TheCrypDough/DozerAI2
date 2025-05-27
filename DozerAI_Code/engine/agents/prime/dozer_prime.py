# C:\Dozers\DozerAI_Code\engine\agents\prime\dozer_prime.py
import os
import sys
from pathlib import Path
import asyncio # Added for async test execution
from dotenv import load_dotenv # Added for testing .env loading
import google.generativeai as genai
from langfuse import Langfuse

# Ensure core is in path for imports
sys.path.append(str(Path(__file__).resolve().parent.parent.parent)) # Add DozerAI_Code to path

from engine.core.kennel_client import KennelClient
from engine.core.schemas import DozerPrimeQueryInput, DozerPrimeRAGOutput
# Ensure the import path for build_prime_rag_graph and langfuse_client_for_flow is correct
from engine.core.langgraph_flows.prime_rag_flow import build_prime_rag_graph, langfuse_client_for_flow, PrimeRAGState

PRIME_LLM_MODEL_NAME = "gemini-2.5-pro-preview-05-06"
prime_llm_client_global: Optional[genai.GenerativeModel] = None
kennel_client_instance_global: Optional[KennelClient] = None

def initialize_global_clients():
    global prime_llm_client_global, kennel_client_instance_global
    
    if not os.getenv("GOOGLE_API_KEY"):
        print("DozerPrime FATAL: GOOGLE_API_KEY not set. Load .env or set environment variable.")
        # Attempt to load .env from standard location if not already loaded by KennelClient
        # This is a fallback for direct script execution; in FastAPI, .env loaded at startup.
        config_dir = Path(__file__).resolve().parent.parent.parent / "config"
        env_path = config_dir / ".env"
        if env_path.exists():
            print(f"Attempting to load .env from {env_path}")
            load_dotenv(env_path)
        else:
            print(f".env file not found at {env_path}. Please ensure it exists and is populated.")
            return # Exit if essential keys are missing

    if not os.getenv("GOOGLE_API_KEY"):
         print("DozerPrime FATAL: GOOGLE_API_KEY still not found after .env load attempt.")
         return
    else:
        try:
            # Configure genai globally if not already done by KennelClient
            if not genai.API_KEY:
                 genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
            prime_llm_client_global = genai.GenerativeModel(PRIME_LLM_MODEL_NAME)
            print(f"DozerPrime: Initialized global LLM: {PRIME_LLM_MODEL_NAME}")
        except Exception as e_llm_init:
            print(f"DozerPrime FATAL: Could not initialize global LLM {PRIME_LLM_MODEL_NAME}. Error: {e_llm_init}")
            prime_llm_client_global = None

    # Initialize KennelClient, it handles its own .env loading internally
    try:
        kennel_client_instance_global = KennelClient()
        if not kennel_client_instance_global.supabase_async:
            print("DozerPrime FATAL: KennelClient global instance failed to initialize Supabase async client.")
            kennel_client_instance_global = None # Ensure it's None
        else:
            print("DozerPrime: Initialized global KennelClient instance.")
    except Exception as e_kc_init:
        print(f"DozerPrime FATAL: Could not initialize global KennelClient. Error: {e_kc_init}")
        kennel_client_instance_global = None

# Call initialization once when module is loaded
initialize_global_clients()

class DozerPrimeAgent:
    def __init__(self):
        if not prime_llm_client_global:
            raise RuntimeError("DozerPrimeAgent cannot be initialized: Global Prime LLM (gemini-2.5-pro-preview-05-06) failed to load.")
        if not kennel_client_instance_global:
             raise RuntimeError("DozerPrimeAgent cannot be initialized: Global KennelClient failed to load.")

        self.rag_graph_app = build_prime_rag_graph() # Pass clients via config
        self.langfuse = langfuse_client_for_flow 
        print("DozerPrimeAgent initialized with RAG graph.")

    async def run_rag_query(self, query_input: DozerPrimeQueryInput) -> DozerPrimeRAGOutput:
        if not self.rag_graph_app:
            return DozerPrimeRAGOutput(llm_response="ERROR: RAG graph not compiled.", retrieved_contexts=[])
        
        if not prime_llm_client_global or not kennel_client_instance_global:
             return DozerPrimeRAGOutput(llm_response="ERROR: Global clients (LLM or Kennel) not initialized.", retrieved_contexts=[])

        trace = None
        if self.langfuse:
            trace = self.langfuse.trace(
                name="dozer-prime-rag-query",
                user_id=query_input.user_id,
                session_id=query_input.session_id,
                input=query_input.model_dump(),
                metadata={"agent_version": "0.1.0_day3_rag"}
            )
        
        initial_state: PrimeRAGState = {
            "query_input": query_input,
            "query_embedding": None,
            "retrieved_chunk_objects": [],
            "context_for_llm": "",
            "llm_response_text": "",
            "final_output": None,
            "error_message": None,
            "langfuse_trace": trace, # Pass the trace object in the state
            # These will be injected via config into the nodes that need them
            "kennel_client": kennel_client_instance_global, # type: ignore
            "prime_llm_client": prime_llm_client_global # type: ignore
        }
        
        # Config to pass clients to nodes that expect them in their signature
        # The nodes in prime_rag_flow.py are defined to pick these up from state for now.
        # If using `with_config` for injection, node signatures and state access change.
        # For Day 3, keeping node access to clients via state as per prime_rag_flow.py structure.
        config_for_invoke = {}

        final_state_dict = None
        try:
            final_state_dict = await self.rag_graph_app.ainvoke(
                initial_state, 
                config=config_for_invoke
            )
            
            if final_state_dict and "final_output" in final_state_dict and final_state_dict["final_output"]:
                output = final_state_dict["final_output"]
                if isinstance(output, DozerPrimeRAGOutput):
                    if trace: trace.update(output=output.model_dump())
                    return output
                else:
                    try:
                        # If it's a dict from serialization, parse it back
                        parsed_output = DozerPrimeRAGOutput(**output) # type: ignore
                        if trace: trace.update(output=parsed_output.model_dump())
                        return parsed_output
                    except Exception as parse_e:
                        error_msg_parse = f"Error parsing final_output dict to Pydantic model: {parse_e}"
                        print(error_msg_parse)
                        if trace: trace.update(output={"error": error_msg_parse}, level="ERROR")
                        return DozerPrimeRAGOutput(llm_response=error_msg_parse, retrieved_contexts=[])
            elif final_state_dict and final_state_dict.get("error_message"):
                err_msg_prop = f"RAG process error: {final_state_dict['error_message']}"
                print(err_msg_prop)
                if trace: trace.update(output={"error": err_msg_prop}, level="ERROR")
                return DozerPrimeRAGOutput(llm_response=err_msg_prop, retrieved_contexts=[])
            else:
                err_msg_final = f"Error: 'final_output' not found or is None in graph result. State: {final_state_dict}"
                print(err_msg_final)
                if trace: trace.update(output={"error": err_msg_final}, level="ERROR")
                return DozerPrimeRAGOutput(llm_response=err_msg_final, retrieved_contexts=[])

        except Exception as e:
            err_msg_exec = f"Exception running RAG graph: {e}"
            print(err_msg_exec)
            import traceback
            traceback.print_exc() # Print stack trace for debugging
            if trace: trace.update(output={"error": err_msg_exec, "stack_trace": traceback.format_exc()}, level="ERROR")
            return DozerPrimeRAGOutput(llm_response=err_msg_exec, retrieved_contexts=[])
        finally:
            if self.langfuse and trace and hasattr(trace, 'id'): # Ensure trace has an ID before trying to flush by it.
                 # Flushing by trace ID is not a direct method. Usually, flush is global.
                 pass # Langfuse client flushes periodically or on shutdown.

async def _test_dozer_prime_rag():
    print("--- Testing Dozer Prime RAG ---")
    
    # Ensure global clients are loaded. initialize_global_clients() is called on module import.
    if not prime_llm_client_global or not kennel_client_instance_global:
        print("Test cannot run: Global LLM or KennelClient not initialized. Check .env and API keys.")
        return

    try:
        agent = DozerPrimeAgent()
    except RuntimeError as e_agent_init:
        print(f"Could not run test, agent initialization failed: {e_agent_init}")
        return
    
    query = DozerPrimeQueryInput(
        query="What is the mission statement of Dozer's Business?", 
        user_id="anthony_ceo_test_run", 
        session_id="test_session_123"
    )
    
    print(f"\nSending query to DozerPrime: '{query.query}'")
    rag_result = await agent.run_rag_query(query)

    print("\n--- Dozer Prime RAG Result ---")
    if rag_result:
        print(f"Response: {rag_result.llm_response}")
        print(f"Langfuse Trace ID (if available): {rag_result.langfuse_trace_id}")
        if rag_result.retrieved_contexts:
            print(f"\nRetrieved {len(rag_result.retrieved_contexts)} contexts:")
            for i, ctx in enumerate(rag_result.retrieved_contexts):
                print(f"  Context {i+1} (Similarity: {ctx.similarity:.4f} - Title: {ctx.document_title}):")
                if ctx.contextual_summary:
                    print(f"    Summary: {ctx.contextual_summary[:100]}...")
                print(f"    Text: {ctx.chunk_text[:150]}...")
        else:
            print("No contexts were retrieved.")
    else:
        print ("RAG Result was None or empty.")
    
    if langfuse_client_for_flow: # Ensure langfuse is flushed if used
        langfuse_client_for_flow.flush()
        print("Langfuse flushed.")

if __name__ == "__main__":
    if sys.platform == "win32" and sys.version_info >= (3, 8, 0):
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    
    asyncio.run(_test_dozer_prime_rag()) 