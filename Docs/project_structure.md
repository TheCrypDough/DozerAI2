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
│ ├── DozerAI_Development_Guide_V1.md (to be created)
│ ├── DozerAI_Rules_V1.md
│ ├── project_structure.md (this file)
│ ├── tasks.md
│ ├── DozerAI_context_for_AI.md
│ ├── Business_Plan_Dozer_V8.md
│ ├── daily_progress
│ │ └── daily_context_log.md
│ ├── logs
│ │ ├── issues.log
│ │ ├── errors.log
│ │ ├── rules_check.log
│ │ └── migration_tracker.md
│ └── memory_bank
│ ├── DozerAI_projectbrief.md
│ ├── DozerAI_productContext.md
│ ├── DozerAI_activeContext.md
│ ├── DozerAI_systemPatterns.md
│ ├── DozerAI_techContext.md
│ └── DozerAI_progress.md
│
├── DozerAI_Code\ # All application source code (Detailed Below)
│
├── .cursor\ # Cursor.io specific files (managed by Cursor at this root level)
│ └── rules
│ └── rulesfordozerai.mdc # Mirrored rules file
│
├── .git\ # Git repository data
└── .gitignore # Git ignore file for the entire C:\Dozers\ project
## Detailed Structure of `C:\Dozers\DozerAI_Code\` (Application Code Root)
Use code with caution.
DozerAI_Code
│
├── app\ # Frontend Source Code for Dozer Employee App Suite (Framework TBD: React/Vue/Svelte + Electron Wrapper)
│ ├── components\ # Reusable UI Components (e.g., ChatWindow, TaskItem, ScheduleView, TimeClockButton)
│ │ ├── common\ # Buttons, Modals, Layout elements
│ │ ├── chat\ # Components specific to the messenger and AI chat
│ │ ├── tasks\ # Task list, task item, task detail components
│ │ ├── schedule\ # Calendar views, shift display components
│ │ ├── time_clock\ # Clock-in/out buttons, status display
│ │ ├── meeting_notes\ # Editor, viewer for notes
│ │ └── suggestions\ # Form for suggestions
│ ├── features\ # Feature-specific modules/slices (logic, state, UI containers)
│ │ ├── messenger
│ │ │ ├── messengerSlice.js # (If using Redux Toolkit or similar state management)
│ │ │ └── MessengerView.jsx
│ │ ├── tasks
│ │ │ ├── tasksSlice.js
│ │ │ └── TasksDashboard.jsx
│ │ ├── schedule
│ │ │ ├── scheduleSlice.js
│ │ │ └── ScheduleCalendar.jsx
│ │ ├── time_clock
│ │ │ ├── timeClockSlice.js
│ │ │ └── TimeClockInterface.jsx
│ │ ├── meeting_notes
│ │ │ ├── meetingNotesSlice.js
│ │ │ └── MeetingNotesEditor.jsx
│ │ └── suggestions
│ │ ├── suggestionsSlice.js
│ │ └── SuggestionsFeed.jsx
│ ├── services\ # Frontend services (e.g., api_client.js for backend communication, supabase_client.js)
│ ├── store\ # Global state management setup (e.g., Redux store, Zustand store)
│ ├── assets\ # Static assets (images, icons, fonts for Dozer's branding)
│ ├── public\ # Files for web deployment (index.html for PWA/Web, manifest.json)
│ ├── main.js # Electron main process file (if Electron is chosen for desktop app)
│ ├── preload.js # Electron preload script (if Electron is chosen)
│ ├── App.jsx # Root React/Vue/Svelte component
│ ├── index.js # Entry point for the frontend application
│ └── package.json # NPM/Yarn dependencies and scripts for the frontend
│
├── config\ # Application Configuration Files (MUST be in .gitignore if containing secrets)
│ ├── .env # Environment variables (API keys for LLMs, Supabase, ElevenLabs, n8n webhook secrets)
│ └── settings.toml # General application settings, agent behavior tunables, feature flags, LLM model choices
│
├── data\ # Local development data generated/cached by DozerAI (Not "The Kennel" itself which is Supabase)
│ ├── local_mem0_cache\ # If Mem0 uses local file persistence for dev caching
│ └── local_graphiti_db\ # If Graphiti uses a local file DB for dev (e.g., local Neo4j data files)
│
├── engine\ # Python Backend: DozerAI Agents & Core Logic
│ ├── agents\ # Individual Pydantic AI agent definitions
│ │ ├── prime\ # Dozer Prime specific modules (orchestration logic)
│ │ │ └── dozer_prime.py # Main class for Dozer Prime
│ │ ├── sub_agents\ # Specialized sub-agents
│ │ │ ├── financial_fox.py
│ │ │ ├── architectural_artisan.py
│ │ │ ├── market_maven.py
│ │ │ ├── operational_owl.py
│ │ │ ├── hr_pawsitive.py
│ │ │ ├── content_coyote.py
│ │ │ └── culinary_coyote.py
│ │ ├── pack_members\ # Templates and core logic for Pack Member employee agents
│ │ │ ├── pack_member_template.py
│ │ │ └── role_specific_configs\ # Configurations for different employee roles
│ │ └── base_agent_utils.py # Base classes or common utilities for agents
│ ├── core\ # Core services and integrations for DozerAI
│ │ ├── kennel_interface.py # Module for interacting with Supabase ("The Kennel" - RAG, CAG, structured data)
│ │ ├── mem0_client.py # Module for Mem0 interaction and memory management
│ │ ├── graphiti_client.py # Module for Graphiti/Neo4j interaction
│ │ ├── langgraph_flows\ # LangGraph state definitions and compiled/defined graph flows
│ │ │ ├── ceo_orchestration_flow.py
│ │ │ └── sub_task_generic_flow.py
│ │ ├── crewai_crews\ # crewAI crew definitions and task structures
│ │ │ ├── marketing_campaign_crew.py
│ │ │ └── new_sop_development_crew.py
│ │ ├── rbac_manager.py # Role-Based Access Control logic interfacing with Supabase RLS
│ │ ├── contextual_retrieval_processor.py # Logic for Anthropic-style contextual retrieval pre-processing
│ │ ├── elevenlabs_service.py # Service for ElevenLabs TTS
│ │ └── n8n_client.py # Client for triggering n8n workflows
│ ├── services\ # FastAPI application and API endpoints
│ │ ├── main_api.py # FastAPI app instantiation and core routers
│ │ └── routers\ # API routers for different functionalities
│ │ ├── app_suite_api.py # Endpoints for App Suite features (tasks, chat, schedule etc.)
│ │ ├── agent_comms_api.py # Endpoints for frontend to interact with agents
│ │ └── admin_api.py # Endpoints for DozerAI admin functions
│ └── tools\ # Internal tools callable by agents (e.g., advanced data parsers, specific calculators)
│ ├── financial_calculators.py
│ └── document_parser_utils.py
│
├── n8n_setup\ # Configuration and exported workflow JSONs for self-hosted n8n
│ ├── docker-compose.yml # For running n8n instance locally via Docker
│ ├── workflows\ # Directory to store exported n8n workflow JSON files
│ │ ├── social_media_post_workflow.json
│ │ ├── pos_data_sync_workflow.json
│ │ ├── accounting_update_workflow.json
│ │ ├── elevenlabs_tts_workflow.json # If routing ElevenLabs calls via n8n
│ │ └── rfid_time_clock_event_workflow.json # For future RFID hardware
│ └── custom_nodes\ # If we develop custom n8n nodes (advanced use case)
│
├── scripts\ # Utility, data ingestion (Blueprint, tax codes, biz practices, software docs), DB seeding, eval runners
│ ├── ingest_business_blueprint_v8.py
│ ├── ingest_our_chat_history.py
│ ├── ingest_tax_codes_wv.py
│ ├── ingest_building_codes_granville.py
│ ├── ingest_software_manuals\ # Subdirectory for various software doc ingestion scripts
│ ├── seed_supabase_roles_permissions.py
│ └── run_langfuse_eval_suite.py
│
├── tests\ # Automated tests (unit, integration, e2e)
│ ├── engine\ # Backend tests
│ │ ├── agents
│ │ └── core
│ └── app\ # Frontend tests
│
├── .gitattributes # For handling line endings, etc.
├── .gitignore # Standard ignores + DozerAI_Code/config/.env, DozerAI_Code/data/, *.pyc, pycache/, DozerAI_Code/app/node_modules/
├── Dockerfile_backend # Dockerfile for the Python backend service for deployment
├── docker-compose.dev.yml # For orchestrating local development environment (backend, Supabase, n8n, Neo4j, Redis)
├── README.md # Project overview, setup instructions for DozerAI_Code contents
└── requirements.txt # Python dependencies for the engine
