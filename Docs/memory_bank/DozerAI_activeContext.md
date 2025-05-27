# DozerAI & App Suite Active Context

*Last Updated: 2025-05-27 01:00:00*

## Current Work Focus

Day 2 (Kennel Ingestion MVP) COMPLETED. Awaiting Day 3 tasks.

## Recent Changes

- **Supabase Schema Initialized:** Successfully executed the `00_initialize_supabase_schema.py` script. All tables, roles, permissions, and RLS policies for "The Kennel" and core App Suite features (Messenger, Tasks, Time Clock, Meetings, Suggestions) are created in the Supabase PostgreSQL database.
- **Python Environment Established:** `venv` created, and initial `requirements.txt` (including `psycopg[binary]`, `python-dotenv`) populated and installed.
- **`.env` Configuration:** `C:\Dozers\DozerAI_Code\config\.env` file structure established for Supabase direct DB connection details, API keys (Google, Langfuse), and other configurations.
- **`.gitignore` Created:** `C:\Dozers\.gitignore` file created and populated to exclude sensitive and unnecessary files from Git.
- **Automated Schema Script:** Developed and successfully ran `00_initialize_supabase_schema.py` using `psycopg` for direct DDL execution, ensuring robust and automated database setup.
- **Troubleshooting & Resolution:** Overcame initial challenges with Supabase connection details in `.env` (parsing, hostname resolution), `psycopg2-binary` installation, `.env` file path detection in script, and PostgreSQL syntax errors in DDL (specifically with `DO $$` blocks and function/trigger definitions). The final script executed successfully in two parts with a commit in between.
- **Day 2 (Document Ingestion Script for Blueprint & Chat Histories) completed:** script developed, debugged (Supabase connections, Gemini API model/response handling, .env issues, venv recreation), and successfully run. Documents (Blueprint, 2x Chat Histories) chunked, Blueprint chunks summarized, and all 1050 chunks stored in Supabase. Added `document_title` to `document_chunks` table and backfilled.

## Next Steps

- Proceed with Day 3 tasks: Anthony to provide Day 3 tasks from `DozerAI_Development_Guide_V1.md`.

## Active Decisions & Considerations

- Confirmed direct database connection using `psycopg` for schema initialization was successful and robust after overcoming initial hurdles.
- The two-part execution strategy for complex DDL in the schema script proved effective.
- Ready to leverage the now-established Supabase tables for Day 2's data ingestion tasks.
- Supabase for Kennel. Self-hosted n8n. Dual RAG/CAG. Integrated App Suite messenger via Supabase Realtime. AG-UI for Backend-Frontend. React+Vite for frontend initial plan. Urgency for 1-Week MVP. Using `gemini-2.5-flash-preview-05-20` for initial summarization.