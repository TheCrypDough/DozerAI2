# DozerAI & App Suite Active Context

*Last Updated: [YYYY-MM-DD HH:MM:SS - To be updated by DozerAI_Builder]*

## Current Work Focus

Initializing Day 1 of Phase 0: Foundational Setup & Core MVPs.
Task: Supabase Project Setup & "The Kennel" Initial Schema (for DozerAI & App Suite).

## Recent Changes (Project Inception)

- **Project Initialization:** `C:\Dozers\` project directory structure established. Git repository `TheCrypDough/DozerAI2` created and initialized.
- **Core Documentation Established:**
    - `DozerAI_CreationGuide_V1.md` (this file's counterpart) finalized and approved.
    - `DozerAI_Rules_V1.md` finalized and approved.
    - Templates for log files (`daily_context_log.md`, `issues.log`, `errors.log`, `rules_check.log`, `migration_tracker.md`), `tasks.md`, and `DozerAI_context_for_AI.md` adapted for DozerAI.
    - Memory Bank files (`DozerAI_projectbrief.md`, `DozerAI_productContext.md`, `DozerAI_systemPatterns.md`, `DozerAI_techContext.md`, `DozerAI_progress.md`) adapted and initialized.
    - `project_structure.md` adapted for DozerAI & App Suite.
- **Comprehensive Tech Stack Defined:** Key technologies selected including Supabase, LangGraph, Pydantic-AI, Mem0, Graphiti, n8n, Langfuse, crewAI, ElevenLabs, Google LLM (Primary).
- **Expanded Vision for Dozer Employee App Suite:** Confirmed features include integrated messenger, task management with sign-offs, meeting notes/transcripts, schedules, time-off requests, employee time clock (app/RFID), and suggestions box.
- **"Doing Better" Principles Adopted:** Commitment to integrate rigorous evaluation, security depth, cost optimization, and scalability planning from the outset.
- **1-Week MVP Goal Set:** Target a functional DozerAI MVP capable of assisting with "Dozer's Blueprint V8.0" (financials, visuals concepts) within one week.

## Next Steps

- Proceed with Day 1 tasks sequentially as outlined in the `DozerAI_Development_Guide_V1.md` (once drafted based on `DozerAI_CreationGuide_V1.md`).
- Focus on setting up the Supabase project, defining initial schemas for "The Kennel" and core App Suite tables, and enabling `pgvector`.

## Active Decisions & Considerations

- Confirmed Supabase (PostgreSQL + `pgvector`) as the primary database for "The Kennel."
- Confirmed self-hosted n8n as the iPaaS solution.
- Contextual Retrieval (Anthropic style) and Dual RAG/CAG are core RAG strategies.
- The Dozer Employee App Suite will be an integrated platform, not reliant on third-party messengers for core team chat.
- Urgency: The 1-week MVP target requires hyper-focused execution on features directly supporting business plan assistance.