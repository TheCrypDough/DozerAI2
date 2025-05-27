# DozerAI & App Suite System Design Patterns (V1.0 - Initial Build)

*Last Updated: 2025-05-27 17:30:00*

## Architecture Overview

- **Integrated AI-Powered Business Operating System:** DozerAI (backend AI agent suite) and the Dozer Employee App Suite (frontend Web App, Electron option) form a unified system.
- **AI Core:**
    - **Master Orchestrator (Dozer Prime):** Implements Anthropic Orchestrator-Worker pattern using LangGraph for stateful, cyclical workflow management. Adheres to Cole Medina's 7-Node Agent Blueprint principles for robust design.
    - **Specialized Sub-Agents ("Pack Leaders" / Domain Experts):** Defined with Pydantic AI for clear capabilities and I/O.
    - **Sub-Agent Teams ("Crews"):** crewAI will be used for orchestrating collaboration between multiple sub-agents on complex, multi-step tasks.
- **Knowledge Hub ("The Kennel"):**
    - **Primary Datastore:** Supabase (Cloud-hosted PostgreSQL) for structured business data, document text/chunks, metadata, App Suite data (chat, tasks, HR).
    - **Vector Store:** `pgvector` extension within Supabase for semantic search on embeddings.
    - **RAG/CAG Strategy:** Dual RAG (Anthropic Contextual Retrieval for enriched chunks, LightRAG principles for pipeline, intelligent Markdown chunking) and CAG (full document context for LLM queries). Crawl4ai for web data ingestion using multiple strategies (sitemap, `llms.txt`, recursive).
    - **Knowledge Graph:** Graphiti (from Zep) with Neo4j as the planned backend graph database for entity and relationship mapping.
    - **Agent Memory:** Mem0 for personalized, self-improving long-term memory for Dozer Prime and Pack Member agents, integrated with The Kennel.
- **Application Suite Backend:** Python/FastAPI providing APIs for the Employee App Suite and internal agent services.
- **Application Suite Frontend:** Secure Web App (Framework TBD: React+Vite initial plan, Electron wrapper later), interacting with backend APIs.
- **Communication Patterns:**
    - **Agent-Frontend Interaction:** Standardized through **AG-UI protocol**, using **Server-Sent Events (SSE)** for real-time streaming of agent actions, text, and tool calls from the FastAPI backend to the Dozer Employee App Suite. Copilot Kit to be evaluated for frontend AG-UI consumption.
    - **Internal App Realtime:** Supabase Realtime for integrated team messenger, live task updates, and notifications within the App Suite.
    - **Inter-Agent (Internal DozerAI):** LangGraph state and data passing for Dozer Prime to sub-agents/crews. A2A protocol (with ADK) is a future consideration for advanced modularity or external exposition.
- **External Tool Integration:** Self-hosted n8n provides workflows triggered by DozerAI agents (via webhooks) to interact with third-party APIs (POS, accounting, social media, Google/Microsoft Office tools, ElevenLabs, etc.).
- **Observability & Evaluation:** Langfuse for end-to-end tracing, monitoring, debugging, and evaluation of LLM calls, agent workflows, and n8n interactions.
- **Security Model:** Role-Based Access Control (RBAC) enforced by Supabase Row-Level Security (RLS) and custom logic in the DozerAI backend, governed by configurations derived from the (future) digitized Employee Operations Handbook. Input/output validation with Pydantic-AI.
- **Deployment Pattern (Dev):** Local Docker Compose stack (Python Backend, n8n, Neo4j, Redis). Supabase Cloud, Langfuse Cloud.
- **Deployment Pattern (Prod):** Cloud VPS with Docker Compose stack for backend services, Caddy for HTTPS/reverse proxy. Supabase Cloud. Static web hosting for App Suite frontend.
- **Key Design Philosophies:** "Doing Better" (Continuous Evaluation, Security Depth, Cost Optimization, Scalability Planning), Cole Medina's 7-Node Agent Blueprint (for individual agent design).

## Core Workflows (Examples)

1.  **CEO Query via App Suite (RAG/CAG + Optional Specialist):**
    *   Anthony (CEO) inputs query to Dozer Prime via App Suite (AG-UI/SSE).
    *   FastAPI AG-UI endpoint receives `RunAgentInput`, initiates Langfuse trace.
    *   Invokes Dozer Prime (LangGraph flow).
    *   DP Node 1: Retrieve context (Mem0 for personalized memory, Kennel RAG/CAG on Blueprint/Docs).
    *   DP Node 2 (Router): Decide if specialist needed.
    *   DP Node 3 (Specialist Call - Optional): Delegate to Financial Fox/Architectural Artisan (Pydantic AI Agent). Specialist may use its own tools/RAG.
    *   DP Node 4 (Synthesis): Dozer Prime's LLM generates response using all context.
    *   DP Node 5 (Memory Update): Interaction saved to Mem0.
    *   FastAPI AG-UI endpoint streams AG-UI events (text chunks, tool calls if any) back to App Suite.
    *   Langfuse trace updated.
2.  **Employee Task Sign-Off (App Suite):**
    *   Employee clicks "Sign Off" in App Suite Task UI.
    *   App Suite Frontend POSTs to FastAPI backend API.
    *   Backend API validates user (Supabase Auth), updates Task status in Supabase `tasks` & `task_signoffs` tables.
    *   Supabase Realtime pushes update to relevant subscribed clients (e.g., manager's dashboard).
    *   DozerAI ("HR Pawsitive" or "Operational Owl") might be notified via a DB trigger/webhook (through n8n) to update project stats or notify next in workflow.
3.  **Automated Social Media Post (DozerAI + n8n):**
    *   Dozer Prime (or "Marketing Maverick") decides to create a social media post based on an event or content.
    *   Agent generates content (text, image prompt).
    *   Agent makes structured request to an n8n webhook (via HTTP).
    *   n8n workflow:
        *   Receives data from DozerAI.
        *   (Optional) Calls an image generation API with prompt.
        *   Posts text and image to specified social media platform(s) using n8n nodes.
        *   Returns success/failure status to DozerAI.
    *   Langfuse traces DozerAI's decision and the n8n trigger.

## "Doing Better" Principles in System Patterns:
- **Evaluation:** Langfuse traces will feed into defined metrics. Agent outputs (especially from specialists like Financial Fox) will have structured formats (Pydantic) allowing for easier programmatic evaluation.
- **Security:** RBAC via Supabase RLS is central. AG-UI communication from a secure backend. n8n webhooks secured. Secrets in `.env`.
- **Cost Optimization:** Tiered LLM usage (powerful for Prime, cheaper for utility like Contextual Retrieval summary). Langfuse tracks token costs. Efficient RAG/CAG with caching.
- **Scalability:** Cloud-native DB (Supabase). Dockerized backend services for cloud VPS deployment. Stateless API design where possible.

Overall Architecture: AI-Powered Business OS: DozerAI backend (Python/FastAPI, LangGraph/crewAI, Pydantic agents) + Dozer Employee App Suite frontend (Web App via React/Vite, Electron option).
Knowledge Hub ("The Kennel"): Supabase (Postgres+pgvector for RAG/CAG with Contextual Retrieval), Graphiti/Neo4j (Knowledge Graph), Mem0 (Agent Memory). Data ingestion pipelines established.
Communication: AG-UI/SSE for agent-frontend real-time interaction. Supabase Realtime for in-app messenger and live data updates. LangGraph for internal agent orchestration.
Workflow Automation: Self-hosted n8n for external APIs.
Security Model: RBAC via Supabase RLS & backend logic.
Observability: Langfuse.
Key Patterns: "Doing Better" (Eval, Security, Cost Opt, Scale), 7-Node Agent Blueprint, Human-in-the-Loop (LangGraph), MCP Agent Army principles for tool abstraction via n8n.

## Overall Architecture
AI-Powered Business OS: DozerAI backend (Python/FastAPI, LangGraph/crewAI, Pydantic agents) + Dozer Employee App Suite frontend (Web App via React/Vite, Electron option).

## Knowledge Hub ("The Kennel")
-   **Primary Store**: Supabase (PostgreSQL + `pgvector`)
    -   Manages: Structured business data, App Suite data, document metadata, RAG chunks, document embeddings (`text-embedding-004`).
    -   Features: Auth & RLS, `pgvector` with HNSW indexing for semantic search.
    -   Ingestion: Pipelines established for documents -> chunks -> embeddings.
-   **Knowledge Graph**: Graphiti (from Zep), with Neo4j as likely backend (Future Integration).
-   **Agent Memory**: Mem0 (Future Integration).

## Communication Protocols
-   **Agent-Frontend**: AG-UI/SSE (Real-time interaction - Future).
-   **In-App (App Suite)**: Supabase Realtime (Chat, live data updates - Future).
-   **Internal Agent Orchestration**: LangGraph.

## Workflow Automation
-   Self-hosted n8n for external APIs and tool integration.

## Security Model
-   RBAC via Supabase RLS (applied to core tables) & backend logic.
-   Future: Threat modeling, more granular permissions.

## Observability & Evaluation
-   Langfuse: Integrated for tracing ingestion scripts and RAG flows.
-   Future: Rigorous evaluation framework for RAG, agent performance.

## Key Design Patterns & Principles
-   **"Doing Better"**: Continuous improvement in Evaluation, Security, Cost Optimization, Scalability.
-   **7-Node Agent Blueprint**: (Guiding principle for complex agent design - Future).
-   **Human-in-the-Loop (HITL)**: Via LangGraph for Dozer Prime and complex tasks.
-   **MCP Agent Army**: Abstracting external tools/services via n8n (Future).
-   **RAG (Retrieval Augmented Generation)**: Basic pipeline implemented (Query Embedding -> Semantic Search -> Context Formatting -> LLM Generation).
    -   Current Model: `text-embedding-004` for retrieval, `gemini-2.5-pro-preview-05-06` for generation.
-   **Dual RAG/CAG**: Conceptual (Chunk-level RAG implemented, Full-document CAG for future).