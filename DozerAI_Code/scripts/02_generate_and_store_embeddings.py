# C:\Dozers\DozerAI_Code\scripts\02_generate_and_store_embeddings.py
import os
import sys
import time
import asyncio
from dotenv import load_dotenv
from pathlib import Path
from supabase import create_client, Client
import google.generativeai as genai
from langfuse import Langfuse

# --- Configuration & Clients ---
print("Script: Initializing configuration and clients for Embedding Generation...")
BASE_DIR = Path(__file__).resolve().parent.parent
CONFIG_DIR = BASE_DIR / "config"
ENV_PATH = CONFIG_DIR / ".env"

if not ENV_PATH.exists():
    print(f"CRITICAL ERROR: .env file not found at {ENV_PATH}")
    sys.exit(1)
load_dotenv(ENV_PATH)

SUPABASE_URL = os.getenv("SUPABASE_API_URL")
SUPABASE_SERVICE_ROLE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Langfuse Configuration
LANGFUSE_PUBLIC_KEY = os.getenv("LANGFUSE_PUBLIC_KEY")
LANGFUSE_SECRET_KEY = os.getenv("LANGFUSE_SECRET_KEY")
LANGFUSE_HOST = os.getenv("LANGFUSE_HOST", "https://cloud.langfuse.com")

# --- BEGIN DEBUG PRINTS ---
print(f"DEBUG: SUPABASE_URL (from SUPABASE_API_URL)='{SUPABASE_URL}' (Type: {type(SUPABASE_URL)})")
print(f"DEBUG: SUPABASE_SERVICE_ROLE_KEY='{SUPABASE_SERVICE_ROLE_KEY}' (Type: {type(SUPABASE_SERVICE_ROLE_KEY)})")
print(f"DEBUG: GOOGLE_API_KEY='{GOOGLE_API_KEY}' (Type: {type(GOOGLE_API_KEY)})")
print(f"DEBUG: LANGFUSE_PUBLIC_KEY='{LANGFUSE_PUBLIC_KEY}' (Type: {type(LANGFUSE_PUBLIC_KEY)})")
print(f"DEBUG: LANGFUSE_SECRET_KEY='{LANGFUSE_SECRET_KEY}' (Type: {type(LANGFUSE_SECRET_KEY)})")
print(f"DEBUG: LANGFUSE_HOST='{LANGFUSE_HOST}' (Type: {type(LANGFUSE_HOST)})")
# --- END DEBUG PRINTS ---

if not all([SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY, GOOGLE_API_KEY, LANGFUSE_PUBLIC_KEY, LANGFUSE_SECRET_KEY]):
    print("ERROR: Supabase URL (from SUPABASE_API_URL), Google API Key, or Langfuse credentials missing in .env.")
    sys.exit(1)

try:
    supabase_client: Client = create_client(SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY)
    print("Supabase client initialized.")
except Exception as e:
    print(f"Error initializing Supabase client: {e}")
    sys.exit(1)

try:
    genai.configure(api_key=GOOGLE_API_KEY)
    EMBEDDING_MODEL_NAME_FOR_DB = "text-embedding-004" # CHANGED to standard 768-dim model
    EMBEDDING_MODEL_SDK_TARGET = f"models/{EMBEDDING_MODEL_NAME_FOR_DB}" # ADDED models/ PREFIX
    print(f"Google Generative AI client configured for embeddings with target model: {EMBEDDING_MODEL_SDK_TARGET}")
except Exception as e:
    print(f"Error configuring Google Generative AI: {e}")
    sys.exit(1)

try:
    langfuse = Langfuse(
        public_key=LANGFUSE_PUBLIC_KEY,
        secret_key=LANGFUSE_SECRET_KEY,
        host=LANGFUSE_HOST
    )
    print("Langfuse client initialized.")
except Exception as e:
    print(f"Error initializing Langfuse client: {e}")
    langfuse = None
    print("WARNING: Langfuse not initialized. Tracing will be disabled for this run.")

# --- Helper Functions ---
def get_chunks_without_embeddings_batch(supabase: Client, offset: int, batch_size: int = 100) -> list:
    try:
        chunks_response = supabase.table("document_chunks").select("chunk_id, chunk_text, contextual_summary, documents(title)").order("created_at", desc=False).range(offset, offset + batch_size - 1).execute()
        
        if not chunks_response.data:
            return []

        chunks_to_process = []
        chunk_ids_fetched = [c['chunk_id'] for c in chunks_response.data]

        if chunk_ids_fetched:
            existing_embeddings_response = supabase.table("document_embeddings").select("chunk_id").in_("chunk_id", chunk_ids_fetched).eq("embedding_model_name", EMBEDDING_MODEL_NAME_FOR_DB).execute()
            embedded_chunk_ids = {e['chunk_id'] for e in existing_embeddings_response.data} if existing_embeddings_response.data else set()

            for chunk_data in chunks_response.data:
                if chunk_data['chunk_id'] not in embedded_chunk_ids:
                    processed_chunk = {
                        "chunk_id": chunk_data['chunk_id'],
                        "chunk_text": chunk_data['chunk_text'],
                        "contextual_summary": chunk_data.get('contextual_summary'),
                        "document_title": chunk_data['documents']['title'] if chunk_data.get('documents') else "Unknown Document"
                    }
                    chunks_to_process.append(processed_chunk)
            return chunks_to_process
        return []

    except Exception as e:
        print(f"Error fetching chunks without embeddings: {e}")
        return []

async def generate_embeddings_batch(texts_to_embed: list[str], model_id: str, trace = None) -> list[list[float]] | None:
    langfuse_generation = None
    if langfuse and trace:
        langfuse_generation = trace.generation(
            name="google-embedding-batch",
            model=model_id,
            input=[{"role":"system", "content":"Texts to embed"}, {"role":"user", "content": str(texts_to_embed)}],
            model_parameters={"batch_size": len(texts_to_embed)}
        )
    
    all_embeddings = []
    try:
        print(f"  Generating embeddings for a batch of {len(texts_to_embed)} texts with model {model_id}...")
        result = genai.embed_content(
            model=model_id, 
            content=texts_to_embed,
            task_type="RETRIEVAL_DOCUMENT"
        )
        all_embeddings = result['embedding']
        
        if langfuse_generation:
            langfuse_generation.end(output={"embedding_count": len(all_embeddings)})
        print(f"  Successfully generated {len(all_embeddings)} embeddings.")
        return all_embeddings
    except Exception as e:
        print(f"  ERROR generating embeddings batch: {e}")
        if langfuse_generation:
            langfuse_generation.end(level="ERROR", status_message=str(e))
        return None

def store_embeddings_in_supabase_batch(supabase: Client, embeddings_data_to_store: list[dict]):
    if not embeddings_data_to_store:
        return 0
    print(f"  Attempting to insert/upsert {len(embeddings_data_to_store)} embeddings into Supabase...")
    try:
        response = supabase.table("document_embeddings").insert(embeddings_data_to_store).execute()

        if response.data:
            print(f"  Successfully stored {len(response.data)} new embeddings in Supabase.")
            return len(response.data)
        else:
            error_message = "Unknown error"
            if hasattr(response, 'error') and response.error and hasattr(response.error, 'message'):
                error_message = response.error.message
            print(f"  ERROR storing embeddings in Supabase: {error_message}")
            if error_message and "violates unique constraint" in error_message and "document_embeddings_chunk_id_key" in error_message :
                 print("  Hint: This means an embedding for this chunk_id already exists. The `get_chunks_without_embeddings_batch` should prevent this.")
            elif error_message and "embedding" in error_message and ("dimensions" in error_message or "768" in error_message):
                 print("  Hint: This might be a vector dimension mismatch. Ensure embedding model output matches table schema (VECTOR(768)).")
            return 0
    except Exception as e:
        print(f"  EXCEPTION during Supabase embedding insertion: {e}")
        return 0

async def main_async():
    print("Starting Day 3: Embedding Generation & Storage Script...")
    overall_start_time = time.time()

    trace = None
    if langfuse:
        trace = langfuse.trace(
            name="dozerai-embedding-generation-job",
            user_id="anthony_pierce_ceo",
            metadata={"environment": "development", "script_version": "0.1.0_day3"}
        )

    offset = 0
    batch_size = 50
    total_embeddings_generated = 0
    total_chunks_processed_for_embedding = 0

    while True:
        current_loop_span = None
        if langfuse and trace:
            current_loop_span = trace.span(
                name="embedding-generation-loop",
                input={"offset": offset, "batch_size": batch_size}
            )

        print(f"\nFetching batch of chunks needing embeddings (offset: {offset}, batch_size: {batch_size})...")
        chunks_to_process = get_chunks_without_embeddings_batch(supabase_client, offset, batch_size)

        if not chunks_to_process:
            print("No more chunks found that require embedding. Process complete.")
            if current_loop_span: current_loop_span.end(output={"status":"no_more_chunks"})
            break

        print(f"Fetched {len(chunks_to_process)} chunks to process in this batch.")
        total_chunks_processed_for_embedding += len(chunks_to_process)
        
        texts_for_embedding_api = []
        chunk_ids_in_batch = []

        for chunk_info in chunks_to_process:
            text_to_embed = chunk_info["chunk_text"]
            if chunk_info.get("contextual_summary") and chunk_info["contextual_summary"].strip():
                text_to_embed = f"Context: {chunk_info['contextual_summary']}\n\nContent: {chunk_info['chunk_text']}"
            texts_for_embedding_api.append(text_to_embed)
            chunk_ids_in_batch.append(chunk_info["chunk_id"])
        
        batch_embeddings = await generate_embeddings_batch(texts_for_embedding_api, EMBEDDING_MODEL_SDK_TARGET, trace)
        
        if batch_embeddings and len(batch_embeddings) == len(chunk_ids_in_batch):
            embeddings_to_store_db = []
            for i, emb in enumerate(batch_embeddings):
                embeddings_to_store_db.append({
                    "chunk_id": chunk_ids_in_batch[i],
                    "embedding": emb,
                    "embedding_model_name": EMBEDDING_MODEL_NAME_FOR_DB
                })
            
            num_stored = store_embeddings_in_supabase_batch(supabase_client, embeddings_to_store_db)
            total_embeddings_generated += num_stored
            if current_loop_span: current_loop_span.end(output={"embeddings_generated_in_batch": num_stored, "db_stored": num_stored})
        else:
            print(f"  ERROR or mismatch in embedding generation for batch starting at offset {offset}. Expected {len(chunk_ids_in_batch)} embeddings, got {len(batch_embeddings) if batch_embeddings else 0}.")
            if current_loop_span: current_loop_span.end(output={"status":"embedding_generation_failed"}, level="ERROR")

        offset += batch_size
        print(f"Current total embeddings generated: {total_embeddings_generated}")
        time.sleep(2)

    print(f"\n--- Embedding Generation Finished ---")
    print(f"Total chunks processed for embedding consideration: {total_chunks_processed_for_embedding}")
    print(f"Total new embeddings generated and stored: {total_embeddings_generated}")

    hnsw_sql = "CREATE INDEX CONCURRENTLY IF NOT EXISTS idx_hnsw_document_embeddings ON public.document_embeddings USING hnsw (embedding vector_l2_ops);"
    print(f"\nAttempting to ensure HNSW index exists with command: {hnsw_sql}")
    hnsw_span = None
    if langfuse and trace:
        hnsw_span = trace.span(name="ensure-hnsw-index", input={"sql": hnsw_sql})
    try:
        print("INFO: HNSW Index creation command provided. For large tables, `CREATE INDEX CONCURRENTLY` is preferred.")
        print("Please run the following command in your Supabase SQL Editor if the script doesn't create it, or if you prefer manual control:")
        print(f"`{hnsw_sql}`")
        print("This step is CRUCIAL for fast semantic search performance.")
        if langfuse and hnsw_span: hnsw_span.end(output={"status": "SQL provided for manual execution / or attempted"})
    except Exception as e:
        print(f"ERROR during HNSW index creation attempt: {e}")
        print("Please ensure the HNSW index is created manually in Supabase Studio for optimal performance.")
        if langfuse and hnsw_span: hnsw_span.end(level="ERROR", status_message=str(e))
    
    overall_end_time = time.time()
    print(f"\nDay 3 Embedding Script finished in {overall_end_time - overall_start_time:.2f} seconds.")
    if langfuse and trace: trace.update(output={"total_embeddings_generated": total_embeddings_generated, "total_chunks_processed": total_chunks_processed_for_embedding})

async def run_script():
    await main_async()

if __name__ == "__main__":
    if sys.platform == "win32" and sys.version_info >= (3, 8, 0):
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(run_script()) 