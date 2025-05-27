# C:\Dozers\DozerAI_Code\scripts\01_ingest_and_contextualize_docs.py
import os
import sys
import hashlib
import time
from dotenv import load_dotenv
from pathlib import Path
from supabase import create_client, Client
import google.generativeai as genai
from langchain_text_splitters import RecursiveCharacterTextSplitter, MarkdownHeaderTextSplitter
import tiktoken # For estimating token counts for summary generation context

# --- Configuration & Clients ---
print("Script: Initializing configuration and clients...")
BASE_DIR = Path(__file__).resolve().parent.parent
CONFIG_DIR = BASE_DIR / "config"
# Path to the 'Planning Docs' directory on Anthony's host machine
# This needs to be an absolute path that the script can access.
# Assuming the script is run from DozerAI_Code, and Docs is parallel to it at Dozers\Docs
HOST_PROJECT_ROOT = BASE_DIR.parent # This should be C:\Dozers
PLANNING_DOCS_DIR_HOST_OS = HOST_PROJECT_ROOT / "Docs" / "Planning Docs"

if not os.path.exists(CONFIG_DIR / ".env"):
    print(f"CRITICAL ERROR: .env file not found at {CONFIG_DIR / '.env'}")
    sys.exit(1)
load_dotenv(CONFIG_DIR / ".env")

SUPABASE_URL = os.getenv("SUPABASE_API_URL")
SUPABASE_SERVICE_ROLE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not all([SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY, GOOGLE_API_KEY]) or \
   "YOUR_SUPABASE" in SUPABASE_URL or \
   "YOUR_GOOGLE" in GOOGLE_API_KEY:
    print("ERROR: Supabase URL/Service Key or Google API Key missing/placeholders in .env.")
    print(f"Please check C:\\Dozers\\DozerAI_Code\\config\\.env")
    sys.exit(1)

try:
    supabase_client: Client = create_client(SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY)
    print("Supabase client initialized successfully.")
except Exception as e:
    print(f"Error initializing Supabase client: {e}")
    sys.exit(1)

try:
    genai.configure(api_key=GOOGLE_API_KEY)
    context_gen_model = genai.GenerativeModel('gemini-2.5-flash-preview-05-20')
    print(f"Google Generative AI client initialized with model: gemini-2.5-flash-preview-05-20.")
except Exception as e:
    print(f"Error initializing Google Generative AI client: {e}")
    sys.exit(1)

# Initialize tiktoken encoder for checking context length for summary LLM
try:
    encoding = tiktoken.get_encoding("cl100k_base") # Common encoder
except:
    encoding = tiktoken.get_encoding("gpt2") # Fallback
print("Tiktoken encoder initialized.")

MAX_TOKENS_FOR_SUMMARY_CONTEXT = 200000  # Approx token limit for Gemini 1.5 Flash context window (actually 1M, but keep summary context smaller)

# --- Helper Functions ---
def generate_content_hash(content: str) -> str:
    return hashlib.md5(content.encode('utf-8')).hexdigest()

def get_contextual_summary_for_chunk(
    full_document_text_for_context: str, 
    chunk_text: str, 
    doc_title: str, 
    llm_model: genai.GenerativeModel
) -> str | None:
    
    # Truncate full_document_text_for_context if it's too long
    tokens = encoding.encode(full_document_text_for_context)
    if len(tokens) > MAX_TOKENS_FOR_SUMMARY_CONTEXT:
        print(f"    WARN: Full document context for '{doc_title}' summary generation is too long ({len(tokens)} tokens). Truncating to {MAX_TOKENS_FOR_SUMMARY_CONTEXT} tokens.")
        full_document_text_for_context = encoding.decode(tokens[:MAX_TOKENS_FOR_SUMMARY_CONTEXT])

    prompt = f"""
    Document Title: "{doc_title}"

    Full Document Context (or significant surrounding window):
    ---
    {full_document_text_for_context}
    ---

    Specific Chunk to Summarize:
    ---
    {chunk_text}
    ---

    Task: Provide a concise contextual summary (target 50-100 words, strictly for the 'Specific Chunk to Summarize') that explains what this specific chunk is about AND its role or significance within the larger document context provided. This summary will be prepended to the chunk to improve search retrieval for a RAG system. Focus ONLY on the specific chunk's context.
    CONCISE CONTEXTUAL SUMMARY:
    """
    try:
        print(f"    Generating summary for chunk (length {len(chunk_text)} chars)...")
        generation_config = genai.types.GenerationConfig(max_output_tokens=1500)
        
        # safety_settings_override = [
        #    {"category": genai.types.HarmCategory.HARM_CATEGORY_HARASSMENT, "threshold": genai.types.HarmBlockThreshold.BLOCK_NONE},
        #    {"category": genai.types.HarmCategory.HARM_CATEGORY_HATE_SPEECH, "threshold": genai.types.HarmBlockThreshold.BLOCK_NONE},
        #    {"category": genai.types.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT, "threshold": genai.types.HarmBlockThreshold.BLOCK_NONE},
        #    {"category": genai.types.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT, "threshold": genai.types.HarmBlockThreshold.BLOCK_NONE},
        # ]
        # response = llm_model.generate_content(prompt, generation_config=generation_config, safety_settings=safety_settings_override)
        response = llm_model.generate_content(prompt, generation_config=generation_config)

        if not response.candidates:
            print(f"    WARN: No candidates returned by LLM for chunk from '{doc_title}'.")
            if response.prompt_feedback:
                print(f"      Prompt Feedback: {response.prompt_feedback}")
                if hasattr(response.prompt_feedback, 'block_reason') and response.prompt_feedback.block_reason:
                    block_reason_name = response.prompt_feedback.block_reason.name if hasattr(response.prompt_feedback.block_reason, 'name') else str(response.prompt_feedback.block_reason)
                    block_reason_message = response.prompt_feedback.block_reason_message if hasattr(response.prompt_feedback, 'block_reason_message') else "No message"
                    print(f"      Response Block Reason: {block_reason_name}, Message: {block_reason_message}")
            return None

        candidate = response.candidates[0]

        if candidate.safety_ratings:
            print(f"      Safety Ratings for chunk from '{doc_title}':")
            for rating in candidate.safety_ratings:
                # Access HarmCategory directly from genai.types if available, otherwise use string
                category_name = rating.category.name if hasattr(rating.category, 'name') else str(rating.category)
                # Attempt to get a more descriptive name if it's an enum and genai.types.HarmCategory is valid
                if hasattr(genai, 'types') and hasattr(genai.types, 'HarmCategory'):
                    try: 
                        category_enum_val = int(str(rating.category).split(':')[-1].strip()) if ':' in str(rating.category) else int(str(rating.category))
                        category_name_from_enum = genai.types.HarmCategory(category_enum_val).name
                        if category_name_from_enum: # Use if valid
                             category_name = category_name_from_enum
                    except (ValueError, AttributeError, TypeError):
                        pass # keep original category_name if enum conversion fails

                probability_name = rating.probability.name if hasattr(rating.probability, 'name') else str(rating.probability)
                print(f"        - Category: {category_name}, Probability: {probability_name}{', BLOCKED' if rating.blocked else ''}")

        # candidate.finish_reason should be an enum member, e.g., <FinishReason.MAX_TOKENS: 2>
        # It has .name (e.g., "MAX_TOKENS") and .value (e.g., 2)
        current_finish_reason_enum = candidate.finish_reason
        
        # Default to string representation if .name or .value are not available
        finish_reason_str = str(current_finish_reason_enum)
        finish_reason_val = -1 # Default to an invalid value

        if hasattr(current_finish_reason_enum, 'name'):
            finish_reason_str = current_finish_reason_enum.name
        if hasattr(current_finish_reason_enum, 'value'):
            finish_reason_val = current_finish_reason_enum.value
        else: # If .value is not present, try to infer integer if current_finish_reason_enum is int-like
            try:
                finish_reason_val = int(current_finish_reason_enum)
            except (ValueError, TypeError):
                print(f"    WARN: Could not determine integer value for finish_reason: {current_finish_reason_enum}")
                # Fallback to trying to parse from string if it looks like "FinishReason.MAX_TOKENS" or "2"
                if isinstance(finish_reason_str, str) and finish_reason_str.isdigit():
                     finish_reason_val = int(finish_reason_str)
                elif isinstance(finish_reason_str, str) and "MAX_TOKENS" in finish_reason_str.upper(): # example
                     finish_reason_val = 2


        # Values from Gemini API documentation:
        # FINISH_REASON_UNSPECIFIED = 0
        # STOP = 1 (Natural stop)
        # MAX_TOKENS = 2
        # SAFETY = 3
        # RECITATION = 4
        # OTHER = 5
        
        if finish_reason_val == 3: # SAFETY
            print(f"    WARN: LLM generation for chunk from '{doc_title}' was BLOCKED due to SAFETY.")
            print(f"      Finish Reason: {finish_reason_str} (Value: {finish_reason_val})")
            if candidate.safety_ratings: # Log details if blocked for safety
                print(f"      Triggering Safety Ratings:")
                for rating in candidate.safety_ratings:
                    category_name = rating.category.name if hasattr(rating.category, 'name') else str(rating.category)
                    probability_name = rating.probability.name if hasattr(rating.probability, 'name') else str(rating.probability)
                    print(f"        - Category: {category_name}, Probability: {probability_name}{', BLOCKED' if rating.blocked else ''}")
            return None
        
        if finish_reason_val not in [1, 2]: # Not STOP or MAX_TOKENS
            print(f"    WARN: LLM generation for chunk from '{doc_title}' did not finish as expected (Reason: {finish_reason_str}, Value: {finish_reason_val}).")
            return None

        if candidate.content and candidate.content.parts:
            summary_parts = [part.text for part in candidate.content.parts if hasattr(part, 'text')]
            summary = "".join(summary_parts).strip()
            
            if not summary:
                print(f"    WARN: LLM generated an empty summary string for chunk from '{doc_title}' (Finish reason: {finish_reason_str}). Parts: {len(candidate.content.parts)}")
                return None
            
            print(f"    Summary generated (length {len(summary)} chars).")
            return summary
        else:
            print(f"    WARN: LLM response for chunk from '{doc_title}' had Finish Reason {finish_reason_str} but no processable content parts.")
            return None

    except Exception as e:
        print(f"    EXCEPTION during contextual summary generation for chunk from '{doc_title}': {e.__class__.__name__}: {e}")
        if 'response' in locals() and response:
            response_details = "Could not get response details."
            try:
                response_details = str(response) 
                if hasattr(response, 'candidates') and response.candidates:
                    response_details += f" Candidate[0]: {str(response.candidates[0])}"
                if hasattr(response, 'prompt_feedback'):
                    response_details += f" PromptFeedback: {str(response.prompt_feedback)}"
            except:
                pass
            print(f"      Raw response details (approx): {response_details[:500]}...") 
        return None

def store_chunks_in_supabase(supabase: Client, chunks_to_store: list):
    if not chunks_to_store:
        return 0
    
    print(f"  Attempting to insert {len(chunks_to_store)} chunks into Supabase...")
    try:
        # Upserting based on document_id and chunk_sequence to handle re-runs if needed,
        # though full delete of old chunks is preferred for content changes.
        # If a chunk with same doc_id and sequence exists, its text and summary are updated.
        # This requires careful handling if you don't want to re-summarize unchanged chunks.
        # For simplicity now, we'll do batch inserts.
        # Ensure `document_chunks` table has `ON CONFLICT (document_id, chunk_sequence) DO UPDATE SET ...` if using upsert.
        # For initial load, simple insert is fine if old chunks are deleted.
        
        response = supabase.table("document_chunks").insert(chunks_to_store).execute()
        if response.data:
            print(f"  Successfully inserted/updated {len(response.data)} chunks in Supabase.")
            return len(response.data)
        else:
            # Check for specific error messages if available
            error_message = "Unknown error during chunk insert"
            if hasattr(response, 'error') and response.error and hasattr(response.error, 'message'):
                error_message = response.error.message
            elif hasattr(response, 'message'):
                 error_message = response.message # some responses might have message directly
            print(f"  ERROR storing chunks in Supabase: {error_message}")
            if error_message and 'violates unique constraint "document_chunks_document_id_chunk_sequence_key"' in error_message:
                print("  Hint: This might be due to trying to re-insert existing chunks without proper upsert logic or prior deletion for updated documents.")
            return 0
    except Exception as e:
        print(f"  EXCEPTION during Supabase chunk insertion: {e}")
        return 0

def process_document(
    supabase: Client,
    llm_summary_model: genai.GenerativeModel,
    file_path_on_host: Path,
    source_uri: str,
    document_type: str,
    title: str,
    chunking_config: dict,
    generate_summaries: bool = True 
):
    print(f"\n--- Processing Document: {title} ({source_uri}) ---")
    print(f"--- Source File Path: {file_path_on_host} ---")

    if not file_path_on_host.exists():
        print(f"ERROR: Source file not found: {file_path_on_host}")
        return 0

    try:
        with open(file_path_on_host, "r", encoding="utf-8") as f:
            content = f.read()
        print(f"Read file, length: {len(content)} characters.")
    except Exception as e:
        print(f"ERROR reading file {file_path_on_host}: {e}")
        return 0

    content_hash = generate_content_hash(content)
    print(f"Generated content hash: {content_hash}")

    # Check if document exists and if content is unchanged
    # Using 'document_id' as the primary key name based on previous discussion
    db_document_response = supabase.table("documents").select("document_id, content_hash").eq("source_uri", source_uri).maybe_single().execute()
    
    doc_id_for_chunks = None
    # Ensure db_document_response itself is not None before trying to access .data
    if db_document_response and hasattr(db_document_response, 'data'):
        db_document_data = db_document_response.data
    else:
        # If db_document_response is None or has no data attribute, treat as if no document data was found.
        # This could happen if there's an issue with the Supabase call itself, not just an empty result.
        print(f"  WARN: No valid response or data received from Supabase for document lookup: {source_uri}. Proceeding as if document is new or lookup failed.")
        db_document_data = None


    if db_document_data:
        doc_id_for_chunks = db_document_data.get("document_id") # Use .get for safety
        if db_document_data.get("content_hash") == content_hash:
            print(f"Document '{title}' (source_uri: {source_uri}) found with matching content hash. Verifying chunks...")
            chunk_check_response = supabase.table("document_chunks").select("document_id", count="exact").eq("document_id", doc_id_for_chunks).limit(1).execute()
            if chunk_check_response.count and chunk_check_response.count > 0:
                print(f"  {chunk_check_response.count} chunks already exist for document_id {doc_id_for_chunks}. Skipping ingestion for this document.")
                return chunk_check_response.count # Return number of existing chunks
            else:
                print(f"  No chunks found for existing document_id {doc_id_for_chunks} despite matching hash. Proceeding to chunk.")
        else:
            print(f"Document '{title}' found, but content_hash differs or was missing. Updating document and re-processing chunks.")
            if doc_id_for_chunks:
                supabase.table("document_chunks").delete().eq("document_id", doc_id_for_chunks).execute() # Delete old chunks
                print(f"  Old chunks deleted for document_id: {doc_id_for_chunks}.")
                supabase.table("documents").update({
                    "full_text_content": content,
                    "content_hash": content_hash,
                    "last_updated_at": "now()",
                    "title": title, # Ensure title is updated if it changed
                    "document_type": document_type # Ensure type is updated
                }).eq("document_id", doc_id_for_chunks).execute() # Use document_id for .eq
                print(f"  Document record updated for document_id: {doc_id_for_chunks}.")
            else:
                print(f"  ERROR: Could not retrieve document_id for existing document {source_uri} to update. This shouldn't happen.")
                return 0 # Stop processing this doc if ID is missing for update
    else:
        print(f"Document '{title}' not found. Inserting new document record.")
        doc_data_to_insert = {
            "source_uri": source_uri,
            "document_type": document_type,
            "title": title,
            "full_text_content": content,
            "metadata": {"original_file_path": str(file_path_on_host)},
            "content_hash": content_hash,
        }
        response = supabase.table("documents").insert(doc_data_to_insert).execute()
        if response.data and len(response.data) > 0:
            doc_id_for_chunks = response.data[0].get("document_id") # Supabase returns a list, .get for safety
            print(f"  New document record inserted with id: {doc_id_for_chunks}")
        else:
            error_message = "Unknown error during document insert"
            if hasattr(response, 'error') and response.error and hasattr(response.error, 'message'):
                error_message = response.error.message
            print(f"  ERROR inserting new document record: {error_message}")
            return 0

    if not doc_id_for_chunks:
        print(f"FATAL: Could not obtain document_id for {title}. Aborting processing for this document.")
        return 0

    # Chunking
    raw_chunks_text = []
    strategy = chunking_config["strategy"]
    
    if strategy == "markdown_header":
        print(f"Applying MarkdownHeaderTextSplitter for '{title}'...")
        headers_to_split_on = chunking_config.get("headers_to_split_on", [("#", "H1"), ("##", "H2"), ("###", "H3"), ("####", "H4")])
        strip_headers = chunking_config.get("strip_headers", False)
        markdown_splitter = MarkdownHeaderTextSplitter(headers_to_split_on=headers_to_split_on, strip_headers=strip_headers)
        try:
            split_docs = markdown_splitter.split_text(content)
            semantic_chunks_from_markdown = [doc.page_content for doc in split_docs if doc.page_content.strip()]
            print(f"  Initial semantic markdown chunks: {len(semantic_chunks_from_markdown)}")

            final_markdown_chunks = []
            max_sem_chunk_len = chunking_config.get("max_semantic_chunk_chars", 6000)
            sub_chunk_size = chunking_config.get("recursive_sub_chunk_size", 3000)
            sub_chunk_overlap = chunking_config.get("recursive_sub_chunk_overlap", 300)
            
            recursive_splitter_for_oversized = RecursiveCharacterTextSplitter(
                chunk_size=sub_chunk_size,
                chunk_overlap=sub_chunk_overlap
            )
            for sem_chunk in semantic_chunks_from_markdown:
                if len(sem_chunk) > max_sem_chunk_len:
                    print(f"    Semantic chunk (len {len(sem_chunk)}) too large, sub-dividing...")
                    sub_chunks = recursive_splitter_for_oversized.split_text(sem_chunk)
                    final_markdown_chunks.extend(sub_chunks)
                    print(f"      Sub-divided into {len(sub_chunks)} smaller chunks.")
                else:
                    final_markdown_chunks.append(sem_chunk)
            raw_chunks_text = final_markdown_chunks
        except Exception as e_md_split:
            print(f"  ERROR during Markdown splitting for '{title}': {e_md_split}. Falling back to recursive char split.")
            strategy = "recursive_char_large"
            # content variable is already set for fallback

    if strategy == "recursive_char_large":
        print(f"Applying RecursiveCharacterTextSplitter for '{title}'...")
        chunk_size = chunking_config.get("chunk_size", 6000)
        chunk_overlap = chunking_config.get("chunk_overlap", 400)
        separators = chunking_config.get("separators", ["\n\n\n", "\n\n", "\n", ". ", "? ", "! ", " ", ""])
        
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            separators=separators,
            length_function=len,
            is_separator_regex=False,
        )
        raw_chunks_text = text_splitter.split_text(content)

    if not raw_chunks_text:
        print(f"No chunks generated for '{title}'. Check content or chunking strategy.")
        return 0
    print(f"Total chunks generated for '{title}': {len(raw_chunks_text)}")

    chunks_for_db_insert = []
    total_processed_chunks_count = 0
    summary_context_text = content[:MAX_TOKENS_FOR_SUMMARY_CONTEXT * 2]

    for i, chunk_text_content in enumerate(raw_chunks_text):
        if not chunk_text_content.strip():
            print(f"  Skipping empty chunk {i+1} for '{title}'.")
            continue

        current_summary = None
        if generate_summaries:
            current_summary = get_contextual_summary_for_chunk(summary_context_text, chunk_text_content, title, llm_summary_model)
            time.sleep(3) # Increased from 1 to 3 seconds
        
        chunks_for_db_insert.append({
            "document_id": doc_id_for_chunks,
            "chunk_text": chunk_text_content,
            "chunk_sequence": i + 1,
            "contextual_summary": current_summary,
            "document_title": title,
            "metadata": {"original_chunk_length": len(chunk_text_content)}
        })

        if len(chunks_for_db_insert) >= 50:
            total_processed_chunks_count += store_chunks_in_supabase(supabase_client, chunks_for_db_insert)
            chunks_for_db_insert = []

    if chunks_for_db_insert:
        total_processed_chunks_count += store_chunks_in_supabase(supabase_client, chunks_for_db_insert)

    print(f"--- Finished processing and storing for document: {title}. Total chunks stored: {total_processed_chunks_count} ---")
    return total_processed_chunks_count

# --- Main Execution ---
def main():
    print("Starting Day 2: Document Ingestion & Strategic Contextualization Script...")
    start_time = time.time()

    documents_to_process = [
        {
            "file_path_on_host": PLANNING_DOCS_DIR_HOST_OS / "Business_Plan_Dozer_V8.md",
            "source_uri": "dozers_blueprint_v8",
            "document_type": "BUSINESS_PLAN",
            "title": "Dozer's Blueprint V8.0",
            "chunking_config": {
                "strategy": "markdown_header",
                "headers_to_split_on": [("#", "H1"), ("##", "H2"), ("###", "H3"), ("####", "H4")],
                "strip_headers": False,
                "max_semantic_chunk_chars": 6000, 
                "recursive_sub_chunk_size": 3000,
                "recursive_sub_chunk_overlap": 300
            },
            "generate_summaries": True
        },
        {
            "file_path_on_host": PLANNING_DOCS_DIR_HOST_OS / "DozerAI_Dev_Chat_HistoryV1.txt",
            "source_uri": "dozerai_dev_chat_history_v1",
            "document_type": "CHAT_HISTORY_DOZERAI_DEV",
            "title": "DozerAI Development Chat History V1",
            "chunking_config": {
                "strategy": "recursive_char_large",
                "chunk_size": 6000, 
                "chunk_overlap": 400,
                "separators": ["\n\n\n", "\n\n", "\n", ". ", "? ", "! ", " ", ""]
            },
            "generate_summaries": False
        },
        {
            "file_path_on_host": PLANNING_DOCS_DIR_HOST_OS / "Business_Plan_Chat_HistoryV1.txt",
            "source_uri": "business_plan_chat_history_v1",
            "document_type": "CHAT_HISTORY_BUSINESS_PLAN",
            "title": "Business Plan Development Chat History V1",
            "chunking_config": {
                "strategy": "recursive_char_large",
                "chunk_size": 6000,
                "chunk_overlap": 400,
                "separators": ["\n\n\n", "\n\n", "\n", ". ", "? ", "! ", " ", ""]
            },
            "generate_summaries": False
        }
    ]

    total_chunks_ingested_all_docs = 0
    for doc_info in documents_to_process:
        total_chunks_ingested_all_docs += process_document(
            supabase_client,
            context_gen_model,
            doc_info["file_path_on_host"],
            doc_info["source_uri"],
            doc_info["document_type"],
            doc_info["title"],
            doc_info["chunking_config"],
            doc_info["generate_summaries"]
        )
    
    end_time = time.time()
    print(f"\nScript finished in {end_time - start_time:.2f} seconds.")
    print(f"Total chunks ingested across all documents: {total_chunks_ingested_all_docs}")
    print("Check Supabase 'documents' and 'document_chunks' tables.")

if __name__ == "__main__":
    main() 