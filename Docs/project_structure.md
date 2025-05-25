# DozerAI & Dozer Employee App Suite Project Structure

**Absolute Project Root:** `C:\Dozers\`
**Documentation Root:** `C:\Dozers\Docs\`
**Application Code Root:** `C:\Dozers\DozerAI_Code\`

**Note:** This document outlines the file structure for the Development environment. Test and Production environments will mirror this structure with environment-specific configurations, databases, and logs, typically managed in cloud deployments or separate secure servers. The canonical definition is maintained at `C:\Dozers\Docs\project_structure.md`. DozerAI_Builder MUST update this document AND `C:\Dozers\Docs\logs\migration_tracker.md` upon ANY structural change within `C:\Dozers\DozerAI_Code\`.

## Top Level Structure of `C:\Dozers\` (Git Repository Root)
Use code with caution.
Markdown
C:\Dozers
│
├── Docs\ # All project documentation, guides, logs, memory bank
│ ├── DozerAI_CreationGuide_V1.md
│ ├── DozerAI_Development_Guide_V1.md (Contains daily dev tasks)
│ ├── DozerAI_Rules_V1.md (Guiding rules for DozerAI_Builder)
│ ├── project_structure.md (This file - canonical structure)
│ ├── tasks.md (Daily task tracking list)
│ ├── DozerAI_context_for_AI.md (AI Builder's memory aid)
│ ├── Business_Plan_Dozer_V8.md (Core business plan document)
│ ├── daily_progress
│ │ └── daily_context_log.md (Log of daily progress, decisions, vibe)
│ ├── logs
│ │ ├── issues.log (Non-critical issues, bugs, suggestions)
│ │ ├── errors.log (Critical errors, script crashes)
│ │ ├── rules_check.log (Log of pre-action rule compliance checks)
│ │ └── migration_tracker.md (Log of file system changes to DozerAI_Code)
│ └── memory_bank\ # Detailed context files for AI Builder
│ ├── DozerAI_projectbrief.md
│ ├── DozerAI_productContext.md
│ ├── DozerAI_activeContext.md
│ ├── DozerAI_systemPatterns.md
│ ├── DozerAI_techContext.md
│ └── DozerAI_progress.md
│
├── DozerAI_Code\ # All application source code (Detailed in next section)
│ └── ...
│
├── .cursor\ # Cursor.io specific files (managed by Cursor at this root level)
│ └── rules
│ └── rulesfordozerai.mdc # Mirrored rules file (name confirmed by Anthony)
│
├── .git\ # Git repository data (managed by Git)
└── .gitignore # Git ignore file for the entire C:\Dozers\ project
## Detailed Structure of `C:\Dozers\DozerAI_Code\` (Application Code Root)
Use code with caution.
DozerAI_Code
│
├── app\ # Frontend Source Code for Dozer Employee App Suite (Framework: React+Vite initial plan, Electron wrapper later)
│ ├── public\ # Static assets served directly (index.html, favicons, manifest.json for PWA)
│ ├── src\ # Main source code for the frontend application
│ │ ├── assets\ # Project-specific static assets (images, icons, fonts for Dozer's branding)
│ │ ├── components\ # Reusable UI Components
│ │ │ ├── common\ # Buttons, Modals, Layout elements, Loaders
│ │ │ ├── auth\ # Authentication related UI (Login, Signup forms) - e.g., AuthComponent.jsx
│ │ │ ├── chat\ # Components for AI chat and team messenger - e.g., ChatInterface.jsx, MessageList.jsx, MessageInput.jsx
│ │ │ ├── tasks\ # Task list, task item, task detail, task sign-off components
│ │ │ ├── schedule\ # Calendar views, shift display components
│ │ │ ├── time_clock\ # Clock-in/out buttons, status display
│ │ │ ├── meeting_notes\ # Editor, viewer for notes, transcript display, audio linking
│ │ │ └── suggestions\ # Form and display for suggestions
│ │ ├── contexts\ # React Context API providers (e.g., AuthContext.jsx, ThemeContext.jsx)
│ │ ├── features\ # Higher-level feature modules/views combining components and logic
│ │ │ ├── DashboardView.jsx
│ │ │ ├── MessengerView.jsx
│ │ │ ├── TaskBoardView.jsx
│ │ │ └── HRPortalView.jsx
│ │ ├── hooks\ # Custom React hooks
│ │ ├── services\ # Frontend services
│ │ │ ├── supabaseClient.js # Supabase JS client initialization
│ │ │ ├── aguiClient.js # Logic for handling AG-UI EventSource connection & events
│ │ │ └── apiClient.js # Wrapper for making calls to DozerAI backend (FastAPI)
│ │ ├── store\ # Global state management (e.g., Zustand, Redux Toolkit - if needed)
│ │ ├── styles\ # Global styles, Tailwind base overrides (beyond index.css)
│ │ ├── utils\ # Utility functions for the frontend
│ │ ├── App.jsx # Root React component
│ │ └── main.jsx # Entry point for the React application (renders App.jsx)
│ ├── .env # Frontend specific environment variables (VITE_SUPABASE_URL etc. - gitignored)
│ ├── .eslintrc.cjs # ESLint configuration
│ ├── index.html # Main HTML file for Vite
│ ├── package.json # NPM/Yarn dependencies and scripts for the frontend
│ ├── postcss.config.js # PostCSS configuration (for Tailwind)
│ ├── tailwind.config.js # Tailwind CSS configuration
│ └── vite.config.js # Vite build configuration
│
├── config\ # Application Configuration Files for Backend (MUST be in .gitignore if containing secrets)
│ ├── .env # Environment variables (API keys for LLMs, Supabase Service Key, n8n secrets, Neo4j creds, Langfuse creds)
│ └── settings.toml # General non-secret application settings, agent behavior tunables, feature flags, LLM model names
│
├── data\ # Local development data generated/cached by DozerAI (NOT "The Kennel" itself which is Supabase)
│ ├── local_mem0_cache\ # If Mem0 uses local file persistence for dev caching (e.g., its ChromaDB files)
│ ├── local_graphiti_db\ # If Graphiti uses a local file DB for dev (e.g., local Neo4j data files or other)
│ └── local_neo4j_data\ # Persistent data volume for local Neo4j Docker container
│
├── engine\ # Python Backend: DozerAI Agents & Core Logic
│ ├── agents\ # Individual Pydantic AI agent definitions
│ │ ├── prime\ # Dozer Prime specific modules (orchestration logic, LangGraph nodes)
│ │ │ ├── dozer_prime.py # Main class/logic for Dozer Prime
│ │ │ └── dozer_prime_agent_nodes.py # LangGraph node functions for Dozer Prime
│ │ ├── sub_agents\ # Specialized sub-agents (Pydantic AI based)
│ │ │ ├── financial_fox.py
│ │ │ ├── architectural_artisan.py
│ │ │ ├── market_maven.py
│ │ │ ├── operational_owl.py
│ │ │ ├── hr_pawsitive.py
│ │ │ ├── content_coyote.py
│ │ │ └── culinary_coyote.py
│ │ ├── pack_members\ # Templates and core logic for Pack Member employee agents
│ │ │ ├── pack_member_template.py # Base template for Pack Member agents
│ │ │ └── role_specific_configs\ # Directory for role-specific prompts/tool configs
│ │ └── base_agent_utils.py # Common utilities or base class elements for Pydantic AI agents
│ ├── core\ # Core services and integrations for DozerAI backend
│ │ ├── kennel_client.py # Module for interacting with Supabase ("The Kennel" - RAG, CAG, structured data)
│ │ ├── mem0_client.py # Module for Mem0 interaction and memory management
│ │ ├── graph_db_client.py # Module for Neo4j interaction (for Graphiti)
│ │ ├── langgraph_flows\ # LangGraph state definitions and compiled/defined graph flows
│ │ │ ├── prime_main_flow.py # Dozer Prime's main orchestration graph
│ │ │ └── sub_task_generic_flow.py # Example of a reusable sub-flow
│ │ ├── crewai_crews\ # crewAI crew definitions and task structures
│ │ │ ├── marketing_campaign_crew.py
│ │ │ └── new_sop_development_crew.py
│ │ ├── rbac_manager.py # Role-Based Access Control logic interfacing with Supabase RLS
│ │ ├── contextual_retrieval_processor.py # Logic for Anthropic-style contextual retrieval
│ │ ├── llm_services.py # Centralized LLM client initialization (Google, OpenAI, Anthropic)
│ │ ├── observability.py # Langfuse client initialization and helper functions
│ │ ├── schemas.py # Pydantic models for API I/O, LangGraph states, AG-UI types (Python side)
│ │ └── text_processing.py # Chunking, parsing utilities
│ ├── services\ # FastAPI application and API endpoints
│ │ ├── main_api.py # FastAPI app instantiation and core routers/middleware
│ │ └── routers\ # API routers for different functionalities
│ │ ├── prime_interaction_router.py # AG-UI and legacy endpoints for Dozer Prime
│ │ ├── app_suite_hr_router.py # Endpoints for App Suite HR features (tasks, timeclock)
│ │ └── app_suite_comms_router.py # Endpoints for App Suite messenger
│ └── tools\ # Internal tools callable by agents (not n8n external tools)
│ ├── financial_analysis_tools.py
│ └── document_summary_tools.py
│
├── n8n_setup\ # Configuration and exported workflow JSONs for self-hosted n8n
│ ├── docker-compose.yml # For running n8n instance locally via Docker (can be part of main docker-compose.dev.yml)
│ ├── workflows\ # Directory to store exported n8n workflow JSON files (version controlled)
│ │ ├── social_media_post_workflow.json
│ │ ├── pos_data_sync_workflow.json
│ │ ├── accounting_update_workflow.json
│ │ ├── elevenlabs_tts_workflow.json
│ │ └── rfid_time_clock_event_workflow.json
│ └── custom_nodes\ # If we develop custom n8n nodes (advanced use case)
│
├── scripts\ # Utility, data ingestion (Blueprint, tax codes, biz practices, software docs), DB seeding, eval runners
│ ├── db_schemas\ # SQL DDL scripts for initial Supabase schema setup
│ │ ├── 001_initial_setup.sql
│ │ └── ... (002 to 008 as previously defined)
│ ├── ingest_business_blueprint_v8.py
│ ├── ingest_our_chat_history.py
│ ├── ingest_tax_codes_wv.py
│ ├── ingest_building_codes_granville.py
│ ├── ingest_software_manuals
│ ├── seed_supabase_roles_permissions.py
│ └── run_langfuse_eval_suite.py
│
├── tests\ # Automated tests (unit, integration, e2e)
│ ├── engine\ # Backend tests
│ │ ├── agents
│ │ ├── core
│ │ └── services
│ └── app\ # Frontend tests
│
├── .gitattributes # For handling line endings, etc.
├── Dockerfile_backend # Dockerfile for the Python backend service for deployment
├── docker-compose.dev.yml # For orchestrating local development environment (backend, Supabase-local, n8n, Neo4j, Redis)
├── README.md # Project overview, setup instructions for DozerAI_Code contents
└── requirements.txt # Python dependencies for the engine
