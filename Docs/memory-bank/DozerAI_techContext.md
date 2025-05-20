---
**5. `C:\Dozers\Docs\memory_bank\DozerAI_techContext.md`**
*(Adapting your DreamerAI `techContext.md` structure and intent)*

```markdown
# DozerAI & App Suite Tech Context

*Last Updated: [YYYY-MM-DD HH:MM:SS - To be updated by DozerAI_Builder]*

## Core Technologies

- **Programming Languages:**
    - Python (Backend: FastAPI, DozerAI Agents, n8n custom nodes if needed, Scripts)
    - JavaScript/TypeScript (Frontend - Dozer Employee App Suite: Framework TBD - React/Vue/Svelte; Electron if used)
- **Frameworks/Libraries (Backend - Python):**
    - **FastAPI:** Primary web framework for DozerAI backend APIs.
    - **Uvicorn:** ASGI server for FastAPI.
    - **LangGraph:** Core orchestration framework for Dozer Prime and complex agent workflows.
    - **crewAI:** Framework for managing collaborative teams of specialized sub-agents.
    - **Pydantic & Pydantic-AI:** Data validation, settings management, structured LLM outputs for all agents and API layers.
    - **Mem0.ai:** For intelligent, self-improving long-term agent memory.
    - **Supabase Python Client / psycopg[binary/pool]:** For interacting with Supabase/PostgreSQL ("The Kennel").
    - **`pgvector` client utilities:** For vector similarity searches.
    - **Neo4j Python Driver / Graphiti Client:** For interacting with the Knowledge Graph.
    - **Langfuse Python SDK:** For LLM observability, tracing, and evaluations.
    - **Requests/HTTPX:** For making HTTP calls (e.g., to n8n webhooks or other APIs directly if needed).
    - **Ollama Python Client:** For interacting with local LLMs (dev/testing).
    - **OpenAI/Anthropic/Google Cloud Vertex AI Python SDKs:** For interacting with cloud LLMs.
    - **python-dotenv, Tomli/Tomlkit:** For configuration management.
    - **Loguru:** For application logging.
    - **Crawl4ai (library):** For web scraping tasks.
    - **LightRAG (principles/components):** Concepts and potentially modules for RAG pipeline.
    - **ElevenLabs Python SDK:** For Text-to-Speech generation.
- **Frameworks/Libraries (Frontend - JS/TS - Specifics TBD based on framework choice):**
    - **Core Framework:** React, Vue, or Svelte.
    - **Desktop Wrapper (Optional):** Electron.
    - **Supabase JS Client:** For authentication, real-time subscriptions, direct Supabase storage/DB access from frontend if appropriate.
    - **State Management:** Redux, Zustand, Pinia, Vuex, etc. (if needed).
    - **UI Component Library:** Material-UI, Tailwind CSS, Bootstrap, etc. (TBD).
    - **SpeechRecognition API (Browser):** For Speech-to-Text.
    - **ElevenLabs JS SDK/API Client:** For playing TTS audio.
- **Databases & Storage:**
    - **Supabase (PostgreSQL):** Primary RDBMS, vector store (`pgvector`), real-time backend, auth, object storage.
    - **Neo4j:** Dedicated Graph Database for Graphiti knowledge graph.
    - **Redis (Optional Backend Cache):** For caching frequently accessed full documents for CAG or other backend data.
- **Workflow Automation:**
    - **n8n (Self-Hosted):** Dockerized instance for external API integrations.
- **Development Tools:**
    - VS Code + Cursor AI (DozerAI_Builder).
    - Git / GitHub (`TheCrypDough/DozerAI2`).
    - Python Virtual Environment (`venv`).
    - Node.js/npm/yarn (for frontend).
    - Docker & Docker Compose (for local dev environment: n8n, Supabase, Neo4j, backend).
    - Langfuse UI (for observability).
    - pgAdmin or similar (for Supabase/Postgres DB inspection).
    - Neo4j Browser (for KG inspection).
    - Context7 (for AI Builder's documentation needs).

## Development Setup (Initial Plan)

- **OS:** Windows 11 Pro (Anthony's primary dev machine). Design for cross-platform cloud deployment.
- **Primary Workspace:** `C:\Dozers\` (Root), `C:\Dozers\DozerAI_Code\` (Code).
- **Python Env:** Managed via `venv` within `C:\Dozers\DozerAI_Code\`.
- **Node Env (Frontend):** Managed via `npm`/`yarn` in `C:\Dozers\DozerAI_Code\app\`.
- **Local Services (via Docker Compose - `docker-compose.dev.yml`):**
    - Supabase (using official Docker image or a community Postgres+pgvector image).
    - Neo4j.
    - Self-hosted n8n.
    - Redis (if chosen for caching).
    - Python/FastAPI backend service for DozerAI.
- **Local LLM (Dev/Testing):** Ollama server running locally with necessary models.
- **Credentials & Configuration:**
    - Secrets in `C:\Dozers\DozerAI_Code\config\.env` (gitignored).
    - Non-secret settings in `C:\Dozers\DozerAI_Code\config\settings.toml`.

## Technical Constraints & Considerations

- **Real-time Performance (App Suite):** Critical for messenger and live updates. Supabase Realtime is designed for this.
- **LLM Latency & Cost:** Ongoing optimization needed. Use smaller models for simpler tasks. Langfuse to monitor. Leverage prompt caching.
- **Data Security & RBAC:** Supabase RLS and backend logic must robustly enforce permissions for all data in "The Kennel" and App Suite functionalities.
- **Scalability:** Architect for cloud deployment. Supabase cloud, Neo4j AuraDB (cloud), and containerized backend services on AWS/GCP/Azure. n8n self-hosted instance may need scaling.
- **Integration Complexity:** Managing interactions between DozerAI agents, "The Kennel," Graphiti, Mem0, n8n, and the App Suite requires careful design of LangGraph flows and Pydantic data models.
- **Offline Capability (App Suite):** To be considered in later phases. Initial build assumes online connectivity.
- **Cross-Platform Frontend:** If Electron is used, ensure build processes for Windows, macOS, Linux. If PWA, ensure good browser compatibility.