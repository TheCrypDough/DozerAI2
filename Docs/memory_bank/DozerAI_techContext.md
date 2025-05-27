# DozerAI & App Suite Technical Context (V1.0 - Initial Build)

*Last Updated: 2025-05-27 17:30:00*

## Languages
-   **Backend**: Python (`~3.11` or as per `venv`)
-   **Frontend**: JavaScript/TypeScript (React+Vite planned - Future)

## Backend Core Technologies & Libraries
-   **Framework**: FastAPI (Future for API endpoints)
-   **Orchestration/Agent Logic**: LangGraph (`~0.0.69`), crewAI (Future), Pydantic AI (for Pydantic models `~2.7.1`)
-   **Database Client**: Supabase Python Client (`~2.4.2`)
-   **Vector DB Interaction**: `psycopg[binary]` (`~3.1.18`) / `psycopg2-binary` (`~2.9.9`) for direct SQL if needed, Supabase client for `pgvector` functions.
-   **Data Ingestion/Processing**: `python-dotenv~=1.0.1`, `google-generativeai~=0.5.4`, `markdown-it-py~=3.0.0`, `langchain-text-splitters~=0.2.1`, `langchain-core~=0.2.5`, `tiktoken~=0.7.0`.
-   **Observability**: Langfuse SDK (`~2.25.0`)
-   **Agent Memory**: Mem0.ai (Future)
-   **Knowledge Graph Client**: Neo4j Driver (Future)
-   **Key Scripts Developed**: 
    -   `00_initialize_supabase_schema.py` (DB setup, HNSW index for `document_embeddings`)
    -   `01_ingest_and_contextualize_docs.py` (Doc parsing, chunking, summarizing)
    -   `02_generate_and_store_embeddings.py` (Embedding generation with `text-embedding-004`)
-   **Core Engine Components**: 
    -   `engine/core/kennel_client.py` (Semantic search, document retrieval)
    -   `engine/core/schemas.py` (Pydantic models for RAG)
    -   `engine/core/langgraph_flows/prime_rag_flow.py` (Basic RAG graph)
    -   `engine/agents/prime/dozer_prime.py` (Agent orchestrator for RAG)

## Frontend Core Technologies & Libraries (Planned - Future)
-   **Framework**: React+Vite (Initial plan)
-   **AG-UI Client**: Copilot Kit (React - evaluation pending) or custom EventSource implementation.
-   **State Management**: TBD (e.g., Zustand, Redux Toolkit)
-   **Supabase Client**: Supabase JS Client for realtime features.

## Databases ("The Kennel")
-   **Primary Relational & Vector Store**: Supabase (Cloud-hosted PostgreSQL with `pgvector` extension).
    -   Key Tables: `documents`, `document_chunks`, `document_embeddings` (with HNSW index on `embedding vector_l2_ops`).
    -   `embedding` column (old) removed from `document_chunks`.
-   **Knowledge Graph**: Neo4j (Likely backend for Graphiti - Future).

## LLM Integrations
-   **Google Generative AI**: 
    -   `gemini-2.5-pro-preview-05-06` (Primary for Dozer Prime generation tasks in RAG).
    -   `gemini-2.5-flash-preview-05-20` (For utility tasks like summarization - Day 2).
    -   `text-embedding-004` (For document and query embeddings - 768 dimensions).
-   **OpenAI/Anthropic**: As needed (Future).

## External Services & Tools
-   **Workflow Automation**: n8n (Self-Hosted via Docker - Future setup).
-   **Voice I/O**: ElevenLabs (TTS), Browser SpeechRecognition API (STT) - (Future for App Suite).
-   **Web Crawling**: Crawl4ai MCP (Future).

## DevOps & Development Environment
-   **Version Control**: Git, GitHub (`TheCrypDough/DozerAI2`)
-   **Local Environment**: `C:\Dozers\`, Python Virtual Environment (`venv` or `.venv`)
-   **Containerization**: Docker (For n8n, local DBs, backend services - Future `docker-compose.dev.yml`)
-   **CI/CD**: GitHub Actions (Future).
-   **Documentation Tools**: Context7, AG-UI Docs.

## Core Technologies

- **Programming Languages:**
    - Python (Backend: FastAPI, DozerAI Agents, n8n custom nodes if needed, Scripts)
    - JavaScript/TypeScript (Frontend - Dozer Employee App Suite: React+Vite initial plan; Electron wrapper if used)
- **Frameworks/Libraries (Backend - Python):**
    - **FastAPI:** Primary web framework for DozerAI backend APIs.
    - **Uvicorn:** ASGI server for FastAPI.
    - **LangGraph:** Core orchestration framework for Dozer Prime and complex agent workflows.
    - **crewAI:** Framework for managing collaborative teams of specialized sub-agents.
    - **Pydantic & Pydantic-AI:** Data validation, settings management, structured LLM inputs/outputs for all agents and API layers.
    - **Mem0.ai SDK:** For intelligent, self-improving long-term agent memory.
    - **Supabase Python Client (`supabase-client`):** For interacting with Supabase/PostgreSQL ("The Kennel").
    - **`psycopg[binary,pool]`:** Underlying PostgreSQL driver, used by Supabase client.
    - **Neo4j Python Driver (`neo4j`):** For interacting with Neo4j Knowledge Graph.
    - **Graphiti Client/Libraries (from Zep, if Python SDK exists):** For interacting with Graphiti layer.
    - **Langfuse Python SDK (`langfuse-python`):** For LLM observability, tracing, and evaluations.
    - **Requests/HTTPX:** For making HTTP calls (e.g., to n8n webhooks).
    - **Google Generative AI SDK (`google-generativeai`):** For interacting with Gemini models (primary LLM, embeddings, context-gen).
    - **OpenAI Python SDK (`openai`):** For OpenAI models (backup/specialized use, tiktoken for tokenization).
    - **Anthropic Python SDK (`anthropic`):** For Claude models (backup/specialized use).
    - **`python-dotenv`, `Tomli/Tomlkit`:** For configuration management.
    - **Loguru:** For application logging.
    - **Crawl4ai (library):** For web scraping tasks (likely called via n8n or a dedicated script).
    - **LightRAG (principles/components):** Conceptual approach for RAG pipeline; specific libraries for chunking (e.g., `markdown`, LangChain text splitters) and embedding (`sentence-transformers`, `torch` if local, or provider SDKs).
    - **ElevenLabs Python SDK (`elevenlabs`):** For Text-to-Speech generation from backend.
    - **`ag-ui-protocol` (Python SDK for AG-UI):** For AG-UI core types and `ag_ui.encoder.EventEncoder` to format SSE events from FastAPI.
- **Frameworks/Libraries (Frontend - JS/TS - React+Vite Initial Plan):**
    - **Core Framework:** React (with Vite for build tooling).
    - **Desktop Wrapper (Optional):** Electron.
    *   **AG-UI Consumption:**
        *   **Copilot Kit (`@copilotkit/react-core`, `@copilotkit/react-ui` - Evaluate):** For pre-built React components & hooks for AG-UI.
        *   Or, custom implementation using browser's `EventSource` API for SSE.
        *   `@ag-ui/core` (JS): For AG-UI core types if needed in frontend.
    - **Supabase JS Client (`@supabase/supabase-js`):** For authentication, real-time subscriptions, direct Supabase storage/DB access.
    - **State Management:** Zustand or Redux Toolkit (TBD if complex state is needed beyond component state/React Context).
    - **UI Component Library:** Tailwind CSS (as per guidelines).
    - **Icons:** Lucide React Icons.
    - **HTTP Client:** `axios` or native `fetch`.
    - **SpeechRecognition API (Browser):** For Speech-to-Text.
    - **Audio Playback:** Native HTML5 Audio or library for ElevenLabs TTS.
- **Databases & Storage:**
    - **Supabase (PostgreSQL Cloud):** Primary RDBMS, vector store (`pgvector`), real-time backend, auth, object storage.
    - **Neo4j (Cloud or Self-Hosted Docker for Dev):** Dedicated Graph Database for Graphiti knowledge graph.
    - **Redis (Optional Backend Cache - Docker for Dev):** For caching frequently accessed full documents for CAG or other backend data.
- **Workflow Automation:**
    - **n8n (Self-Hosted):** Dockerized instance for external API integrations.
- **Development Tools & DevOps:**
    - VS Code + Cursor AI (DozerAI_Builder).
    - Git / GitHub (`TheCrypDough/DozerAI2`).
    - Python Virtual Environment (`venv`).
    - Node.js/npm (Vite uses npm or yarn).
    - Docker & Docker Compose (for local dev environment stack: n8n, Neo4j, Redis, Supabase-local-dev-image if used, backend service).
    - Langfuse UI (for observability).
    - pgAdmin or Supabase Studio (for DB inspection).
    - Neo4j Browser (for KG inspection).
    - Context7 (for DozerAI_Builder's documentation needs).
    - Caddy (for reverse proxy/HTTPS in cloud VPS deployment).
    - GitHub Actions (for CI/CD - future).

## Development Setup (Initial Plan)

- **OS:** Windows 11 Pro (Anthony's primary dev machine). Application designed for cross-platform cloud deployment (backend) and web access (frontend).
- **Absolute Project Root:** `C:\Dozers\`.
- **Application Code Root:** `C:\Dozers\DozerAI_Code\`.
- **Python Env:** Managed via `venv` within `C:\Dozers\DozerAI_Code\`.
- **Node Env (Frontend):** Managed via `npm` in `C:\Dozers\DozerAI_Code\app\`.
- **Local Services (via `C:\Dozers\DozerAI_Code\docker-compose.dev.yml`):**
    - Self-hosted n8n.
    - Neo4j.
    - Redis (if implemented for caching).
    - Python/FastAPI backend service for DozerAI.
    - (Optional) Local Supabase instance (via official/community Docker image) for fully offline dev, though Supabase Cloud free tier is primary for dev.
- **Cloud Services (Development):**
    - Supabase Cloud (Free Tier).
    - Langfuse Cloud (Free Tier).
    - LLM Provider APIs (Google AI Studio, OpenAI, Anthropic - using free tiers/credits).
    - ElevenLabs (Free Tier).
- **Credentials & Configuration:**
    - Secrets in `C:\Dozers\DozerAI_Code\config\.env` (gitignored).
    - Non-secret settings in `C:\Dozers\DozerAI_Code\config\settings.toml`.

## Technical Constraints & Considerations

- **Real-time Performance (App Suite & AG-UI):** Critical for messenger, live updates, and streaming agent responses. Supabase Realtime and AG-UI over SSE are key.
- **LLM Latency & Cost:** Constant monitoring (Langfuse) and optimization (model choice, prompt engineering, RAG/CAG effectiveness, caching).
- **Context Window Management:** Gemini 2.5 Pro's large window is an advantage for CAG. For other models/tasks, careful context management is needed.
- **Data Security & RBAC:** Supabase RLS and backend logic must robustly enforce permissions. AG-UI endpoint security.
- **Scalability (Future):** Cloud-native design for backend. Stateless services where possible. Database connection pooling. Load testing.
- **Integration Complexity:** High number of advanced components requires meticulous design of interfaces (Pydantic, AG-UI events) and robust error handling.
- **Self-Hosted n8n/Neo4j Maintenance:** Requires ongoing updates and resource management (especially if deployed to a budget VPS).
- **1-Week MVP Urgency:** Requires ruthless prioritization and focus on core deliverables for business plan assistance.

## Languages: Python (backend), JS/TS (frontend - React+Vite planned).
## Backend Core: FastAPI, LangGraph, crewAI, Pydantic-AI, Mem0.ai. Supabase Client, Neo4j Driver, Langfuse SDK. Python scripts for data ingestion.
## Frontend Core: React+Vite (planned), AG-UI client logic (Copilot Kit eval / custom EventSource), Supabase JS Client.
## Databases: Supabase (Postgres, pgvector), Neo4j. Initial schema and document/chunk tables populated.
## Integrations: n8n (self-hosted Docker). LLMs: Google (Primary - Gemini 2.5 Pro for Prime, `gemini-2.5-flash-preview-05-20` for summarization tasks), OpenAI/Anthropic. ElevenLabs. Crawl4ai.
## Dev Environment: C:\\Dozers\\. Docker Compose for local services. Git/GitHub. Context7. AG-UI Docs. Python venv for script execution.
## Key Libraries: ag-ui-protocol (Python), @ag-ui/core / @ag-ui/client / @copilotkit/react-core (JS - TBD), `google-generativeai`, `supabase`, `python-dotenv`, `langchain-text-splitters`, `tiktoken`.