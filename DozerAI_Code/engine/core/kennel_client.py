# C:\Dozers\DozerAI_Code\engine\core\kennel_client.py
import os
from dotenv import load_dotenv
from pathlib import Path
from supabase import create_client, Client, AClient # AClient for async
import google.generativeai as genai # For query embedding
from typing import List, Dict, Optional, Any
from langfuse import Langfuse

# --- Configuration & Clients ---
BASE_DIR = Path(__file__).resolve().parent.parent.parent # DozerAI_Code
CONFIG_DIR = BASE_DIR / "config"
ENV_PATH = CONFIG_DIR / ".env"
load_dotenv(ENV_PATH)

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_SERVICE_ROLE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY") # For query embedding

LANGFUSE_PUBLIC_KEY = os.getenv("LANGFUSE_PUBLIC_KEY")
LANGFUSE_SECRET_KEY = os.getenv("LANGFUSE_SECRET_KEY")
LANGFUSE_HOST = os.getenv("LANGFUSE_HOST", "https://cloud.langfuse.com")

QUERY_EMBEDDING_MODEL_SDK_TARGET = "models/text-embedding-004"

class KennelClient:
    def __init__(self, supabase_url: str = os.getenv("SUPABASE_API_URL"), supabase_key: str = SUPABASE_SERVICE_ROLE_KEY):
        if not supabase_url or not supabase_key:
            raise ValueError("Supabase URL and Key must be provided or set in .env")
        self.supabase_async: AClient = create_client(supabase_url, supabase_key)
        print("Async KennelClient (Supabase) initialized.")
        
        if GOOGLE_API_KEY:
            if not getattr(genai, 'API_KEY', None):
                try:
                    genai.configure(api_key=GOOGLE_API_KEY)
                    print(f"KennelClient: Google Generative AI configured with key.")
                except Exception as e_cfg:
                    print(f"KennelClient: Error configuring Google API in KennelClient: {e_cfg}")

            print(f"KennelClient: Google Generative AI embedding model target: {QUERY_EMBEDDING_MODEL_SDK_TARGET}.")
        else:
            print("KennelClient WARNING: GOOGLE_API_KEY not found, query embedding will fail.")

        self.langfuse = None
        if LANGFUSE_PUBLIC_KEY and LANGFUSE_SECRET_KEY:
            try:
                self.langfuse = Langfuse(
                    public_key=LANGFUSE_PUBLIC_KEY,
                    secret_key=LANGFUSE_SECRET_KEY,
                    host=LANGFUSE_HOST
                )
                print("KennelClient: Langfuse client initialized.")
            except Exception as e:
                print(f"KennelClient Error initializing Langfuse: {e}")

    async def _get_query_embedding(self, query_text: str) -> Optional[List[float]]:
        if not getattr(genai, 'API_KEY', None) or not hasattr(genai, 'embed_content_async'):
            print("ERROR: Google Generative AI SDK not properly configured or embed_content_async not found.")
            return None
        
        try:
            print(f"  Generating embedding for query: '{query_text[:50]}...' with model {QUERY_EMBEDDING_MODEL_SDK_TARGET}")
            result = await genai.embed_content_async(
                model=QUERY_EMBEDDING_MODEL_SDK_TARGET,
                content=query_text,
                task_type="RETRIEVAL_QUERY"
            )
            return result['embedding']
        except Exception as e:
            print(f"  ERROR generating query embedding: {e}")
            return None

    async def semantic_search_chunks(self, query_text: str, top_k: int = 5, 
                                     embedding_model_in_db: str = "text-embedding-004",
                                     parent_observation: Optional[Any]=None) -> List[Dict]:
        langfuse_span = None
        if self.langfuse and parent_observation:
             if hasattr(parent_observation, 'span') and callable(parent_observation.span):
                langfuse_span = parent_observation.span(
                    name="kennel-semantic-search",
                    input={"query": query_text, "top_k": top_k, "model_in_db": embedding_model_in_db}
                )
             elif hasattr(parent_observation, 'name') and isinstance(getattr(parent_observation, 'name', None), str) and "Langfuse" in parent_observation.name:
                langfuse_span = parent_observation.span(
                    name="kennel-semantic-search",
                    input={"query": query_text, "top_k": top_k, "model_in_db": embedding_model_in_db}
                )

        query_embedding = await self._get_query_embedding(query_text)
        if not query_embedding:
            if langfuse_span: langfuse_span.end(output={"error": "Failed to generate query embedding"}, level="ERROR")
            return []

        try:
            print(f"  Performing semantic search with top_k={top_k} for model '{embedding_model_in_db}'...")
            response = await self.supabase_async.rpc(
                "match_document_chunks",
                {
                    "query_embedding": query_embedding,
                    "match_model_name": embedding_model_in_db,
                    "match_count": top_k,
                },
            ).execute()

            if response.data:
                print(f"  Semantic search returned {len(response.data)} chunks.")
                if langfuse_span: langfuse_span.end(output={"retrieved_chunk_count": len(response.data), "chunks_preview": response.data[:2]})
                return [dict(row) for row in response.data]
            else:
                print(f"  Semantic search returned no results. Response: {response}")
                if hasattr(response, 'error') and response.error:
                     print(f"  Supabase RPC error: {response.error.message}")
                     if langfuse_span: langfuse_span.end(output={"error": response.error.message, "status": "no_results"}, level="WARNING")
                else:
                     if langfuse_span: langfuse_span.end(output={"status": "no_results"}, level="INFO")
                return []
        except Exception as e:
            print(f"  ERROR during semantic search: {e}")
            if langfuse_span: langfuse_span.end(output={"error": str(e)}, level="ERROR")
            return []

    async def get_document_full_text(self, document_id: str, parent_observation: Optional[Any]=None) -> Optional[str]:
        langfuse_span = None
        if self.langfuse and parent_observation:
             if hasattr(parent_observation, 'span') and callable(parent_observation.span):
                langfuse_span = parent_observation.span(name="kennel-get-full-text", input={"document_id": document_id})
             elif hasattr(parent_observation, 'name') and isinstance(getattr(parent_observation, 'name', None), str) and "Langfuse" in parent_observation.name:
                langfuse_span = parent_observation.span(name="kennel-get-full-text", input={"document_id": document_id})
        
        try:
            print(f"  Fetching full text for document_id: {document_id}...")
            response = await self.supabase_async.table("documents").select("full_text_content").eq("document_id", document_id).maybe_single().execute()
            if response.data and response.data.get("full_text_content"):
                content = response.data["full_text_content"]
                print(f"  Full text fetched (length: {len(content)} chars).")
                if langfuse_span: langfuse_span.end(output={"text_length": len(content)})
                return content
            else:
                print(f"  Full text not found for document_id: {document_id}.")
                if langfuse_span: langfuse_span.end(output={"error": "Full text not found"}, level="WARNING")
                return None
        except Exception as e:
            print(f"  ERROR fetching full text for document_id {document_id}: {e}")
            if langfuse_span: langfuse_span.end(output={"error": str(e)}, level="ERROR")
            return None

async def _test_kennel_client():
    print("Testing KennelClient...")
    kennel = KennelClient()
    if not kennel.supabase_async:
        return

    test_query = "What is Dozer's mission statement?"
    print(f"\nTesting semantic search for: '{test_query}'")
    
    mock_trace = None
    if kennel.langfuse:
        mock_trace = kennel.langfuse.trace(name="kennel_client_test_trace", user_id="test_user")

    results = await kennel.semantic_search_chunks(test_query, top_k=2, parent_observation=mock_trace)
    if results:
        print(f"Found {len(results)} relevant chunks:")
        for i, res in enumerate(results):
            print(f"  Chunk {i+1} (Similarity: {res.get('similarity', 'N/A')} - Title: {res.get('document_title', 'N/A')} ):")
            print(f"    Text: {res.get('chunk_text', '')[:200]}...")
            print(f"    Contextual Summary: {res.get('contextual_summary', 'N/A')[:100]}...")
    else:
        print("No chunks found or error in search.")

    if mock_trace: mock_trace.update(output={"test_results_count": len(results) if results else 0})

if __name__ == "__main__":
    # import asyncio # Already imported at top
    # asyncio.run(_test_kennel_client())
    print("KennelClient defined. Run _test_kennel_client() within an async context and after data ingestion to test.") 