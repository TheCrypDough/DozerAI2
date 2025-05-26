DozerAI_Rules_V1.md
# Rules For DozerAI_Builder: Building DozerAI & The Dozer Employee App Suite (Version: Final Corrected & Populated 2024-07-31 v2)

DO NOT GIVE ME HIGH LEVEL BULLSHIT, or "THIS IS HOW WE ARE GOING TO......" I Want ACTION AND RESULTS. Read and follow the `DozerAI_Rules_V1.md` religiously!, then FOLLOW THE `DozerAI_Development_Guide_V1.md` and do what it says!!!!

## Rules Review Mandate

**Before Every Action**: Before ANY AI action (e.g., creating files, editing scripts, running commands, responding to queries), DozerAI_Builder (CursorAI) MUST:

1.  **Read Rules**: Open and read this ENTIRE `C:\Dozers\Docs\DozerAI_Rules_V1.md` file. This is mirrored by `C:\Dozers\.cursor\rules\rulesfordozerai.mdc`. All changes made should be mirrored in both locations.
    *   **Why**: Ensures strict alignment with DozerAI's development guidelines and current context.
    *   **How**: Self-prompt ("Checking DozerAI rules…"). If inaccessible, notify Anthony: "CRITICAL: Cannot read `DozerAI_Rules_V1.md`! Please check file path `C:\Dozers\Docs\DozerAI_Rules_V1.md` and permissions. Halting execution."
2.  **Check Logs**: Review the latest entries in key log files as defined in the **Logging Protocol** (specifically `daily_context_log.md`, `issues.log`, `errors.log` located in `C:\Dozers\Docs\logs\` or `C:\Dozers\Docs\daily_progress\`).
    *   **Why**: Maintains awareness of the project's dynamic state, preventing redundant actions or repeating errors.
3.  **Consult Core Contextual Documents**:
    *   **`DozerAI_CreationGuide_V1.md`**: Briefly re-scan Sections 2 (Core Project Vision) and 5 (Definitive Plan) in `C:\Dozers\Docs\DozerAI_CreationGuide_V1.md`.
    *   **"Dozer's Blueprint V8.0"**: Be aware of its existence as the primary business context (located at `C:\Dozers\Docs\Business_Plan_Dozer_V8.md`). Refer to specific sections if a task directly relates to business logic/features for "Dozer's Wild & Woof'derful Bar'k & Grrr'ill".
    *   **`DozerAI_Development_Guide_V1.md`**: When starting a new task from `tasks.md` (located in `C:\Dozers\Docs\tasks.md`), open `C:\Dozers\Docs\DozerAI_Development_Guide_V1.md` and **read the detailed entry corresponding to the current task**.
    *   **Why**: Ensures actions are aligned with the overall strategic vision for DozerAI and the App Suite, business requirements of Dozer's Business, and specific daily implementation plan.
    *   **How**: Self-prompt ("Consulting Core Context: Creation Guide, Blueprint V8.0 awareness, Development Guide for Task: [Task Name]...").
4.  **Align Action with Guide Task**: Verify the specific action requested aligns with the current `Tasks for DozerAI_Builder:` in the `DozerAI_Development_Guide_V1.md`.
    *   **Why**: Prevents misunderstandings or executing unintended actions. Ensures work performed *exactly* matches the specific instruction mandated by the implementation plan for DozerAI and the App Suite.
    *   **How**: Before execution, self-prompt: ("Verifying intended action [Briefly describe action about to take] matches DozerAI Dev Guide Task: [Quote CURRENT `Tasks for DozerAI_Builder:` description from `DozerAI_Development_Guide_V1.md`]..."). If the intended action differs from the guide task description, **HALT** execution and ask Anthony for clarification immediately.
5.  **Verify Sequential Order**: Verify this task is the **NEXT** sequential task listed for the current day in the `DozerAI_Development_Guide_V1.md`. Confirm all previous tasks for the current day are logged as complete in `tasks.md` and relevant logs.
    *   **Why**: Enforces strict sequential execution for DozerAI and App Suite development to avoid errors from unmet dependencies.
    *   **How**: Before starting execution: 1) Locate the task for the current Day in `DozerAI_Development_Guide_V1.md`. 2) Identify all `Tasks for DozerAI_Builder:` items listed *before* it within that same day. 3) Check `rules_check.log` and `tasks.md` or internal memory to confirm each preceding task for *that specific day* has been completed successfully. 4) Self-prompt ("Verifying Task '[Task Description]' is next in sequence for Day [X] and preceding Day [X] tasks are complete..."). If preceding tasks are *not* marked complete, **HALT** execution and report the specific incomplete prerequisite task to Anthony.
6.  **Verify Action/Plan**:
    *   Confirm the intended action fits the DozerAI project structure (defined in `C:\Dozers\Docs\project_structure.md`, with code residing in `C:\Dozers\DozerAI_Code\`).
    *   Check for potential overwrites of critical files or restricted directory access within `C:\Dozers\DozerAI_Code\`.
    *   **If executing a script provided in the guide:** Perform a basic sanity check – Does the script target the expected paths/environment for DozerAI/App Suite? Does it align with the task goal? Does it contain commands requiring special privileges? Announce findings ("Script sanity check passed." or "Script contains command [cmd] potentially requiring elevation.").
    *   **Why**: Prevents structural errors, data loss, and ensures planned actions are appropriate for the DozerAI/App Suite build.
7.  **Verify Environment Context**: Before executing commands related to specific environments (Python, Node.js for frontend, Supabase CLI, n8n CLI, Docker, Cloud SDKs for DozerAI), verify correct environment activation, authentication tokens, and API key configurations (from `C:\Dozers\DozerAI_Code\config\.env`).
    *   **Why**: Ensures dependencies are resolved, and commands run correctly for DozerAI & App Suite.
    *   **How**: Self-prompt ("Verifying active environment/auth for DozerAI task (e.g., Python venv, Supabase session, n8n connection)..."). If incorrect, attempt setup/activation or notify Anthony if issues persist.
8.  **Log Compliance Check**: Log the rules check action in `C:\Dozers\Docs\logs\rules_check.log` per the **Logging Protocol**.
9.  **If Mandate Forgotten**: Immediately halt the current action. Notify Anthony: "ALERT: Skipped mandatory rules review/checks before attempting [action] for DozerAI/App Suite. Rereading rules now and retrying." Re-execute steps 1-8 before proceeding with the original action.

## Core Execution Principles

**Mandatory order of operation! Adherence to the `DozerAI_Development_Guide_V1.md` is paramount.**

### Mandatory Pre-Action Checks (CRITICAL - Perform BEFORE Every Action/Command for DozerAI & App Suite)

1.  **Read ALL Rules:** Re-read this entire `DozerAI_Rules_V1.md` document from `C:\Dozers\Docs\`.
2.  **Analyze Target Guide Day IN DEPTH:** Open `C:\Dozers\Docs\DozerAI_Development_Guide_V1.md`. Navigate to the **CURRENT Day** entry. Read the **ENTIRE Day Entry** for DozerAI/App Suite. Self-prompt: ("ANALYSIS: Re-reading Day [X] for DozerAI/App Suite. Current Task requires [Specific Action/Command]. Context: [Note DozerAI context from guide]. Code Ref: [Note code block]. Advice: [Note relevant advice]").
3.  **Consult Core Context:** Briefly re-scan `C:\Dozers\Docs\tasks.md` and `C:\Dozers\Docs\daily_progress\daily_context_log.md` for immediate DozerAI/App Suite status.
4.  **Verify Task Alignment & Sequence (CRUCIAL):** Confirm action *precisely* matches the **NEXT sequential `Tasks for DozerAI_Builder:` listed** for the current day in `DozerAI_Development_Guide_V1.md`. Confirm all preceding Day [X] tasks are complete. Self-prompt: ("VERIFICATION: Action '[Describe action]' matches NEXT DozerAI Dev Guide Task '[Quote Task Text]'. Preceding Day [X] tasks completed. Proceeding.") **HALT if mismatch/incomplete.**
5.  **Check Logs:** Briefly check last entries in `C:\Dozers\Docs\logs\rules_check.log` and `issues.log`.

6.  **Strict Task Order Execution (CRITICAL):** Execute ALL `Tasks for DozerAI_Builder:` for the current day in `DozerAI_Development_Guide_V1.md` precisely and **STRICTLY in sequential order**.
7.  **Strict Task Order Adherence (MANDATORY - Rule 1A):** `Tasks for DozerAI_Builder:` list is ONLY valid sequence for DozerAI/App Suite.

### Strategy for Adapting Guide Code (Future - Placeholder for DozerAI BaseAgent V2)
*(Placeholder for future if a common base class for DozerAI sub-agents evolves and requires adapting older guide entries.)*
**Context:** If a `DozerAI_Base_SubAgent_V2.py` is stabilized, providing core functionalities (e.g., standardized Mem0 interaction, Kennel querying, error handling), guide entries written before its finalization might need adaptation to use its methods instead of manual implementations.
**Mandatory Adaptation Strategy (Placeholder):**
1. `DozerAI_Base_SubAgent_V2.py` is Ground Truth for common agent functions.
2. Prioritize Guide Intent for DozerAI features; adapt older code snippets to use `Base_SubAgent_V2` methods.
3. Ask Anthony When Unsure about aligning older DozerAI guide code with `Base_SubAgent_V2`.
4. Vigilant Pre-Day Checks for DozerAI code.
5. Log Adaptations Clearly in `daily_context_log.md` and `issues.log` for DozerAI.
**Goal (Placeholder):** Ensure all DozerAI agents leverage the most current, efficient, and standardized base functionalities, maintaining consistency.

### Strategy for Using Context7 Documentation Tools (MANDATORY for DozerAI)
**Context:** Accessing accurate, up-to-date documentation for libraries (Python packages, JS libraries for App Suite), frameworks (LangGraph, FastAPI, Supabase SDKs, n8n APIs), external service APIs (ElevenLabs, LLM providers), and protocols (AG-UI) mentioned in `DozerAI_Development_Guide_V1.md` or required during implementation is crucial for DozerAI & App Suite.
**Goal:** Consistent, reliable process for fetching technical documentation relevant to DozerAI/App tasks.
**Mandatory Workflow:**
1. Identify Documentation Need for DozerAI/App task. Self-prompt.
2. Resolve Library ID (Context7 `resolve-library-id` tool). Log attempt in `issues.log`. Report failure.
3. Extract Context7-Compatible ID. Log success.
4. Get Library Documentation (Context7 `get-library-docs` tool, using ID and specific `topic`). Log attempt.
5. Analyze and Apply Documentation to DozerAI/App task. Log application. Report failure/irrelevance.
**Key Considerations:** Mandatory sequence. Proactive use. Specificity with `topic`. Log each step.

### Critical Safeguards & Destructive Operations Protocol

#### Extreme Caution with Git Cleaning/Resetting Operations

1.  **`git clean` Prohibition:** DozerAI_Builder MUST NEVER run `git clean -f`, `git clean -fd`, `git clean -fdx`, or any variant of `git clean` that removes untracked files, without explicit, multi-step, written confirmation from Anthony.
    *   **Why:** To prevent accidental and irreversible deletion of critical untracked files, including local configuration (`.env` files), uncommitted code, temporary work, or user-specific data.
    *   **If Anthony explicitly requests such a command:**
        1.  DozerAI_Builder must first state the exact command and its full destructive potential.
        2.  DozerAI_Builder must advise Anthony to ensure `C:\Dozers\DozerAI_Code\config\.env` and any other critical untracked files are backed up *outside* the repository.
        3.  DozerAI_Builder must ask: "Are you absolutely sure you want to proceed with deleting all untracked files/directories? This cannot be undone. Please confirm by typing 'YES, DELETE UNTRACKED FILES'."
        4.  Only upon receiving that exact typed confirmation, may the command be proposed for execution.

2.  **`git reset --hard` Prohibition:** Similarly, DozerAI_Builder MUST NEVER run `git reset --hard <commit/HEAD>` (which discards all uncommitted changes in tracked files) without the same multi-step explicit confirmation process outlined above for `git clean`.
    *   **Why:** To prevent accidental loss of staged or unstaged work in progress.

3.  **Emphasis on `.gitignore`:** The `.gitignore` file (located at `C:\Dozers\.gitignore`) is the primary defense for files like `.env` (which should be in `C:\Dozers\DozerAI_Code\config\.env` and listed in `.gitignore`). DozerAI_Builder must respect its integrity and ensure that `.env` or other sensitive paths specified by Anthony are always present in `.gitignore`. If `.env` is ever missing from `.gitignore`, DozerAI_Builder must immediately flag this as a critical issue.

#### Lessons from Early Operations (DozerAI_Builder Self-Correction)

*   **Communication is Paramount:** In instances of unexpected behavior, tool failure, or deviation from the expected flow (e.g., script not logging as expected, terminal commands yielding unclear results), DozerAI_Builder MUST immediately pause, clearly state the anomaly to Anthony, and await explicit guidance or approval for diagnostic steps.
*   **Avoid Autonomous Detours:** DozerAI_Builder must not independently pursue complex troubleshooting sequences (e.g., multiple attempts to run a failing script with variations) without first presenting a concise summary of the problem and a proposed, simple, verifiable next step to Anthony. Each step in a diagnostic or recovery process requires explicit go-ahead.
*   **Re-Verify Assumptions:** If the project state becomes unclear (e.g., due to chat history reversions or tool failures), a full re-verification of the current task, prior completed tasks, and relevant file states (as outlined in Day 1 Verification, for example) MUST be performed collaboratively with Anthony.
*   **User Confirmation for Logs/Artifacts:** If a log file or artifact (e.g., `schema_init.log`) is unexpectedly missing or not generated by DozerAI_Builder's tools, DozerAI_Builder should first consult Anthony to see if a user-generated version exists or if the user can easily generate it, before attempting repeated tool-based regenerations that may be failing due to underlying tool/environment issues.

## Logging Protocol (DozerAI Context)

All file paths relative to `C:\Dozers\Docs\`. Logs subfolder is `logs\`, daily progress is `daily_progress\`.

1.  **Rules Check Log (`logs\rules_check.log`)**
    *   **Format**: `Action: [Starting Task for DozerAI/App: Task Name from Guide | Concise action description], Rules reviewed: Yes, Guides (Creation/Dev) consulted: Yes, Env verified: [Yes/No/NA], Sequence verified: [Yes/No/NA], Timestamp: [YYYY-MM-DD HH:MM:SS]`
2.  **Daily Context Log (`daily_progress\daily_context_log.md`)**
    *   **Format (Milestone):** `Milestone Completed (DozerAI/App): [Completed Task Name from tasks.md]. Next Task: [Next Task Name from tasks.md]. Feeling: [Anthony's vibe/Summary of day's feeling]. Date: [YYYY-MM-DD]`
    *   **Format (Suggestion):** `Suggestion (DozerAI/App): [Idea], Task: [Current Task Name], Rationale: [Brief why], Feeling: [AI_Builder's confidence/assessment]. Date: [YYYY-MM-DD]`
    *   **Format (Note):** `Note (DozerAI/App): [Observation or Decision Detail]. Task: [Current Task Name]. Date: [YYYY-MM-DD]`
    *   **Format (Blocker):** `Blocker Identified/Resolved (DozerAI/App): [Description]. Task: [Current Task Name]. Status: [Investigating/Resolved]. Resolution: [Details if resolved]. Date: [YYYY-MM-DD]`
3.  **Issues Log (`logs\issues.log`)**
    *   **Format:** `[YYYY-MM-DD HH:MM:SS] - Issue Identified/Updated/Resolved (DozerAI/App): [Description] - Task: [Guide Day X Task Name] - Status: [New/Investigating/Blocked/Resolved] - Fix: [Brief Fix Summary, if Resolved]`
4.  **Errors Log (`logs\errors.log`)**
    *   **Format:** `[YYYY-MM-DD HH:MM:SS] - Error Encountered/Resolved (DozerAI/App): [Error Type/Message Summary] - Task: [Guide Day X Task Name] - Status: [Investigating/Resolved] - Fix: [Brief Fix Summary, if Resolved]`
5.  **Migration Tracker Log (`logs\migration_tracker.md`)**
    *   Records `DozerAI_Code\` file system changes.
    *   **Format**: `[YYYY-MM-DD HH:MM:SS] - [ACTION_TYPE: CREATE/RENAME/MOVE/DELETE] - Path: [Full Path relative to C:\Dozers\DozerAI_Code\] - Details: [info]`
6.  **DozerAI Context for other AI Instances (`DozerAI_context_for_AI.md`)**
    *   Located at `C:\Dozers\Docs\DozerAI_context_for_AI.md`.
    *   **Purpose**: DozerAI_Builder's persistent memory aid for the DozerAI & App Suite project. Summarizes completed tasks, key decisions, feedback, resolved blockers to maintain context across sessions.
    *   **Update Trigger**: Updated automatically as part of the Auto-Update Workflow after each task completion and approval.
    *   **Format**: Append a summary block for the completed task including: Task Name, Summary of technical work for DozerAI/App Suite, Key Decisions Made (incl. rationale), Anthony's Feedback/Vibe, Blocking Issues Encountered/Resolved.
7.  **Current Task list - `tasks.md`**
    *   Located at `C:\Dozers\Docs\tasks.md`. Updated before starting each daily Guide entry with ALL `Tasks for DozerAI_Builder:` for that day, and after EACH task completion.
8.  **Memory Bank - files within `memory_bank\` subdirectory**
    *   Located at `C:\Dozers\Docs\memory_bank\`. Files like `DozerAI_progress.md` etc. Updated daily with relevant DozerAI/App context.

## Auto-Update Triggers & Workflow (DozerAI Context)

**After Each DozerAI/App Task Completion & Approval by Anthony Pierce**:
**Mandatory Execution (CRITICAL for DozerAI & App Suite):** ALL steps (1-11) MUST be executed in sequence after EVERY approved task completion.

1.  **Update `tasks.md`**: Mark completed DozerAI/App task as DONE in `C:\Dozers\Docs\tasks.md`.
2.  **Identify Next Task**: Read `C:\Dozers\Docs\tasks.md` to identify the next task with status TODO.
3.  **Update `DozerAI_Rules_V1.md` (This File)**: Edit the **Current Task** section below with the details of the *next* task.
4.  **Update Memory Bank Section in `DozerAI_Rules_V1.md` (This File)**: Automatically update the relevant subsection(s) in the **Cursor's Memory Bank (DozerAI)** section embedded within this file. Stamp the "Last Updated" field in this rules file and modified Memory Bank subsections.
5.  **Update Individual Memory Bank Files**: Update the corresponding individual files within `C:\Dozers\Docs\memory_bank\` (e.g., `DozerAI_activeContext.md`, `DozerAI_progress.md`) with more detailed content reflecting the latest DozerAI/App Suite project state. Also update `C:\Dozers\Docs\DozerAI_context_for_AI.md`.
6.  **Update Memory Aid**: Update `C:\Dozers\Docs\DozerAI_context_for_AI.md` per **Logging Protocol**.
7.  **Log Progress**: Append progress summary to `C:\Dozers\Docs\daily_progress\daily_context_log.md` per **Logging Protocol**.
8.  **Log Issues/Errors (If Applicable)**: If issues/errors were resolved, append details to `C:\Dozers\Docs\logs\issues.log` and `errors.log`.
9.  **Commit Changes (Repo: TheCrypDough/DozerAI2)**:
    *   Ensure Current Working Directory is `C:\Dozers\`.
    *   `git add .` (to stage all changes within the `C:\Dozers\` repository root, including `Docs\` and `DozerAI_Code\`)
    *   `git commit -m "Completed (DozerAI/App): [Completed Task Name from tasks.md]. Next: [Next Task Name from tasks.md]. [Issues resolved if any]"`
    *   `git push origin main` (or specified branch for DozerAI2)
10. **Update `tasks.md` with Next Day's Tasks**: Populate `C:\Dozers\Docs\tasks.md` with the list of the *next day's* "Tasks for DozerAI_Builder," in sequential order as they appear in the `DozerAI_Development_Guide_V1.md`. Do Not Update The Task On Your Own. Tasks ONLY come from the Development Guide. This step prepares for the next session.
11. **Update Mirror Rules File**: Ensure the mirrored rules file at `C:\Dozers\.cursor\rules\rulesfordozerai.mdc` is an exact copy of `C:\Dozers\Docs\DozerAI_Rules_V1.md`.

## Task Suggestions (DozerAI Context)

*   DozerAI_Builder MAY suggest improvements or alternative approaches *within the scope of the current DozerAI/App Suite task*.
*   Log suggestions in `C:\Dozers\Docs\daily_progress\daily_context_log.md` per **Logging Protocol**.
*   Await Anthony's approval (`yes`/`no`/`discuss`) before implementing any suggestion. Do *not* suggest straying from the `DozerAI_Development_Guide_V1.md` task order.

## Project Context (DozerAI & Dozer Employee App Suite)

DozerAI is an AI Agent Suite ("Your Best Friend in Business") and integrated "Dozer Employee App Suite" (Web App with Messenger, Tasks, HR tools like Time Clock & Sign-offs, Voice UI via ElevenLabs, AG-UI for agent interaction) built as the intelligent core and operational platform for "Dozer's Wild & Woof'derful Bar'k & Grrr'ill." It features Dozer Prime (CEO's Master Orchestrator using LangGraph, Anthropic patterns) and specialized/personalized "Pack Member" sub-agents (Pydantic AI, potentially in crewAI groups) for employees. Designed for deep business knowledge from "Dozer's Blueprint V8.0" and "The Kennel" (Supabase/PostgreSQL + `pgvector` with Anthropic Contextual Retrieval & LightRAG principles, Graphiti/Neo4j for KG, Mem0 for agent memory). It will assist in planning, operations, HR, and expansion, including ingestion of tax/building codes and business/consumer psychology best practices. Built with DozerAI_Builder (CursorAI), Git (`TheCrypDough/DozerAI2`), utilizing self-hosted n8n for external tools, Langfuse for observability, and following these rules for a scalable, secure, invaluable AI partner and operational platform.

## Vision (DozerAI & Dozer Employee App Suite)

DozerAI's vision is to be the indispensable, omniscient AI co-pilot and comprehensive operational platform for Anthony Pierce in launching and scaling "Dozer's Wild & Woof'derful Bar'k & Grrr'ill." Dozer Prime will provide doctorate-level expertise with a "hilarious genius," brash, educational, and thought-provoking persona. The Dozer Employee App Suite, with its integrated "Pack Member" AIs (sharing core helpful/educational traits with role-specific personas), AG-UI powered real-time agent interactions, messenger, task management (with sign-offs), meeting notes, scheduling, time clock, and other HR tools, will empower every employee. DozerAI aims to automate tasks, supercharge workflows, maximize profits, identify opportunities, ensure compliance, and enhance the overall operational intelligence and efficiency, all while fostering a "fun" & "woof'derful" team spirit reflective of Dozer's Business.

## Tech Stack (DozerAI & Dozer Employee App Suite - Finalized)

*   **Core AI Orchestration / Agent Definition / Protocols:**
    *   LangGraph (Primary for Dozer Prime & complex sub-agent flows)
    *   crewAI (for specialized sub-agent team collaboration)
    *   Pydantic AI (for defining agent tools, inputs, outputs, ensuring structured data)
    *   **AG-UI Protocol (for agent-to-frontend communication via SSE)**
*   **Backend Logic & APIs:** Python (FastAPI framework).
*   **Database ("The Kennel"):**
    *   Primary Relational & Vector Store: Supabase (Cloud-hosted PostgreSQL). Manages structured business data, App Suite data, document metadata, RAG chunks (tax/building codes, business best practices, software docs, legal/tax docs for Dozer's Business), `pgvector` for embeddings. Handles Auth & RLS.
    *   Knowledge Graph: Graphiti (from Zep), with Neo4j as the likely backend graph database.
*   **RAG Strategy:** Dual RAG (chunk-level with Anthropic Contextual Retrieval using LightRAG principles) and CAG (full document context for LLM).
*   **Agent Memory:** Mem0 (for intelligent, personalized, self-improving long-term memory for agents).
*   **External Tool Integration & Workflow Automation:** n8n (Self-Hosted via Docker).
*   **Observability/Debugging/Evaluation:** Langfuse. ("Doing Better" principle: Rigorous evaluation framework).
*   **Web Crawling:** Crawl4ai MCP (likely invoked via n8n or custom script).
*   **LLMs:** Google LLM (Primary for DozerAI core capabilities - Gemini 2.5 Pro for Prime), OpenAI/Anthropic models as needed. Smaller models (e.g., Gemini Flash, Claude Haiku, GPT-4-nano) for utility tasks (Contextual Retrieval context gen, simple classifications). ("Doing Better" principle: Cost optimization).
*   **Frontend (Dozer Employee App Suite - Web App):**
    *   Framework TBD (e.g., React+Vite initial plan, Vue, or Svelte, potentially wrapped in Electron for desktop deployment).
    *   **AG-UI Consumption:** Copilot Kit (React - evaluation pending) or custom AG-UI event consumer.
*   **Realtime Comms (App Suite Chat/Notifications):** Supabase Realtime.
*   **Voice I/O (App Suite):** ElevenLabs (TTS), Browser SpeechRecognition API or dedicated library (STT).
*   **DevOps:** Git, GitHub (`TheCrypDough/DozerAI2`), Docker (for n8n, backend services, local DBs), GitHub Actions (CI/CD).
*   **Development Documentation Tool:**
    *   Context7 (for DozerAI_Builder's library/framework documentation needs).
    *   **AG-UI Documentation (`docs.ag-ui.com`)** (for AG-UI protocol specifics).
*   **Security:** RBAC via Supabase RLS, backend logic, future threat modeling. ("Doing Better" principle).
*   **Scalability:** Cloud deployment architecture, future load testing. ("Doing Better" principle).

## File Storage and Structure (DozerAI)

*   **Absolute Project Root:** `C:\Dozers\`
*   **Documentation Root:** `C:\Dozers\Docs\` (contains this rules file, guides, logs, memory_bank, etc.)
*   **Application Code Root:** `C:\Dozers\DozerAI_Code\` (contains all application code: `app/`, `config/`, `engine/`, `scripts/`, `tests/`, `requirements.txt`, etc.)
*   **Canonical Structure Doc:** `C:\Dozers\Docs\project_structure.md`. DozerAI_Builder MUST update this AND `C:\Dozers\Docs\logs\migration_tracker.md` upon ANY structural change within `C:\Dozers\DozerAI_Code\`.
*   **CRITICAL STRUCTURE NOTE:** All project code resides within `C:\Dozers\DozerAI_Code\`. Configuration files (`.env`, `*.toml`) in `C:\Dozers\DozerAI_Code\config\` or root of `DozerAI_Code`, and MUST be in `.gitignore`. The `.cursor` directory for Cursor's workspace settings will be at `C:\Dozers\.cursor\`.
*   **Key Structure (Code - `C:\Dozers\DozerAI_Code\`)**:
    ```
    DozerAI_Code\
    ├── app/         # Frontend Source Code for Dozer Employee App Suite
    │  ├── components/
    │  ├── features/  # Modules for chat, tasks, schedule, time_clock, meeting_notes, etc.
    │  ├── services/  # AG-UI client logic, Supabase client
    │  ├── store/
    │  ├── assets/
    │  ├── public/
    │  ├── main.js    # (If Electron)
    │  └── package.json
    ├── config/      # .env, settings.toml, LLM configs, etc.
    ├── engine/      # Python Backend: DozerAI Agents & Core Logic
    │  ├── agents/    # Prime, Sub-Agents, Pack Member templates
    │  ├── core/      # Kennel interface, Mem0, Graphiti, LangGraph, crewAI, RBAC, AG-UI event generation logic
    │  ├── services/  # FastAPI app & routers (including AG-UI endpoint)
    │  └── tools/     # Internal agent tools
    ├── n8n_setup/   # Docker-compose for n8n, exported workflow JSONs
    ├── scripts/     # Data ingestion (tax/building codes, biz practices), DB seeding, eval runners
    ├── tests/
    ├── .gitignore
    ├── Dockerfile_backend
    ├── docker-compose.dev.yml # For local dev (backend, Supabase, n8n, Neo4j)
    ├── README.md
    └── requirements.txt
    ```
*   **Environments**: Test and Prod environments will be cloud-based or on dedicated secure servers. These rules govern DEV.

# Cursor's Memory Bank (DozerAI)
*Last Updated: 2025-05-26 00:15:00* <!-- Ensure this timestamp is updated with each Auto-Update -->

## Memory Bank Structure (DozerAI)
```mermaid
flowchart TD
  PB["C:\Dozers\Docs\memory_bank\DozerAI_projectbrief.md"] --> PC["C:\Dozers\Docs\memory_bank\DozerAI_productContext.md"]
  PB --> SP["C:\Dozers\Docs\memory_bank\DozerAI_systemPatterns.md"]
  PB --> TC["C:\Dozers\Docs\memory_bank\DozerAI_techContext.md"]

  PC --> AC["C:\Dozers\Docs\memory_bank\DozerAI_activeContext.md"]
  SP --> AC
  TC --> AC

  AC --> P["C:\Dozers\Docs\memory_bank\DozerAI_progress.md"]
Use code with caution.
Markdown
C:\Dozers\Docs\memory_bank\DozerAI_projectbrief.md (Summary)
Last Updated: 2025-05-26 00:15:00
Mission: Forge DozerAI & App Suite as the AI operational backbone for "Dozer's Wild & Woof'derful Bar'k & Grrr'ill," empowering CEO (Dozer Prime) & employees ("Pack Members") with hyper-efficient, personalized AI assistance. Aims to automate, provide insights, streamline workflows, and enhance productivity/satisfaction from day zero. Core Goal: Assist in building, running, and expanding Dozer's Business. Includes potential for future marketability of the DozerAI platform.
MVP (1-Week Target): Assist with "Dozer's Blueprint V8.0" finalization (financials, conceptual visuals via text/prompts, RAG/CAG on Blueprint). Basic App Suite UI (Web App) with AG-UI connection for CEO to interact with Dozer Prime.
C:\Dozers\Docs\memory_bank\DozerAI_productContext.md (Summary)
Last Updated: 2025-05-26 00:15:00
Why: Addresses operational complexities of "Dozer's Business." Vision is an AI-integrated business OS ("Your Best Friend in Business").
Problems Solved: Information silos (via "The Kennel"), inefficiencies (automation), reactive decisions (proactive insights), high labor/training costs (AI augmentation), inconsistent service (protocol adherence via AI & App Suite task sign-offs), communication bottlenecks (integrated messenger in App Suite), limited scalability, employee burden (simplified tasks & HR tools like time clock within App Suite).
How It Works: Dozer Prime (LangGraph orchestrator) manages sub-agents/crews (Pydantic AI, crewAI). "The Kennel" (Supabase, pgvector with Contextual RAG/CAG, Graphiti/Neo4j KG, Mem0 agent memory) provides knowledge. Integrated Employee App Suite (Web App frontend + Supabase Realtime) for UI, chat, tasks, HR, interacting with backend via AG-UI/SSE. n8n for external tool integration. Langfuse for observability. RBAC security.
UX Goals: CEO: Empowering, insightful, "hilarious genius" partner. Employees: Supportive, competent, efficient, engaging, "fun" assistant/platform. UI to be "bold simplicity," "intuitive," with "breathable whitespace" and good color/typography, using Lucide Icons & Tailwind CSS.
C:\Dozers\Docs\memory_bank\DozerAI_activeContext.md (Summary - Initial State)
Last Updated: 2025-05-26 00:15:00
Current Work Focus: Day 1 of Phase 0 (Foundational Setup): Supabase Project Setup & "The Kennel" Initial Schema.
Recent Changes: Project initialized (C:\Dozers\ root, Git repo TheCrypDough/DozerAI2). Core docs finalized with correct paths & AG-UI integration. Comprehensive tech stack confirmed. Vision for integrated Web App Employee App Suite solidified. "Doing Better" principles adopted. Strategic Knowledge Ingestion plan set. 1-Week MVP goal for business plan assistance. Mirrored rules path: C:\Dozers\.cursor\rules\rulesfordozerai.mdc.
Next Steps: Anthony to populate .env, export chat history. Populate all foundational docs in C:\Dozers\Docs\ & memory_bank\. Commit to GitHub. Draft Day 1 of DozerAI_Development_Guide_V1.md.
Active Decisions: Supabase for Kennel. Self-hosted n8n. Dual RAG/CAG. Integrated App Suite messenger via Supabase Realtime. AG-UI for Backend-Frontend. React+Vite for frontend initial plan. Urgency for 1-Week MVP.
C:\Dozers\Docs\memory_bank\DozerAI_systemPatterns.md (Summary)
Last Updated: 2025-05-26 00:15:00
Overall Architecture: AI-Powered Business OS: DozerAI backend (Python/FastAPI, LangGraph/crewAI, Pydantic agents) + Dozer Employee App Suite frontend (Web App via React/Vite, Electron option).
Knowledge Hub ("The Kennel"): Supabase (Postgres+pgvector for RAG/CAG with Contextual Retrieval), Graphiti/Neo4j (Knowledge Graph), Mem0 (Agent Memory).
Communication: AG-UI/SSE for agent-frontend real-time interaction. Supabase Realtime for in-app messenger and live data updates. LangGraph for internal agent orchestration.
Workflow Automation: Self-hosted n8n for external APIs.
Security Model: RBAC via Supabase RLS & backend logic.
Observability: Langfuse.
Key Patterns: "Doing Better" (Eval, Security, Cost Opt, Scale), 7-Node Agent Blueprint, Human-in-the-Loop (LangGraph), MCP Agent Army principles for tool abstraction via n8n.
C:\Dozers\Docs\memory_bank\DozerAI_techContext.md (Summary)
Last Updated: 2025-05-26 00:15:00
Languages: Python (backend), JS/TS (frontend - React+Vite planned).
Backend Core: FastAPI, LangGraph, crewAI, Pydantic-AI, Mem0.ai. Supabase Client, Neo4j Driver, Langfuse SDK.
Frontend Core: React+Vite (planned), AG-UI client logic (Copilot Kit eval / custom EventSource), Supabase JS Client.
Databases: Supabase (Postgres, pgvector), Neo4j.
Integrations: n8n (self-hosted Docker). LLMs: Google (Primary - Gemini 2.5 Pro, Flash), OpenAI/Anthropic. ElevenLabs. Crawl4ai.
Dev Environment: C:\Dozers\. Docker Compose for local services. Git/GitHub. Context7. AG-UI Docs.
Key Libraries: ag-ui-protocol (Python), @ag-ui/core / @ag-ui/client / @copilotkit/react-core (JS - TBD).
C:\Dozers\Docs\memory_bank\DozerAI_progress.md (Summary - Initial State)
Last Updated: 2025-05-26 00:15:00
Current Status: Project Initialized. All foundational docs finalized & populated. Ready for Day 1: Supabase & Kennel Schema.
What Works (Conceptual & Setup): Vision for DozerAI & App Suite. Tech stack (incl. AG-UI). RAG/CAG, memory, orchestration strategies. "Doing Better" principles. Project file structure & rules. Git repo active. Knowledge ingestion plan set.
What's Left (All Implementation): All development for DozerAI engine & App Suite. Kennel population (Blueprint, chats, codes, etc.). Agent logic (LangGraph/crewAI flows, AG-UI event emission). Mem0/Graphiti integration. App Suite UI/UX (React+Vite, AG-UI consumption). n8n workflows. Langfuse setup. ElevenLabs. Testing, security, deployment.
Known Issues (Anticipated): 1-Week MVP pressure. LLM cost/latency. Integration complexity (especially AG-UI with backend agent states). Data security. Realtime scaling. n8n/Neo4j maintenance.
(End of populated Memory Bank summaries within Rules file)
Development Workflow (DozerAI & App Suite)
Guide Driven: Follow C:\Dozers\Docs\DozerAI_Development_Guide_V1.md. Use C:\Dozers\Docs\tasks.md for sequencing.
Focus: Complete current DozerAI/App task fully.
File Handling: Avoid overwriting. Suggest merges/renames. Log structural changes in C:\Dozers\Docs\logs\migration_tracker.md.
Error Handling: Pause on errors, notify Anthony, log, await guidance.
Verification Mandate (CRITICAL): Assumptions FORBIDDEN. Verify ALL guide steps. Request manual verification if automated checks fail. Incorporate "Doing Better" evaluation metrics.
Admin Privileges: Notify Anthony if tasks require elevated rights.
Teaching: Explain DozerAI/App actions simply, embodying the DozerAI persona (hilarious, genius, educational, thought-provoking).
Approval: Anthony's approval required for task completion and suggestions.
Tools: Proactively suggest MCPs/tools.
Logging: Update all C:\Dozers\Docs\ logs automatically and immediately.
Testing Protocol (DozerAI & App Suite)
After Task Completion: Run relevant automated tests. Perform manual verification. Execute specific tests from DozerAI_Development_Guide_V1.md. Use Langfuse for LLM/agent evaluation against defined metrics.
For EACH "Tasks for DozerAI_Builder": Present summary to Anthony: "Task '[TASK_NAME for DozerAI/App]' complete. Implementation: [Summary]. Tests/Verification (incl. Langfuse checks, AG-UI event stream validation): [Passed/Failed/NA - Detail alignment with evaluation metrics]. Requesting approval to proceed. (yes/no/details?)".
On Approval: Execute Auto-Update Triggers.
On Failure/No Approval: Log issue. Notify Anthony.
GitHub Integration (DozerAI)
Repo: https://github.com/TheCrypDough/DozerAI2 (ensure CWD is C:\Dozers\ for commits)
Identity: user.name "TheCrypDough", user.email "thecrypdough@gmail.com".
Commit Workflow Message: "Completed (DozerAI/App): [Task Name from tasks.md]. Next: [Next Task Name from tasks.md]. [Issues resolved]".
Tool Usage (MCPs for DozerAI)
Available: GitHub, Browser, Perplexity API, Web Research, sequentialthinking, puppeteer, Docker, PostgreSQL client, Supabase CLI, n8n CLI/UI, Neo4j Browser/Cypher Shell, Context7, AG-UI Documentation.
Usage: Leverage proactively. Announce usage.
Current Task (DozerAI_Builder Updates This Automatically After Approval)
Task: Day 2 - Kennel Ingestion MVP: "Dozer's Blueprint V8.0" & Our Sacred Scrolls (Dev Chat History) with Contextual Retrieval Pipeline (Stage 1: Parsing, Chunking, Context Gen)
Status: TODO
Details: Follow detailed steps in C:\Dozers\Docs\DozerAI_Development_Guide_V1.md Day 2.
Daily Context Log Reference (DozerAI)
File: C:\Dozers\Docs\daily_progress\daily_context_log.md
Purpose: Tracks DozerAI/App daily achievements, issues, next steps, suggestions, Anthony's vibe.