# DozerAI & App Suite System Patterns

*Last Updated: [YYYY-MM-DD HH:MM:SS - To be updated by DozerAI_Builder]*

## Architecture Overview

- **Integrated AI-Powered Business Operating System:** DozerAI (backend AI agent suite) and the Dozer Employee App Suite (frontend) form a unified system.
- **AI Core:**
    - **Master Orchestrator (Dozer Prime):** Implements Anthropic Orchestrator-Worker pattern using LangGraph for stateful, cyclical workflow management.
    - **Specialized Sub-Agents ("Pack Members" / Domain Experts):** Defined with Pydantic AI for clear capabilities and I/O.
    - **Sub-Agent Teams:** crewAI will be used for orchestrating collaboration between multiple sub-agents on complex tasks.
- **Knowledge Hub ("The Kennel"):**
    - **Primary Datastore:** Supabase (PostgreSQL) for structured data, document text/chunks, metadata.
    - **Vector Store:** `pgvector` extension within Supabase for semantic search on embeddings.
    - **RAG/CAG Strategy:** Dual RAG (Contextual Retrieval enriched chunks) and CAG (full document context). LightRAG principles guide the RAG pipeline.
    - **Knowledge Graph:** Graphiti (from Zep) with Neo4j (or advanced Postgres graph features) for entity and relationship mapping.
    - **Agent Memory:** Mem0 for personalized, self-improving long-term memory for agents.
- **Application Suite Backend:** Python/FastAPI providing APIs for the Employee App Suite and internal agent services.
- **Application Suite Frontend:** Framework TBD (React/Vue/Svelte + Electron for desktop), interacting with backend APIs and Supabase Realtime.
- **External Tool Integration:** Self-hosted n8n provides workflows triggered by DozerAI agents (via webhooks) to interact with third-party APIs (POS, accounting, social, ElevenLabs, etc.).
- **Observability:** Langfuse for end-to-end tracing, monitoring, debugging, and evaluation of LLM calls and agent workflows.
- **Security:** Role-Based Access Control (RBAC) enforced by Supabase Row-Level Security (RLS) and custom logic in the DozerAI backend, governed by configurations derived from the Employee Operations Handbook.

## Key Technical Decisions & Patterns

- **Database Strategy:** Supabase (PostgreSQL) chosen for its relational strength, `pgvector` support, real-time capabilities, authentication, and RLS, simplifying "The Kennel" and App Suite backend.
- **Agent Orchestration:** LangGraph for primary Dozer Prime orchestration; crewAI for managing teams of sub-agents.
- **Data Validation & LLM Output Structuring:** Pydantic & Pydantic-AI used extensively for API request/response models, agent communication, tool I/O schemas, and ensuring structured output from LLMs.
- **Workflow Automation Layer:** Self-hosted n8n for integrating with external services, abstracting API complexities from core agent logic.
- **Memory Architecture:** Multi-layered approach: "The Kennel" (raw/processed knowledge), Graphiti (structured relationships), Mem0 (intelligent contextual recall).
- **Contextual Retrieval (RAG):** Anthropic-style context generation for chunks before embedding to enhance retrieval accuracy.
- **Realtime Communication (App Suite):** Supabase Realtime for integrated team messenger and live updates in the App Suite.
- **Configuration Management:** `.env` files for secrets, `settings.toml` for application settings, managed within `C:\Dozers\DozerAI_Code\config\`.
- **"Doing Better" Principles:**
    - **Evaluation:** Langfuse + custom metrics will be used for continuous agent performance evaluation.
    - **Security:** RBAC, Supabase RLS, secure API design, future threat modeling.
    - **Cost Optimization:** Track token usage (Langfuse), use smaller LLMs for utility tasks, leverage prompt caching.
    - **Scalability:** Design for cloud deployment, load testing critical components (Kennel, LangGraph, n8n).

## Component Relationships (Conceptual High-Level)

```mermaid
graph TD
    subgraph Dozer_Employee_App_Suite [Dozer Employee App Suite (Frontend: TBD Framework + Electron)]
        AppUI["UI Panels (Chat, Tasks, HR, etc.)"]
        SupabaseClientJS["Supabase JS Client (Auth, Realtime, Storage)"]
        ElevenLabsIntegrationJS["ElevenLabs JS (for STT/TTS in-app) or via Backend"]
        BackendAPIClient["Backend API Client (to FastAPI)"]
    end

    subgraph DozerAI_Backend [DozerAI Backend (Python/FastAPI on Cloud Provider TBD)]
        APIService["FastAPI Endpoints"]
        DozerPrime["Dozer Prime (LangGraph, Mem0)"]
        SubAgentSystem["Sub-Agents & Crews (Pydantic AI, crewAI, Mem0)"]
        KennelInterface["Kennel Interface (to Supabase)"]
        GraphitiClient["Graphiti Client (to Neo4j/KG DB)"]
        Mem0Client["Mem0 Client"]
        N8N_Trigger["n8n Trigger Module (HTTP to n8n webhooks)"]
        ElevenLabsClientPY["ElevenLabs Python SDK (if backend handles TTS)"]
    end

    subgraph Data_Stores_Knowledge [Data Stores & Knowledge - "The Kennel"]
        SupabaseDB["Supabase (PostgreSQL + pgvector + RLS + Realtime + Auth + Storage)"]
        Neo4j_KG["Neo4j (for Graphiti Knowledge Graph)"]
    end

    subgraph External_Integrations
        N8N_SelfHosted["Self-Hosted n8n (Docker)"]
        ExternalAPIs["External APIs (POS, Social Media, Accounting, etc.)"]
        LLM_Providers["LLM Providers (Google, OpenAI, Anthropic)"]
        ElevenLabsAPI["ElevenLabs API"]
    end

    subgraph Observability
        LangfusePlatform["Langfuse (Tracing, Monitoring, Evals)"]
    end

    AppUI --> SupabaseClientJS
    AppUI --> BackendAPIClient
    AppUI --> ElevenLabsIntegrationJS

    BackendAPIClient --> APIService
    APIService --> DozerPrime
    DozerPrime -- Orchestrates --> SubAgentSystem
    DozerPrime <--> Mem0Client
    SubAgentSystem <--> Mem0Client
    DozerPrime <--> KennelInterface
    SubAgentSystem <--> KennelInterface
    DozerPrime <--> GraphitiClient
    SubAgentSystem <--> GraphitiClient
    DozerPrime --> N8N_Trigger
    SubAgentSystem --> N8N_Trigger
    APIService --> ElevenLabsClientPY

    KennelInterface --> SupabaseDB
    GraphitiClient --> Neo4j_KG
    Mem0Client --> SupabaseDB # Mem0 might store its processed memory in Supabase

    N8N_Trigger --> N8N_SelfHosted
    N8N_SelfHosted --> ExternalAPIs
    DozerPrime -- LLM Calls --> LLM_Providers
    SubAgentSystem -- LLM Calls --> LLM_Providers
    ElevenLabsClientPY --> ElevenLabsAPI
    ElevenLabsIntegrationJS --> ElevenLabsAPI


    DozerPrime -- Logs/Traces --> LangfusePlatform
    SubAgentSystem -- Logs/Traces --> LangfusePlatform
    N8N_SelfHosted -- Potentially Logs --> LangfusePlatform