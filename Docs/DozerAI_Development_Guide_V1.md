# DozerAI & Dozer Employee App Suite - Development Guide V1.0

## Phase 0: Foundation & Core MVPs for Business Plan Assistance (Target: Days 1-7)

---

**Day 1 - Kennel Foundation: Supabase Connection, Automated Schema Execution Script, Env Config & Gitignore**

**Anthony's Vision (for this DozerAI/App Feature):**
"Okay, DozerAI_Builder, I need 'The Kennel' set up in Supabase *without* me manually copying SQL. You provide a Python script. I put my Supabase keys in the `.env` file. I run *that one script*, and it should create all the tables and everything. I can handle running a Python script. Make it tell me if it worked or if something blew up. This *has* to be automated."

**Description:**
This crucial first day focuses on establishing the cloud-based data infrastructure ("The Kennel") using Supabase and ensuring DozerAI_Builder can programmatically set up the initial schema. We will:
1.  Confirm Anthony has created the Supabase project, enabled `pgvector`, and populated the `C:\Dozers\DozerAI_Code\config\.env` file with critical Supabase credentials (URL, Service Role Key, DB Password, DB Host, DB User, DB Port, DB Name), Google API Key, and Langfuse Keys.
2.  DozerAI_Builder will provide a comprehensive `.gitignore` file to be placed at `C:\Dozers\.gitignore`.
3.  DozerAI_Builder will provide the initial `requirements.txt` for the Python backend.
4.  DozerAI_Builder will create a Python script (`C:\Dozers\DozerAI_Code\scripts\00_initialize_supabase_schema.py`) that uses the `psycopg` (or compatible) library.
5.  This script will read database connection details from the `.env` file.
6.  The script will then programmatically execute the SQL DDL (from our eight defined schema blocks) to create all necessary tables, roles, permissions, types, and RLS policies directly in Anthony's Supabase project.
7.  Anthony will set up his Python environment, install dependencies, and run this single Python script, then verify success.

**Relevant Context (for DozerAI/App Suite):**
*Technical Analysis:* We are using a Python script with the `psycopg` (or compatible `psycopg2-binary` / `psycopg[binary]`) library for direct PostgreSQL DDL execution against Anthony's Supabase-hosted PostgreSQL database. This bypasses potential limitations of the `supabase-py` (PostgREST client) for complex, multi-statement DDL and administrative commands like `CREATE EXTENSION`. The script connects using the standard PostgreSQL protocol, for which Supabase provides connection details via the dashboard. Robust error handling within the Python script will report success or failure for each DDL block. This method automates the schema setup for Anthony and serves as an example of programmatic database interaction.
*Layman’s Terms:* We're still building the digital library ("The Kennel"). DozerAI_Builder is giving Anthony a super-smart robot (Python script). Anthony gives the robot the library keys (`.env` file), including the direct address to the PostgreSQL database that Supabase manages. This time, when Anthony tells the robot "go," the robot will *itself* go into the library and build all the initial shelves and filing systems directly by talking the database's native language, then report back if everything is perfect or if it hit a snag. No manual instruction-following with SQL for Anthony.

**DozerAI_Builder's Thought Input:**
This fully automated script-driven approach for Day 1 is ideal. Using `psycopg` ensures robust DDL execution capabilities. The script must be meticulously crafted with clear success/error reporting for each of the 8 schema blocks to give Anthony confidence and actionable feedback. This provides a clean, automated start to "The Kennel" setup.

**Anthony's Thought Input (for DozerAI/App Development):**
"Yes! One script to run – that's what I need. I can handle getting the `.env` file right with all those database details and running a Python script. If it tells me 'all good' or 'Houston, we have a problem, and here's why,' that's real progress. This is how DozerAI should make my life easier from Day 1!"

**Additional Files, Documentation, Tools, Programs Needed (for DozerAI/App):**
-   Supabase Account & Live Project: (Tool), (Cloud Database Service), (Primary data store), (Already set up by Anthony, `pgvector` enabled).
-   `psycopg[binary]` Python library: (Library), (PostgreSQL database adapter for Python), (Will be added to `requirements.txt` and installed in Python environment).
-   `python-dotenv` Python library: (Library), (For loading `.env` files in Python), (Will be added to `requirements.txt`).
-   `Business_Plan_Dozer_V8.md`: (Document), (Located at `C:\Dozers\Docs\Business_Plan_Dozer_V8.md`), (Core business plan).
-   `DozerAI_Dev_Chat_History.txt`: (Document), (Located at `C:\Dozers\Docs\DozerAI_Dev_Chat_History.txt`), (Our development chat history).

**Any Additional Updates Needed to the Project (DozerAI/App) Due to This Implementation?**
-   `C:\Dozers\DozerAI_Code\config\.env` populated by Anthony (critical with direct DB connection details).
-   `.gitignore` created at `C:\Dozers\.gitignore`.
-   `requirements.txt` created in `C:\Dozers\DozerAI_Code\`.
-   Python script `00_initialize_supabase_schema.py` created in `C:\Dozers\DozerAI_Code\scripts\`.

**DozerAI/App Project/File Structure Update Needed:** Yes.
    - Create directory: `C:\Dozers\DozerAI_Code\config\` (if not exists from Anthony's prep)
    - Create directory: `C:\Dozers\DozerAI_Code\scripts\` (if not exists from Anthony's prep)

**Any Additional Updates Needed to the DozerAI Guide for Changes or Explanation?**
-   This Day 1 entry fully details the script-driven schema execution.

**Any Removals from the DozerAI Guide Needed?**
-   All previous Day 1 plans involving manual SQL execution or Supabase CLI `db push` by Anthony.

**Effect on DozerAI/App Project Timeline:**
-   More initial coding for DozerAI_Builder for the robust Python script. Significantly less manual work, reduced error potential, and increased automation for Anthony, making Day 1 more efficient and aligned with project goals.

**Integration Plan (for DozerAI/App):**
-   **When:** Day 1 (Week 1) – Foundational database schema setup via automated Python script.
-   **Where:** Supabase Cloud platform, local project directory `C:\Dozers\`.
-   **Dependencies (Software):** Python 3.10+, `pip`, Text Editor, Web Browser.
-   **Setup Instructions (Summary):** Anthony ensures Python/pip, populates `.env` with all required Supabase DB connection details. DozerAI_Builder provides Python script and `requirements.txt`. Anthony creates Python virtual environment, installs requirements, and runs the `00_initialize_supabase_schema.py` script.

**Recommended Tools (for DozerAI/App):**
-   Python.
-   Text Editor (VS Code, Notepad++, etc.).
-   Terminal (PowerShell or Git Bash).
-   Supabase Studio (for verifying table creation after script runs).

---
**Tasks for Anthony Pierce (CEO):**

1.  **Confirm Pre-Day 1 Completion (Final Check):**
    *   Verify your Supabase project is created on [supabase.com](https://supabase.com).
    *   Verify `pgvector` extension is ENABLED in your Supabase project dashboard (Database -> Extensions).
    *   Verify Python (3.10+ recommended) and `pip` are installed and accessible from your terminal.
    *   Verify `C:\Dozers\Docs\Business_Plan_Dozer_V8.md` and `C:\Dozers\Docs\DozerAI_Dev_Chat_History.txt` are in place.
2.  **Create Directories (if they don't exist):**
    *   `C:\Dozers\DozerAI_Code\config\`
    *   `C:\Dozers\DozerAI_Code\scripts\`
3.  **Populate `.env` File (CRITICAL - Ensure ALL DB Details are Correct):**
    *   Open/Create `C:\Dozers\DozerAI_Code\config\.env`.
    *   Paste the following content, **replacing ALL placeholders** with your actual credentials. **Get `SUPABASE_DB_HOST`, `SUPABASE_DB_PASSWORD`, etc., from your Supabase Dashboard: Project Settings -> Database -> Connection String (URI).**
        ```env
        # Supabase Configuration (for Python script using psycopg)
        SUPABASE_DB_USER="postgres"
        SUPABASE_DB_PASSWORD="YOUR_DATABASE_PASSWORD_FROM_SUPABASE_DASHBOARD" # Password for the 'postgres' user
        SUPABASE_DB_HOST="db.<your-project-ref>.supabase.co" # e.g., db.abcdefghijklmnopqrs.supabase.co
        SUPABASE_DB_PORT="5432" # Usually 5432 or 6543 for pooled connections, check your connection string
        SUPABASE_DB_NAME="postgres" # Default Supabase database name

        # Supabase API Keys (for supabase-py client if used elsewhere, not directly by this schema script)
        SUPABASE_URL="YOUR_SUPABASE_PROJECT_URL_FROM_DASHBOARD" # e.g., https://xyz.supabase.co
        SUPABASE_SERVICE_ROLE_KEY="YOUR_SUPABASE_SERVICE_ROLE_SECRET_KEY_FROM_DASHBOARD"

        # LLM API Keys
        GOOGLE_API_KEY="YOUR_GOOGLE_AI_STUDIO_API_KEY_FOR_GEMINI"
        OPENAI_API_KEY="" # Optional
        ANTHROPIC_API_KEY="" # Optional
        OPENROUTER_API_KEY="" # Optional

        # Observability - Langfuse
        LANGFUSE_PUBLIC_KEY="YOUR_LANGFUSE_PROJECT_PUBLIC_KEY"
        LANGFUSE_SECRET_KEY="YOUR_LANGFUSE_PROJECT_SECRET_KEY"
        LANGFUSE_HOST="https://cloud.langfuse.com"

        # External Services
        ELEVENLABS_API_KEY=""
        
        # n8n Self-Hosted Configuration (Placeholders)
        N8N_WEBHOOK_URL_BASE="http://localhost:5678/webhook/" 
        N8N_API_KEY_DOZERAI_TRIGGER="YOUR_SECURE_N8N_API_KEY" 
        
        # Neo4j Configuration (Placeholders)
        NEO4J_URI="bolt://localhost:7687" 
        NEO4J_USERNAME="neo4j"
        NEO4J_PASSWORD="YOUR_SECURE_NEO4J_PASSWORD"
        
        # Application Settings
        PYTHON_BACKEND_PORT="8090" 
        FRONTEND_APP_URL="http://localhost:5173" # Default for Vite
        ```
    *   Save the file `C:\Dozers\DozerAI_Code\config\.env`.
4.  **Create `.gitignore` File (at `C:\Dozers\.gitignore`):**
    *   Create `C:\Dozers\.gitignore` and paste the full `.gitignore` content previously provided by DozerAI_Builder (from message "2024-07-31 15:52") into it. Save.
5.  **Create `requirements.txt` (at `C:\Dozers\DozerAI_Code\requirements.txt`):**
    *   Create `C:\Dozers\DozerAI_Code\requirements.txt` and paste the `requirements.txt` content previously provided by DozerAI_Builder (from message "2024-07-31 16:03") into it. Save.
6.  **Create Python Schema Initialization Script:**
    *   Create `C:\Dozers\DozerAI_Code\scripts\00_initialize_supabase_schema.py` and paste the full Python script code (provided by DozerAI_Builder in this current message, directly below the "Tasks for DozerAI_Builder" section) into it. Save.
7.  **Set up Python Virtual Environment & Install Dependencies:**
    *   Open your terminal (PowerShell or Git Bash).
    *   Navigate to the application code root: `cd C:\Dozers\DozerAI_Code\`
    *   Create a virtual environment: `python -m venv venv`
    *   Activate the virtual environment:
        *   PowerShell: `.\venv\Scripts\Activate.ps1`
        *   Git Bash / Cmd: `source venv/Scripts/activate` or `venv\Scripts\activate.bat`
    *   Install required Python packages: `pip install -r requirements.txt`
    *   Confirm successful installation (especially `psycopg[binary]` and `python-dotenv`).
8.  **Run the Automated Schema Initialization Script:**
    *   While the virtual environment is active and you are in `C:\Dozers\DozerAI_Code\`, run:
        ```bash
        python scripts/00_initialize_supabase_schema.py
        ```
    *   Observe the output. The script should print success messages for each of the 8 SQL blocks being executed or report any errors.
    *   **Report to DozerAI_Builder:** State "Python schema script executed successfully and all tables verified in Supabase Studio" OR copy/paste any error messages encountered.
9.  **Verification (Manual):**
    *   After the script runs successfully, log in to your Supabase dashboard.
    *   Go to the "Table Editor." Verify that tables like `roles`, `users`, `documents`, `tasks`, `messages`, `time_clock_entries`, etc., have been created.
10. **Initial Git Commit (After all above is successful):**
    *   This will be done as the *last step* of Day 1.

---
**Tasks for DozerAI_Builder (CursorAI):**

1.  **Confirm Previous Deliverables:** DozerAI_Builder confirms that the full content for `C:\Dozers\.gitignore` and `C:\Dozers\DozerAI_Code\requirements.txt` has already been provided in the immediately preceding messages to Anthony.
2.  **Provide Python Schema Initialization Script (`C:\Dozers\DozerAI_Code\scripts\00_initialize_supabase_schema.py`):**
    *   Provide the full, complete, and corrected Python script that uses `psycopg` to connect to Supabase and execute all eight SQL DDL blocks directly. This script needs robust error handling and clear print statements for Anthony.

    ```python
    # C:\Dozers\DozerAI_Code\scripts\00_initialize_supabase_schema.py
    import os
    import sys
    import time
    from dotenv import load_dotenv
    import psycopg # Using psycopg (psycopg3)

    # --- Load Environment Variables ---
    # Script is in DozerAI_Code/scripts/, .env is in DozerAI_Code/config/
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    ENV_PATH = os.path.join(BASE_DIR, 'config', '.env')

    if not os.path.exists(ENV_PATH):
        print(f"CRITICAL ERROR: .env file not found at {ENV_PATH}")
        print("Ensure C:\\Dozers\\DozerAI_Code\\config\\.env exists and is populated.")
        sys.exit(1)
    load_dotenv(ENV_PATH)

    DB_USER = os.getenv("SUPABASE_DB_USER")
    DB_PASSWORD = os.getenv("SUPABASE_DB_PASSWORD")
    DB_HOST = os.getenv("SUPABASE_DB_HOST")
    DB_PORT = os.getenv("SUPABASE_DB_PORT", "5432") # Default PostgreSQL port
    DB_NAME = os.getenv("SUPABASE_DB_NAME")

    print(f"--- .env Values Loaded by Script ---")
    print(f"DB_USER: {DB_USER}")
    print(f"DB_PASSWORD: {'********' if DB_PASSWORD else 'NOT FOUND'}")
    print(f"DB_HOST: {DB_HOST}")
    print(f"DB_PORT: {DB_PORT}")
    print(f"DB_NAME: {DB_NAME}")
    print(f"------------------------------------")


    if not all([DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME]) or \
       "YOUR_DATABASE_PASSWORD" in DB_PASSWORD or \
       "<your-project-ref>" in DB_HOST:
        print("\nCRITICAL ERROR: One or more Supabase DIRECT DATABASE connection details (DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME) are missing or still placeholders in .env.")
        print(f"Please ensure these are correctly populated in {ENV_PATH} using details from your Supabase Dashboard (Project Settings -> Database -> Connection String URI).")
        sys.exit(1)

    CONN_STRING = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

    # --- SQL Schema Definitions ---
    SQL_001_INITIAL_CORE_TABLES = """
    CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

    CREATE OR REPLACE FUNCTION public.trigger_set_timestamp()
    RETURNS TRIGGER AS $$
    BEGIN
      NEW.updated_at = NOW();
      RETURN NEW;
    END;
    $$ LANGUAGE plpgsql;
    COMMENT ON FUNCTION public.trigger_set_timestamp() IS 'Automatically sets the updated_at timestamp to the current time upon row update.';

    CREATE TABLE IF NOT EXISTS public.app_settings (
        setting_key TEXT PRIMARY KEY,
        setting_value JSONB,
        description TEXT,
        created_at TIMESTAMPTZ DEFAULT now(),
        updated_at TIMESTAMPTZ DEFAULT now()
    );
    COMMENT ON TABLE public.app_settings IS 'Stores global configuration settings for DozerAI and App Suite.';

    CREATE TRIGGER set_timestamp_app_settings
    BEFORE UPDATE ON public.app_settings
    FOR EACH ROW
    EXECUTE PROCEDURE public.trigger_set_timestamp();
    """

    SQL_002_USERS_ROLES_PERMISSIONS = """
    CREATE TABLE IF NOT EXISTS public.roles (
        id SERIAL PRIMARY KEY,
        role_name TEXT UNIQUE NOT NULL,
        description TEXT,
        created_at TIMESTAMPTZ DEFAULT now(),
        updated_at TIMESTAMPTZ DEFAULT now()
    );
    COMMENT ON TABLE public.roles IS 'Defines different job roles within Dozer''s Business.';

    CREATE TABLE IF NOT EXISTS public.users (
        id UUID PRIMARY KEY REFERENCES auth.users(id) ON DELETE CASCADE,
        full_name TEXT,
        employee_id TEXT UNIQUE,
        job_title TEXT,
        profile_picture_url TEXT,
        created_at TIMESTAMPTZ DEFAULT now(),
        updated_at TIMESTAMPTZ DEFAULT now()
    );
    COMMENT ON TABLE public.users IS 'Stores application-specific profile information for users.';

    CREATE TABLE IF NOT EXISTS public.user_roles (
        user_id UUID NOT NULL REFERENCES public.users(id) ON DELETE CASCADE,
        role_id INTEGER NOT NULL REFERENCES public.roles(id) ON DELETE CASCADE,
        assigned_at TIMESTAMPTZ DEFAULT now(),
        PRIMARY KEY (user_id, role_id)
    );
    COMMENT ON TABLE public.user_roles IS 'Junction table mapping users to roles.';

    CREATE TABLE IF NOT EXISTS public.permissions (
        id SERIAL PRIMARY KEY,
        permission_name TEXT UNIQUE NOT NULL,
        description TEXT,
        created_at TIMESTAMPTZ DEFAULT now()
    );
    COMMENT ON TABLE public.permissions IS 'Defines specific granular permissions.';

    CREATE TABLE IF NOT EXISTS public.role_permissions (
        role_id INTEGER NOT NULL REFERENCES public.roles(id) ON DELETE CASCADE,
        permission_id INTEGER NOT NULL REFERENCES public.permissions(id) ON DELETE CASCADE,
        assigned_at TIMESTAMPTZ DEFAULT now(),
        PRIMARY KEY (role_id, permission_id)
    );
    COMMENT ON TABLE public.role_permissions IS 'Junction table mapping roles to permissions.';

    CREATE TRIGGER set_timestamp_roles
    BEFORE UPDATE ON public.roles
    FOR EACH ROW
    EXECUTE PROCEDURE public.trigger_set_timestamp();

    CREATE TRIGGER set_timestamp_users
    BEFORE UPDATE ON public.users
    FOR EACH ROW
    EXECUTE PROCEDURE public.trigger_set_timestamp();

    INSERT INTO public.roles (role_name, description) VALUES
        ('CEO', 'Chief Executive Officer, full system access.'),
        ('Manager', 'General management responsibilities, department-specific access.'),
        ('Employee_BarkRanger', 'Bark Ranger specific access for dog park operations.'),
        ('Employee_Chef', 'Chef/Kitchen Staff specific access for culinary operations.'),
        ('Employee_Server', 'Server/Bartender specific access for F&B service.'),
        ('System_Admin_DozerAI', 'Administrative role for DozerAI system management.'),
        ('PackLeaderAgent', 'System Role: AI Department Lead Sub-Agent.'),
        ('PackMemberAgent', 'System Role: AI Employee Assistant.'),
        ('Unassigned', 'Default role for new users until properly assigned.')
    ON CONFLICT (role_name) DO NOTHING;

    INSERT INTO public.permissions (permission_name, description) VALUES
        ('view_all_financials', 'Can view all financial reports and data.'),
        ('manage_all_schedules', 'Can create, edit, and delete all employee schedules.'),
        ('view_own_schedule', 'Can view own assigned schedule.'),
        ('request_time_off', 'Can submit time off requests.'),
        ('approve_time_off_dept', 'Can approve time off requests for their department.'),
        ('manage_inventory_all', 'Can manage all inventory items.'),
        ('access_kennel_full_read', 'Read access to all non-sensitive Kennel documents.'),
        ('manage_users_roles', 'Can assign roles and manage user profiles.'),
        ('post_global_announcements', 'Can send messages to all-employee channels.'),
        ('manage_all_tasks', 'Can create, assign, and manage all tasks across projects.'),
        ('view_own_tasks', 'Can view tasks assigned to self.'),
        ('sign_off_own_tasks', 'Can mark own tasks as completed and sign off.'),
        ('approve_task_signoffs', 'Can approve task signoffs from subordinates.'),
        ('manage_all_time_clock_entries', 'Can view and correct all time clock entries.'),
        ('view_own_time_clock_entries', 'Can view own time clock entries.'),
        ('submit_suggestions', 'Can submit to the suggestion box.'),
        ('manage_suggestions', 'Can review, categorize, and action suggestions.'),
        ('manage_all_meetings', 'Can manage all meetings and their artifacts.')
    ON CONFLICT (permission_name) DO NOTHING;
    """

    SQL_003_DOCUMENTS_CHUNKS_EMBEDDINGS = """
    CREATE EXTENSION IF NOT EXISTS vector;

    CREATE TABLE IF NOT EXISTS public.documents (
        id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
        source_uri TEXT UNIQUE NOT NULL,
        document_type TEXT NOT NULL,
        full_text_content TEXT,
        title TEXT,
        metadata JSONB,
        access_tags JSONB, 
        ingested_at TIMESTAMPTZ DEFAULT now(),
        last_updated_at TIMESTAMPTZ DEFAULT now(),
        content_hash TEXT
    );
    COMMENT ON TABLE public.documents IS 'Stores source documents for The Kennel.';
    CREATE INDEX IF NOT EXISTS idx_documents_type ON public.documents(document_type);
    CREATE INDEX IF NOT EXISTS idx_documents_source_uri ON public.documents(source_uri);
    CREATE INDEX IF NOT EXISTS idx_documents_access_tags ON public.documents USING GIN(access_tags);

    CREATE TABLE IF NOT EXISTS public.document_chunks (
        id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
        document_id UUID NOT NULL REFERENCES public.documents(id) ON DELETE CASCADE,
        chunk_text TEXT NOT NULL,
        chunk_sequence INTEGER NOT NULL,
        contextual_summary TEXT,
        metadata JSONB,
        created_at TIMESTAMPTZ DEFAULT now(),
        UNIQUE (document_id, chunk_sequence)
    );
    COMMENT ON TABLE public.document_chunks IS 'Stores processed text chunks from documents for RAG.';
    CREATE INDEX IF NOT EXISTS idx_chunks_document_id ON public.document_chunks(document_id);

    CREATE TABLE IF NOT EXISTS public.document_embeddings (
        id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
        chunk_id UUID NOT NULL REFERENCES public.document_chunks(id) ON DELETE CASCADE UNIQUE,
        embedding VECTOR(768) NOT NULL, 
        embedding_model_name TEXT NOT NULL,
        created_at TIMESTAMPTZ DEFAULT now()
    );
    COMMENT ON TABLE public.document_embeddings IS 'Stores vector embeddings for document chunks.';
    CREATE INDEX IF NOT EXISTS idx_embeddings_chunk_id ON public.document_embeddings(chunk_id);

    CREATE TRIGGER set_timestamp_documents
    BEFORE UPDATE ON public.documents
    FOR EACH ROW
    EXECUTE PROCEDURE public.trigger_set_timestamp();
    """

    SQL_004_APP_MESSENGER_TABLES = """
    CREATE TYPE public.channel_type_enum AS ENUM ('PUBLIC_CHANNEL', 'PRIVATE_GROUP', 'DIRECT_MESSAGE');
    CREATE TABLE IF NOT EXISTS public.chat_channels (
        id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
        channel_name TEXT, 
        description TEXT,
        channel_type public.channel_type_enum NOT NULL,
        created_by_user_id UUID REFERENCES public.users(id) ON DELETE SET NULL, 
        created_at TIMESTAMPTZ DEFAULT now(),
        updated_at TIMESTAMPTZ DEFAULT now(),
        is_archived BOOLEAN DEFAULT FALSE
    );
    COMMENT ON TABLE public.chat_channels IS 'Stores chat channels for App Suite messenger.';
    CREATE INDEX IF NOT EXISTS idx_chat_channels_type ON public.chat_channels(channel_type);

    CREATE TABLE IF NOT EXISTS public.channel_members (
        channel_id UUID NOT NULL REFERENCES public.chat_channels(id) ON DELETE CASCADE,
        user_id UUID NOT NULL REFERENCES public.users(id) ON DELETE CASCADE,
        joined_at TIMESTAMPTZ DEFAULT now(),
        last_read_at TIMESTAMPTZ, 
        notifications_enabled BOOLEAN DEFAULT TRUE,
        is_admin BOOLEAN DEFAULT FALSE,
        PRIMARY KEY (channel_id, user_id)
    );
    COMMENT ON TABLE public.channel_members IS 'Maps users to chat channels.';

    CREATE TABLE IF NOT EXISTS public.messages (
        id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
        channel_id UUID NOT NULL REFERENCES public.chat_channels(id) ON DELETE CASCADE,
        sender_user_id UUID REFERENCES public.users(id) ON DELETE SET NULL, 
        content_text TEXT NOT NULL,
        sent_at TIMESTAMPTZ DEFAULT now(),
        updated_at TIMESTAMPTZ, 
        metadata JSONB
    );
    COMMENT ON TABLE public.messages IS 'Stores individual chat messages.';
    CREATE INDEX IF NOT EXISTS idx_messages_channel_id_sent_at ON public.messages(channel_id, sent_at DESC);
    CREATE INDEX IF NOT EXISTS idx_messages_sender_user_id ON public.messages(sender_user_id);

    CREATE TRIGGER set_timestamp_chat_channels
    BEFORE UPDATE ON public.chat_channels
    FOR EACH ROW
    EXECUTE PROCEDURE public.trigger_set_timestamp();

    CREATE TRIGGER set_timestamp_messages_updated
    BEFORE UPDATE ON public.messages
    FOR EACH ROW
    EXECUTE PROCEDURE public.trigger_set_timestamp();

    ALTER TABLE public.chat_channels ENABLE ROW LEVEL SECURITY;
    ALTER TABLE public.channel_members ENABLE ROW LEVEL SECURITY;
    ALTER TABLE public.messages ENABLE ROW LEVEL SECURITY;

    CREATE POLICY "Users can access channels they are members of or public" ON public.chat_channels
        FOR ALL USING (
            EXISTS (
                SELECT 1 FROM public.channel_members cm
                WHERE cm.channel_id = chat_channels.id
                AND cm.user_id = auth.uid()
            ) OR chat_channels.channel_type = 'PUBLIC_CHANNEL'
        )
        WITH CHECK ( 
             EXISTS (
                SELECT 1 FROM public.channel_members cm
                WHERE cm.channel_id = chat_channels.id
                AND cm.user_id = auth.uid() AND (cm.is_admin = TRUE OR chat_channels.created_by_user_id = auth.uid())
            ) OR (chat_channels.channel_type = 'PUBLIC_CHANNEL' AND chat_channels.created_by_user_id = auth.uid()) 
        );
    
    CREATE POLICY "Users can manage own channel memberships or if admin" ON public.channel_members
        FOR ALL USING (user_id = auth.uid() OR EXISTS ( 
            SELECT 1 FROM public.chat_channels cc
            JOIN public.channel_members admin_cm ON cc.id = admin_cm.channel_id
            WHERE cc.id = channel_members.channel_id AND admin_cm.user_id = auth.uid() AND admin_cm.is_admin = TRUE
        ))
        WITH CHECK (user_id = auth.uid() OR EXISTS (
            SELECT 1 FROM public.chat_channels cc
            JOIN public.channel_members admin_cm ON cc.id = admin_cm.channel_id
            WHERE cc.id = channel_members.channel_id AND admin_cm.user_id = auth.uid() AND admin_cm.is_admin = TRUE
        ));

    CREATE POLICY "Users can access messages in their member channels" ON public.messages
        FOR ALL USING ( 
            EXISTS (
                SELECT 1 FROM public.channel_members cm
                WHERE cm.channel_id = messages.channel_id
                AND cm.user_id = auth.uid()
            )
        )
        WITH CHECK ( 
            (EXISTS (
                SELECT 1 FROM public.channel_members cm
                WHERE cm.channel_id = messages.channel_id
                AND cm.user_id = auth.uid()
            )) AND 
            (messages.sender_user_id = auth.uid() OR messages.sender_user_id IS NULL) 
        );
    """

    SQL_005_APP_TASKS_TABLES = """
    CREATE TABLE IF NOT EXISTS public.projects (
        id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
        project_name TEXT NOT NULL,
        description TEXT,
        owner_user_id UUID REFERENCES public.users(id) ON DELETE SET NULL,
        status TEXT DEFAULT 'Active', 
        created_at TIMESTAMPTZ DEFAULT now(),
        updated_at TIMESTAMPTZ DEFAULT now(),
        archived_at TIMESTAMPTZ
    );
    COMMENT ON TABLE public.projects IS 'Stores projects to logically group tasks.';

    CREATE TYPE public.task_status_enum AS ENUM ('TODO', 'IN_PROGRESS', 'REVIEW', 'DONE', 'BLOCKED', 'CANCELLED');
    CREATE TYPE public.task_priority_enum AS ENUM ('LOW', 'MEDIUM', 'HIGH', 'URGENT');

    CREATE TABLE IF NOT EXISTS public.tasks (
        id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
        project_id UUID REFERENCES public.projects(id) ON DELETE SET NULL, 
        title TEXT NOT NULL,
        description TEXT,
        status public.task_status_enum DEFAULT 'TODO',
        priority public.task_priority_enum DEFAULT 'MEDIUM',
        due_date DATE,
        assigned_to_user_id UUID REFERENCES public.users(id) ON DELETE SET NULL,
        created_by_user_id UUID REFERENCES public.users(id) ON DELETE SET NULL,
        created_at TIMESTAMPTZ DEFAULT now(),
        updated_at TIMESTAMPTZ DEFAULT now(),
        completed_at TIMESTAMPTZ,
        tags TEXT[] 
    );
    COMMENT ON TABLE public.tasks IS 'Stores individual tasks for the App Suite.';
    CREATE INDEX IF NOT EXISTS idx_tasks_project_id ON public.tasks(project_id);
    CREATE INDEX IF NOT EXISTS idx_tasks_assigned_to ON public.tasks(assigned_to_user_id);
    CREATE INDEX IF NOT EXISTS idx_tasks_status ON public.tasks(status);
    CREATE INDEX IF NOT EXISTS idx_tasks_tags ON public.tasks USING GIN(tags);

    CREATE TABLE IF NOT EXISTS public.task_dependencies (
        task_id UUID NOT NULL REFERENCES public.tasks(id) ON DELETE CASCADE,
        depends_on_task_id UUID NOT NULL REFERENCES public.tasks(id) ON DELETE CASCADE,
        created_at TIMESTAMPTZ DEFAULT now(),
        PRIMARY KEY (task_id, depends_on_task_id),
        CHECK (task_id <> depends_on_task_id) 
    );
    COMMENT ON TABLE public.task_dependencies IS 'Defines dependencies between tasks.';

    CREATE TABLE IF NOT EXISTS public.task_signoffs (
        id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
        task_id UUID NOT NULL REFERENCES public.tasks(id) ON DELETE CASCADE,
        signed_off_by_user_id UUID NOT NULL REFERENCES public.users(id) ON DELETE CASCADE,
        signed_off_at TIMESTAMPTZ DEFAULT now(),
        comments TEXT, 
        manager_approved_at TIMESTAMPTZ, 
        manager_approver_id UUID REFERENCES public.users(id) ON DELETE SET NULL
    );
    COMMENT ON TABLE public.task_signoffs IS 'Records employee task sign-offs.';
    CREATE INDEX IF NOT EXISTS idx_task_signoffs_task_id ON public.task_signoffs(task_id);

    CREATE TRIGGER set_timestamp_projects
    BEFORE UPDATE ON public.projects
    FOR EACH ROW
    EXECUTE PROCEDURE public.trigger_set_timestamp();

    CREATE TRIGGER set_timestamp_tasks
    BEFORE UPDATE ON public.tasks
    FOR EACH ROW
    EXECUTE PROCEDURE public.trigger_set_timestamp();
    
    ALTER TABLE public.projects ENABLE ROW LEVEL SECURITY;
    ALTER TABLE public.tasks ENABLE ROW LEVEL SECURITY;
    ALTER TABLE public.task_dependencies ENABLE ROW LEVEL SECURITY;
    ALTER TABLE public.task_signoffs ENABLE ROW LEVEL SECURITY;

    CREATE POLICY "Tasks RLS Policy for Users and Admins" ON public.tasks
        FOR ALL USING (
            auth.uid() = assigned_to_user_id OR
            auth.uid() = created_by_user_id OR
            EXISTS (
                SELECT 1 FROM public.user_roles ur
                JOIN public.role_permissions rp ON ur.role_id = rp.role_id
                JOIN public.permissions p ON rp.permission_id = p.id
                WHERE ur.user_id = auth.uid() AND p.permission_name IN ('manage_all_tasks', 'manage_project_tasks') -- Assuming 'manage_project_tasks' would also check project ownership/membership
            ) OR
            (project_id IS NOT NULL AND EXISTS (SELECT 1 FROM public.projects proj WHERE proj.id = tasks.project_id AND proj.owner_user_id = auth.uid()))
        )
        WITH CHECK (
            auth.uid() = created_by_user_id OR -- Creator can always modify
            auth.uid() = assigned_to_user_id OR -- Assignee can modify (e.g. status)
            EXISTS (
                SELECT 1 FROM public.user_roles ur
                JOIN public.role_permissions rp ON ur.role_id = rp.role_id
                JOIN public.permissions p ON rp.permission_id = p.id
                WHERE ur.user_id = auth.uid() AND p.permission_name IN ('manage_all_tasks', 'manage_project_tasks')
            ) OR
            (project_id IS NOT NULL AND EXISTS (SELECT 1 FROM public.projects proj WHERE proj.id = tasks.project_id AND proj.owner_user_id = auth.uid()))
        );
    -- Similar granular RLS policies for projects, task_dependencies, and task_signoffs would be defined based on user roles and specific permissions.
    -- For brevity, the above task policy is illustrative.
    """

    SQL_006_APP_TIME_CLOCK_TABLES = """
    CREATE TYPE public.clock_method_enum AS ENUM ('APP_MANUAL', 'RFID_TERMINAL', 'APP_AUTO_LOCATION', 'MANUAL_CORRECTION_BY_MANAGER');

    CREATE TABLE IF NOT EXISTS public.time_clock_entries (
        id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
        user_id UUID NOT NULL REFERENCES public.users(id) ON DELETE CASCADE,
        clock_in_at TIMESTAMPTZ NOT NULL DEFAULT now(),
        clock_out_at TIMESTAMPTZ,
        clock_in_method public.clock_method_enum NOT NULL,
        clock_out_method public.clock_method_enum,
        clock_in_location_data JSONB, 
        clock_out_location_data JSONB,
        rfid_tag_id_in TEXT, 
        rfid_tag_id_out TEXT, 
        notes TEXT, 
        corrected_by_user_id UUID REFERENCES public.users(id) ON DELETE SET NULL, 
        original_entry_id UUID REFERENCES public.time_clock_entries(id) ON DELETE SET NULL, 
        created_at TIMESTAMPTZ DEFAULT now(),
        updated_at TIMESTAMPTZ DEFAULT now(),
        duration_minutes INTEGER GENERATED ALWAYS AS (
            CASE
                WHEN clock_out_at IS NOT NULL AND clock_in_at IS NOT NULL THEN
                    CAST(EXTRACT(EPOCH FROM (clock_out_at - clock_in_at)) / 60 AS INTEGER)
                ELSE NULL
            END
        ) STORED
    );
    COMMENT ON TABLE public.time_clock_entries IS 'Stores employee clock-in/out events.';
    CREATE INDEX IF NOT EXISTS idx_time_clock_entries_user_id_clock_in_at ON public.time_clock_entries(user_id, clock_in_at DESC);

    CREATE TRIGGER set_timestamp_time_clock_entries
    BEFORE UPDATE ON public.time_clock_entries
    FOR EACH ROW
    EXECUTE PROCEDURE public.trigger_set_timestamp();

    ALTER TABLE public.time_clock_entries ENABLE ROW LEVEL SECURITY;

    CREATE POLICY "Users can manage their own time entries" ON public.time_clock_entries
        FOR ALL USING (user_id = auth.uid())
        WITH CHECK (user_id = auth.uid());

    CREATE POLICY "Managers with permission can manage all time entries" ON public.time_clock_entries
        FOR ALL USING ( 
            EXISTS (
                SELECT 1
                FROM public.user_roles ur
                JOIN public.role_permissions rp ON ur.role_id = rp.role_id
                JOIN public.permissions p ON rp.permission_id = p.id
                WHERE ur.user_id = auth.uid() AND p.permission_name = 'manage_all_time_clock_entries' 
            )
        )
        WITH CHECK ( 
             EXISTS (
                SELECT 1
                FROM public.user_roles ur
                JOIN public.role_permissions rp ON ur.role_id = rp.role_id
                JOIN public.permissions p ON rp.permission_id = p.id
                WHERE ur.user_id = auth.uid() AND p.permission_name = 'manage_all_time_clock_entries' 
            )
        );
    """

    SQL_007_APP_MEETING_NOTES_TABLES = """
    CREATE TABLE IF NOT EXISTS public.meetings (
        id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
        title TEXT NOT NULL,
        agenda TEXT,
        start_time TIMESTAMPTZ NOT NULL,
        end_time TIMESTAMPTZ,
        location_virtual_url TEXT, 
        location_physical TEXT, 
        created_by_user_id UUID NOT NULL REFERENCES public.users(id) ON DELETE CASCADE,
        created_at TIMESTAMPTZ DEFAULT now(),
        updated_at TIMESTAMPTZ DEFAULT now()
    );
    COMMENT ON TABLE public.meetings IS 'Stores meeting information for App Suite.';

    CREATE TABLE IF NOT EXISTS public.meeting_attendees (
        meeting_id UUID NOT NULL REFERENCES public.meetings(id) ON DELETE CASCADE,
        user_id UUID NOT NULL REFERENCES public.users(id) ON DELETE CASCADE,
        rsvp_status TEXT DEFAULT 'PENDING', 
        PRIMARY KEY (meeting_id, user_id)
    );
    COMMENT ON TABLE public.meeting_attendees IS 'Maps users to meetings.';

    CREATE TABLE IF NOT EXISTS public.meeting_notes (
        id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
        meeting_id UUID NOT NULL REFERENCES public.meetings(id) ON DELETE CASCADE,
        user_id_author UUID NOT NULL REFERENCES public.users(id) ON DELETE CASCADE,
        note_content TEXT NOT NULL, 
        is_summary BOOLEAN DEFAULT FALSE, 
        is_action_items BOOLEAN DEFAULT FALSE, 
        created_at TIMESTAMPTZ DEFAULT now(),
        updated_at TIMESTAMPTZ DEFAULT now()
    );
    COMMENT ON TABLE public.meeting_notes IS 'Stores meeting notes and AI summaries.';
    CREATE INDEX IF NOT EXISTS idx_meeting_notes_meeting_id ON public.meeting_notes(meeting_id);

    CREATE TYPE public.transcript_process_status_enum AS ENUM ('PENDING', 'PROCESSING', 'COMPLETED', 'FAILED');
    CREATE TABLE IF NOT EXISTS public.meeting_recordings (
        id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
        meeting_id UUID NOT NULL REFERENCES public.meetings(id) ON DELETE CASCADE,
        recording_file_path_supabase TEXT NOT NULL, 
        file_mime_type TEXT, 
        duration_seconds INTEGER,
        transcript_text TEXT, 
        transcript_status public.transcript_process_status_enum DEFAULT 'PENDING',
        uploaded_by_user_id UUID NOT NULL REFERENCES public.users(id) ON DELETE CASCADE,
        uploaded_at TIMESTAMPTZ DEFAULT now()
    );
    COMMENT ON TABLE public.meeting_recordings IS 'Stores meeting recording metadata and transcripts.';
    CREATE INDEX IF NOT EXISTS idx_meeting_recordings_meeting_id ON public.meeting_recordings(meeting_id);
    
    CREATE TRIGGER set_timestamp_meetings
    BEFORE UPDATE ON public.meetings
    FOR EACH ROW
    EXECUTE PROCEDURE public.trigger_set_timestamp();

    CREATE TRIGGER set_timestamp_meeting_notes
    BEFORE UPDATE ON public.meeting_notes
    FOR EACH ROW
    EXECUTE PROCEDURE public.trigger_set_timestamp();

    ALTER TABLE public.meetings ENABLE ROW LEVEL SECURITY;
    ALTER TABLE public.meeting_attendees ENABLE ROW LEVEL SECURITY;
    ALTER TABLE public.meeting_notes ENABLE ROW LEVEL SECURITY;
    ALTER TABLE public.meeting_recordings ENABLE ROW LEVEL SECURITY;

    CREATE POLICY "Users can manage meetings they created or are invited to, or if admin" ON public.meetings
        FOR ALL USING (
            created_by_user_id = auth.uid() OR
            EXISTS (SELECT 1 FROM public.meeting_attendees ma WHERE ma.meeting_id = meetings.id AND ma.user_id = auth.uid()) OR
            EXISTS (SELECT 1 FROM public.user_roles ur JOIN public.role_permissions rp ON ur.role_id = rp.role_id JOIN public.permissions p ON rp.permission_id = p.id WHERE ur.user_id = auth.uid() AND p.permission_name = 'manage_all_meetings')
        )
        WITH CHECK (
            created_by_user_id = auth.uid() OR
            EXISTS (SELECT 1 FROM public.user_roles ur JOIN public.role_permissions rp ON ur.role_id = rp.role_id JOIN public.permissions p ON rp.permission_id = p.id WHERE ur.user_id = auth.uid() AND p.permission_name = 'manage_all_meetings')
        );
    -- Similar RLS policies for attendees, notes, recordings based on meeting access / authorship / admin rights.
    """

    SQL_008_APP_SUGGESTIONS_TABLES = """
    CREATE TYPE public.suggestion_status_enum AS ENUM ('NEW', 'UNDER_REVIEW', 'PLANNED', 'IMPLEMENTED', 'REJECTED', 'DUPLICATE', 'ARCHIVED');

    CREATE TABLE IF NOT EXISTS public.suggestions (
        id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
        submitted_by_user_id UUID REFERENCES public.users(id) ON DELETE SET NULL, 
        is_anonymous BOOLEAN DEFAULT FALSE,
        title TEXT NOT NULL,
        description TEXT NOT NULL,
        category TEXT, 
        status public.suggestion_status_enum DEFAULT 'NEW',
        submitted_at TIMESTAMPTZ DEFAULT now(),
        updated_at TIMESTAMPTZ DEFAULT now(),
        manager_notes TEXT, 
        upvotes INTEGER DEFAULT 0,
        downvotes INTEGER DEFAULT 0 
    );
    COMMENT ON TABLE public.suggestions IS 'Stores employee suggestions for improvements.';
    CREATE INDEX IF NOT EXISTS idx_suggestions_status ON public.suggestions(status);
    CREATE INDEX IF NOT EXISTS idx_suggestions_category ON public.suggestions(category);

    CREATE TYPE public.vote_type_enum AS ENUM ('UPVOTE', 'DOWNVOTE');

    CREATE TABLE IF NOT EXISTS public.suggestion_votes (
        suggestion_id UUID NOT NULL REFERENCES public.suggestions(id) ON DELETE CASCADE,
        user_id UUID NOT NULL REFERENCES public.users(id) ON DELETE CASCADE,
        vote_type public.vote_type_enum NOT NULL,
        voted_at TIMESTAMPTZ DEFAULT now(),
        PRIMARY KEY (suggestion_id, user_id) 
    );
    COMMENT ON TABLE public.suggestion_votes IS 'Tracks user votes for suggestions.';

    CREATE TRIGGER set_timestamp_suggestions
    BEFORE UPDATE ON public.suggestions
    FOR EACH ROW
    EXECUTE PROCEDURE public.trigger_set_timestamp();

    ALTER TABLE public.suggestions ENABLE ROW LEVEL SECURITY;
    ALTER TABLE public.suggestion_votes ENABLE ROW LEVEL SECURITY;

    CREATE POLICY "Users can submit suggestions" ON public.suggestions
        FOR INSERT WITH CHECK (is_anonymous = TRUE OR submitted_by_user_id = auth.uid());

    CREATE POLICY "All authenticated users can view suggestions" ON public.suggestions
        FOR SELECT USING (auth.role() = 'authenticated'); 
        
    CREATE POLICY "Submitters can update own new suggestions" ON public.suggestions
        FOR UPDATE USING (submitted_by_user_id = auth.uid() AND status = 'NEW')
        WITH CHECK (submitted_by_user_id = auth.uid() AND status = 'NEW');

    CREATE POLICY "Managers with permission can update all suggestions" ON public.suggestions
        FOR UPDATE USING (
            EXISTS (
                SELECT 1
                FROM public.user_roles ur
                JOIN public.role_permissions rp ON ur.role_id = rp.role_id
                JOIN public.permissions p ON rp.permission_id = p.id
                WHERE ur.user_id = auth.uid() AND p.permission_name = 'manage_suggestions' 
            )
        );
    
    CREATE POLICY "Authenticated users can cast/change their vote" ON public.suggestion_votes
        FOR ALL USING (user_id = auth.uid())
        WITH CHECK (user_id = auth.uid());
    
    CREATE POLICY "Authenticated users can view all votes" ON public.suggestion_votes
        FOR SELECT USING (auth.role() = 'authenticated');
    """

    # --- Main script execution ---
    def execute_sql_block_direct(conn_params, sql_block: str, block_name: str):
        """Executes a block of SQL using a new psycopg connection for each block."""
        print(f"Attempting to execute schema block: {block_name}...")
        conn = None
        try:
            conn = psycopg.connect(**conn_params)
            with conn.cursor() as cur:
                cur.execute(sql_block)
            conn.commit() 
            print(f"SUCCESS: {block_name} executed successfully.")
            return True
        except psycopg.Error as e: # Catch psycopg specific errors
            print(f"DATABASE ERROR executing {block_name}: {e}")
            if conn:
                try:
                    conn.rollback()
                    print(f"Rolled back transaction for {block_name}.")
                except Exception as rb_e:
                    print(f"ERROR during rollback for {block_name}: {rb_e}")
            return False
        except Exception as e:
            print(f"UNEXPECTED ERROR executing {block_name}: {e}")
            return False
        finally:
            if conn:
                conn.close()

    def main():
        print("Starting Supabase schema initialization script via psycopg...")
        
        conn_params = {
            "host": DB_HOST,
            "port": DB_PORT,
            "dbname": DB_NAME,
            "user": DB_USER,
            "password": DB_PASSWORD,
            "sslmode": "require" # Supabase typically requires SSL
        }
        print(f"Attempting to connect to: postgresql://{DB_USER}:********@{DB_HOST}:{DB_PORT}/{DB_NAME}")

        all_sql_blocks_map = {
            "001_initial_core_tables": SQL_001_INITIAL_CORE_TABLES,
            "002_users_roles_permissions": SQL_002_USERS_ROLES_PERMISSIONS,
            "003_documents_chunks_embeddings": SQL_003_DOCUMENTS_CHUNKS_EMBEDDINGS,
            "004_app_messenger_tables": SQL_004_APP_MESSENGER_TABLES,
            "005_app_tasks_tables": SQL_005_APP_TASKS_TABLES,
            "006_app_time_clock_tables": SQL_006_APP_TIME_CLOCK_TABLES,
            "007_app_meeting_notes_tables": SQL_007_APP_MEETING_NOTES_TABLES,
            "008_app_suggestions_tables": SQL_008_APP_SUGGESTIONS_TABLES,
        }
        
        # Test connection first
        try:
            print("Testing database connection...")
            conn_test = psycopg.connect(**conn_params)
            conn_test.close()
            print("Database connection test successful.")
        except psycopg.OperationalError as e:
            print(f"CRITICAL DATABASE CONNECTION FAILED: {e}")
            print("Could not connect to the Supabase PostgreSQL database.")
            print("Please check ALL .env variables: SUPABASE_DB_USER, SUPABASE_DB_PASSWORD, SUPABASE_DB_HOST, SUPABASE_DB_PORT, SUPABASE_DB_NAME.")
            print(f"Ensure these match your Supabase project's direct database connection details.")
            print(f"Also ensure your Supabase project allows connections from your IP if IP restrictions are enabled, and that the DB password is for the 'postgres' user.")
            sys.exit(1)
        except Exception as e:
            print(f"Unexpected error during connection test: {e}")
            sys.exit(1)

        all_successful = True
        for block_name, sql_content in all_sql_blocks_map.items():
            if not execute_sql_block_direct(conn_params, sql_content, block_name):
                all_successful = False
                print(f"Halting script due to error in {block_name}.")
                break
            print(f"Successfully applied {block_name}. Waiting 1 second...")
            time.sleep(1) 

        if all_successful:
            print("\nAll SQL blocks executed successfully via Python script!")
            print("Schema initialization complete.")
            print("Please verify table creation in Supabase Studio as a final check.")
            print("\nIMPORTANT: If you haven't run it for SQL_003 already, you may need to manually run the HNSW index creation in Supabase SQL Editor after some data is inserted into 'document_embeddings':")
            print("CREATE INDEX CONCURRENTLY IF NOT EXISTS idx_hnsw_document_embeddings ON public.document_embeddings USING hnsw (embedding vector_l2_ops);")
        else:
            print("\nSchema initialization encountered errors. Please review logs above.")

    if __name__ == "__main__":
        main()
    ```

4.  **Log Start of Day 1 in `rules_check.log`:**
    *   After providing the above code and instructions to Anthony, I will mentally note (and later physically log once Anthony confirms his part is done) the `rules_check.log` entry.
5.  **Instruct Anthony for His Tasks (Revised for fully automated script):**
    *   "Anthony, I have provided:
        1.  The full content for `C:\Dozers\.gitignore`.
        2.  The content for `C:\Dozers\DozerAI_Code\requirements.txt`.
        3.  The full Python script `00_initialize_supabase_schema.py` (save to `C:\Dozers\DozerAI_Code\scripts\`). This script will now attempt to **directly execute all SQL** to set up your Supabase database schema.

        Please proceed with your Day 1 tasks:
        1.  **Confirm Pre-Day 1 Completion:** Supabase project live, `pgvector` enabled, Python/pip installed, source docs (Blueprint, Chat History) ready at specified paths.
        2.  **Create Directories:** If they don't exist: `C:\Dozers\DozerAI_Code\config\` and `C:\Dozers\DozerAI_Code\scripts\`.
        3.  **Populate `.env` File (CRITICAL):** Ensure `C:\Dozers\DozerAI_Code\config\.env` is fully populated with your actual credentials, **especially `SUPABASE_DB_USER`, `SUPABASE_DB_PASSWORD`, `SUPABASE_DB_HOST`, `SUPABASE_DB_PORT`, and `SUPABASE_DB_NAME` from your Supabase Database settings (Connection String URI).** Also include your Google API Key and Langfuse Keys.
        4.  **Create `.gitignore`:** Create `C:\Dozers\.gitignore` and paste the full content I've provided into it. Save.
        5.  **Create `requirements.txt`:** Create `C:\Dozers\DozerAI_Code\requirements.txt` and paste the content I've provided. Save.
        6.  **Create Schema Script:** Create `C:\Dozers\DozerAI_Code\scripts\00_initialize_supabase_schema.py` and paste the Python code I've just provided. Save.
        7.  **Set up Python Virtual Environment & Install Dependencies:**
            *   Open terminal, navigate to `cd C:\Dozers\DozerAI_Code\`
            *   `python -m venv venv`
            *   Activate: `.\venv\Scripts\Activate.ps1` (PowerShell) or `source venv/Scripts/activate` (Git Bash)
            *   `pip install -r requirements.txt` (Ensure `psycopg[binary]` installs correctly).
        8.  **Run the Automated Schema Initialization Script:**
            *   In the activated venv, from `C:\Dozers\DozerAI_Code\`, run: `python scripts/00_initialize_supabase_schema.py`
        9.  **Observe Output & Verify:** The script will print success or error messages for each of the 8 SQL blocks as it attempts to execute them. After it finishes, manually check your Supabase Table Editor to confirm tables are created.
        10. **Report to Me:** Notify me "Day 1 Python schema script executed. Status: [Success/Errors Encountered]. Tables checked in Supabase Studio." Provide any error messages if the script failed."

---
**Explanation of Day 1 Tasks (Revised):**
The process is now streamlined. Anthony's main technical lift is setting up the Python environment and running the `00_initialize_supabase_schema.py` script. This script now takes full responsibility for connecting to Supabase (using direct PostgreSQL connection details from `.env`) and executing all eight DDL SQL blocks. This greatly reduces the manual SQL work for Anthony. The SQL for the HNSW index on `document_embeddings` is commented out within the script for now and noted as something to run manually later or as a separate step, as it's best applied when there's some data, or concurrently.

**Troubleshooting (Revised):**
-   **Python Script Errors:**
    -   `ModuleNotFoundError` for `psycopg` or `dotenv`: Ensure `pip install -r requirements.txt` in an *active* virtual environment was successful.
    -   Database Connection Errors (from `psycopg.OperationalError`): This is the most likely failure point. **Triple-check every variable in `.env` related to `SUPABASE_DB_...`**. Ensure the host is correct (e.g., `db.<project-ref>.supabase.co`), the password is for the `postgres` user, and that your Supabase project isn't paused or restricting IP connections (Dashboard -> Project Settings -> Database -> Connection Pooling -> ensure your IP isn't blocked if Network Restrictions are on).
    -   SQL Execution Errors printed by the script: If a specific SQL block fails, the script will report it. This would indicate an issue with the SQL DDL itself (my responsibility to fix) or a permissions problem with the `postgres` user on Supabase (less likely for schema creation).
-   **No Tables in Supabase Studio after "Successful" Script:** Double-check script output for any silent errors. Ensure the connection string parameters in `.env` are for the *correct* Supabase project.

**Advice for Implementation:**
Anthony: The most critical part for you is getting the `.env` file 100% correct with the direct database connection string components from your Supabase dashboard. Run the script and observe its output closely.
DozerAI_Builder: The Python script now directly executes SQL. It includes print statements for clarity and basic error handling. The `psycopg` library is robust for this.

**(Other sections: Test, Backup Plans, Challenges, Out of the Box Ideas, Logs, Commits, Motivation remain conceptually the same as in my very first full Day 1 entry, but adapted for the success/failure of the *Python script's execution* rather than manual SQL steps by Anthony.)**

---


changes made to day one during implementation:

Summary of deviations from the original Day 1 Guide (for your records):
The primary deviation was the method of applying the schema. Instead of individual SQL files or one giant SQL block executed in a single transaction, we had to refactor the Python script (00_initialize_supabase_schema.py) to execute the schema in two distinct, committed parts.
Part 1: Created core tables and critical functions (like public.get_user_role).
Part 2: Created RLS policies (which depend on public.get_user_role) and the remaining tables/schema elements.
This was necessary to resolve a PostgreSQL error where RLS policies could not find the get_user_role function when the entire schema was executed in a single batch, likely due to the order of DDL parsing versus execution by the database engine.
Minor SQL syntax corrections were made iteratively (e.g., semicolon placement in trigger definitions within DO $$ blocks).
The Python script was enhanced with more detailed logging to a file (schema_init.log) to aid debugging when direct console output was unreliable.
The Python script's .env file path detection was made more robust.
Connection logic was updated to prefer the Supabase Pooler and fall back to direct connection, with checks for complete configuration details for each.
We can now consider the primary goal of Day 1 ("Supabase Project Setup & 'The Kennel' Initial Schema") complete.

End Day 1


**Day 2 - Kennel Ingestion MVP: "Dozer's Blueprint V8.0" & Our Sacred Scrolls (Dev Chat History) with Contextual Retrieval Pipeline (Stage 1: Parsing, Chunking, Context Gen)**

**Anthony's Vision (for this DozerAI/App Feature):**
"Alright, DozerAI_Builder, 'The Kennel' has its shelves built! Now, it's time to start stocking them with the most critical knowledge. We need to get 'Dozer's Blueprint V8.0' and all our development chat history into a state where DozerAI can actually *understand* it. This means breaking them down smartly and, as we discussed from Cole Medina's insights, adding that crucial 'Contextual Retrieval' summary to each piece so DozerAI isn't just getting snippets but *understands their place in the bigger picture*. For today, let's focus on getting the documents read, intelligently chunked (especially the Markdown Blueprint), and generating those contextual summaries for each chunk. Tomorrow, we'll embed them."

**Description:**
Day 2 focuses on the first stage of ingesting our two primary foundational documents – "Dozer's Blueprint V8.0" (business plan) and our `DozerAI_Dev_Chat_History.txt` – into "The Kennel." This involves:
1.  Creating a Python script (`01_ingest_and_contextualize_docs.py`) that can read these source documents.
2.  Implementing intelligent chunking strategies:
    *   For the Markdown-formatted "Dozer's Blueprint V8.0," we will use a header-aware chunking strategy to maintain semantic coherence.
    *   For the plain text `DozerAI_Dev_Chat_History.txt`, we will use a suitable text splitter (e.g., recursive character with overlap).
3.  For each generated chunk from both documents, the script will then use a cost-effective LLM (like Google's Gemini Flash or a smaller OpenAI/Anthropic model via OpenRouter if preferred) to generate a "contextual summary" as per the Anthropic Contextual Retrieval method. This summary situates the chunk within its parent document.
4.  The script will store the original document metadata, the generated chunks, and their corresponding contextual summaries in the `documents` and `document_chunks` tables in our Supabase database (created on Day 1). The actual vector embedding will happen on Day 3.

**Relevant Context (for DozerAI/App Suite):**
*Technical Analysis:* This stage is critical for populating "The Kennel" with high-quality, context-rich data for DozerAI's RAG/CAG system. The script will use Python libraries for file reading (`pathlib`), text processing, and Markdown parsing (e.g., `mistune` or `markdown-it-py` for robust Markdown parsing to identify headers for chunking). LLM calls for contextual summary generation will be made via their respective Python SDKs (e.g., `google-generativeai`), configured using API keys from the `.env` file. Results (document metadata, chunks, contextual summaries) will be inserted into Supabase using the `supabase-py` client, targeting the `documents` and `document_chunks` tables. Error handling and logging (to console and potentially a file log) will be included.
*Layman’s Terms:* We're taking our two most important books – the main Business Plan for "Dozer's" and the diary of how we're building DozerAI – and preparing them for DozerAI's brain. First, we'll chop these books into sensible paragraphs or sections ("chunks"). For the Business Plan, which has nice headings, we'll be smart and try to keep related ideas under one heading together in a chunk. Then, for *every single chunk*, we'll ask a quick, cheap AI helper to write a tiny note (a "contextual summary") explaining what that chunk is about and where it fits in the whole book. We'll then file away the original document info, all these chunks, and their little summary notes into "The Kennel" (our Supabase database). Tomorrow, we'll make the "smart index cards" (embeddings) for them.

**DozerAI_Builder's Thought Input:**
Implementing header-aware Markdown chunking and the Anthropic Contextual Retrieval method from the start is a best practice that will significantly enhance the quality of our RAG system. Using a cost-effective LLM for summary generation is key. Storing chunks and summaries now, before embedding, allows for easier review and potential reprocessing if needed. The `01_ingest_and_contextualize_docs.py` script will be a cornerstone of "The Kennel's" data pipeline.

**Anthony's Thought Input (for DozerAI/App Development):**
"This sounds like exactly what we need. I want DozerAI to *really get* the Blueprint and our conversations, not just spit back random sentences. If adding these 'contextual summaries' to each piece makes the AI smarter, then that's the way to go. I'm ready to see this script in action and start feeding Dozer's brain with the good stuff!"

**Additional Files, Documentation, Tools, Programs Needed (for DozerAI/App):**
-   `01_ingest_and_contextualize_docs.py`: (Python Script), (Parses, chunks, generates contextual summaries), (Core of Day 2), (To be created in `C:\Dozers\DozerAI_Code\scripts\`).
-   Python Libraries: (To be added to `C:\Dozers\DozerAI_Code\requirements.txt`)
    *   `google-generativeai` (for Gemini models for context generation)
    *   `mistune` or `markdown-it-py` (for Markdown parsing - let's choose `markdown-it-py` for its extensibility)
    *   `langchain-text-splitters` (for general text splitting, has good recursive character splitter and now Markdown header splitter)
    *   `tiktoken` (for token counting to manage LLM input for summaries, often an OpenAI SDK dependency but useful standalone)
-   `C:\Dozers\Docs\Business_Plan_Dozer_V8.md`: (Source Document)
-   `C:\Dozers\Docs\DozerAI_Dev_Chat_History.txt`: (Source Document)
-   Supabase Project: (Cloud Database), (Target for storing processed data), (Already set up).
-   `.env` file: (Located at `C:\Dozers\DozerAI_Code\config\.env`), (Must contain `GOOGLE_API_KEY` and Supabase credentials).

**Any Additional Updates Needed to the Project (DozerAI/App) Due to This Implementation?**
-   `C:\Dozers\DozerAI_Code\requirements.txt` will be updated with new Python libraries.
-   The `documents` and `document_chunks` tables in Supabase will be populated.

**DozerAI/App Project/File Structure Update Needed:** No new directories, just the new Python script and updated `requirements.txt`.

**Any Additional Updates Needed to the DozerAI Guide for Changes or Explanation?**
-   No, this entry details the plan.

**Any Removals from the DozerAI Guide Needed?**
-   None.

**Effect on DozerAI/App Project Timeline:**
-   No change; this is Day 2 as planned.

**Integration Plan (for DozerAI/App):**
-   **When:** Day 2 (Week 1) – Core data ingestion pipeline (Stage 1).
-   **Where:** Python script running locally, interacting with Supabase Cloud.
-   **Dependencies (Software):** Python environment from Day 1, activated.
-   **Setup Instructions (Summary):** Anthony updates `requirements.txt`, installs new packages. DozerAI_Builder provides the script. Anthony runs the script.

**Recommended Tools (for DozerAI/App):**
-   Python, VS Code (or preferred IDE).
-   Supabase Studio (to verify data insertion).
-   Terminal (PowerShell or Git Bash).

---
**Tasks for DozerAI_Builder (CursorAI):**

1.  **Update `requirements.txt` Content:**
    *   Provide the updated content for `C:\Dozers\DozerAI_Code\requirements.txt`, adding `google-generativeai`, `markdown-it-py`, `langchain-text-splitters`, and `tiktoken`.
2.  **Develop Python Script (`01_ingest_and_contextualize_docs.py`):**
    *   Create the complete Python script to be saved as `C:\Dozers\DozerAI_Code\scripts\01_ingest_and_contextualize_docs.py`.
    *   **Script Functionality:**
        *   Load Supabase and Google API credentials from `C:\Dozers\DozerAI_Code\config\.env`.
        *   Initialize Supabase client (`supabase-py`).
        *   Initialize Google Generative AI client (for Gemini Flash or a similar cost-effective model for summaries).
        *   Define file paths for `Business_Plan_Dozer_V8.md` and `DozerAI_Dev_Chat_History.txt`.
        *   **Function to process Markdown (`Business_Plan_Dozer_V8.md`):**
            *   Read the file.
            *   Use `langchain_text_splitters.MarkdownHeaderTextSplitter` to chunk based on headers (e.g., H1, H2, H3). Define appropriate headers to split by.
            *   For each chunk, generate a contextual summary using the chosen Google LLM. The prompt should include the full document text (or a very large surrounding window if the full doc exceeds LLM context for this *summary generation step*) and the current chunk, asking for a ~50-100 token summary of the chunk's role and context within the document.
            *   Store document metadata (source_uri, type="BUSINESS_PLAN", title, hash) in Supabase `documents` table (if not exists, based on hash). Get `document_id`.
            *   Store each chunk text and its `contextual_summary` in Supabase `document_chunks` table, linked to the `document_id`.
        *   **Function to process Plain Text (`DozerAI_Dev_Chat_History.txt`):**
            *   Read the file.
            *   Use `langchain_text_splitters.RecursiveCharacterTextSplitter` (e.g., chunk size 1000-1500, overlap 100-200).
            *   For each chunk, generate a contextual summary using the Google LLM (similar prompt, providing the full chat history or a large window as context).
            *   Store document metadata (source_uri, type="CHAT_HISTORY", title, hash) in Supabase `documents` table. Get `document_id`.
            *   Store each chunk text and its `contextual_summary` in Supabase `document_chunks` table.
        *   Include robust error handling for file operations, API calls, and database insertions.
        *   Print clear progress messages (e.g., "Processing Business_Plan_Dozer_V8.md...", "Chunking complete, X chunks created.", "Generating contextual summaries (this may take a while)...", "Storing chunks in Supabase...").
        *   At the end, print a summary: "Successfully processed X documents, creating Y chunks with contextual summaries, and stored them in Supabase."
3.  **Log Start in `rules_check.log`:**
    *   Mentally prepare log entry.
4.  **Instruct Anthony for His Tasks:**
    *   Provide clear instructions for Anthony to save the updated `requirements.txt`, save the new Python script, install new dependencies, and run the script.

---
**Code for `requirements.txt` (to be saved as `C:\Dozers\DozerAI_Code\requirements.txt` - *APPEND* these to existing):**
```text
# APPEND these to your existing requirements.txt from Day 1

# For Google Generative AI (Gemini models)
google-generativeai~=0.5.0 # Check for latest stable

# For Markdown parsing and text splitting
markdown-it-py~=3.0.0
langchain-text-splitters~=0.2.0 # Or latest compatible with langchain_core if used

# For token counting (often a dependency, but good to have explicitly)
tiktoken~=0.7.0
Use code with caution.
Markdown
Code for Python Script (C:\Dozers\DozerAI_Code\scripts\01_ingest_and_contextualize_docs.py):
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

# --- Configuration & Clients ---
# Load environment variables from .env file in the config directory
# Script is in DozerAI_Code/scripts/, .env is in DozerAI_Code/config/
BASE_DIR = Path(__file__).resolve().parent.parent # Resolves to DozerAI_Code
CONFIG_DIR = BASE_DIR / "config"
DOCS_DIR_HOST_OS = Path("C:/Dozers/Docs") # Path on Anthony's machine

load_dotenv(CONFIG_DIR / ".env")

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_SERVICE_ROLE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not all([SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY, GOOGLE_API_KEY]):
    print("ERROR: Supabase or Google API Key missing in .env. Please check C:\\Dozers\\DozerAI_Code\\config\\.env")
    sys.exit(1)

try:
    supabase_client: Client = create_client(SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY)
    print("Supabase client initialized successfully.")
except Exception as e:
    print(f"Error initializing Supabase client: {e}")
    sys.exit(1)

try:
    genai.configure(api_key=GOOGLE_API_KEY)
    # Using a cost-effective model for summary generation
    # Ensure you have access to this model or choose an alternative like "gemini-1.0-pro" if flash is not available
    context_gen_model = genai.GenerativeModel('gemini-1.5-flash-latest') 
    print(f"Google Generative AI client initialized with model: gemini-1.5-flash-latest")
except Exception as e:
    print(f"Error initializing Google Generative AI client: {e}")
    sys.exit(1)

# --- Helper Functions ---
def generate_content_hash(content: str) -> str:
    return hashlib.md5(content.encode('utf-8')).hexdigest()

def get_contextual_summary(full_document_text: str, chunk_text: str, doc_title: str) -> str:
    prompt = f"""
    You are an expert summarizer. Given the following full document titled '{doc_title}' and a specific chunk from it,
    provide a concise contextual summary (around 50-100 words) for ONLY the provided CHUNK.
    This summary should explain what the chunk is about and its role or significance within the larger document.
    This summary will be prepended to the chunk to improve search retrieval for a RAG system.
    Focus SOLELY on summarizing the CHUNK based on its relationship to the FULL DOCUMENT.

    FULL DOCUMENT (or a significant surrounding window):
    ---
    {full_document_text[:800000]} 
    ---
    (Note: Full document might be truncated if excessively long for this summary generation step)

    SPECIFIC CHUNK TO SUMMARIZE:
    ---
    {chunk_text}
    ---

    CONCISE CONTEXTUAL SUMMARY FOR THE CHUNK (50-100 words):
    """
    try:
        # print(f"DEBUG: Prompt sent to LLM for summary:\n{prompt[:500]}...\n") # Debug: careful with long prints
        print(f"DEBUG: Generating summary for chunk (length {len(chunk_text)}) from document '{doc_title}'...")
        response = context_gen_model.generate_content(prompt)
        # print(f"DEBUG: LLM Response object: {response}") # Debug response object
        summary = response.text.strip()
        # print(f"DEBUG: Generated summary: {summary}")
        return summary
    except Exception as e:
        print(f"ERROR generating contextual summary for chunk from '{doc_title}': {e}")
        # print(f"DEBUG: Failed prompt was:\n{prompt[:500]}...\n") # Debug: careful with long prints
        # print(f"DEBUG: Failed chunk was:\n{chunk_text[:500]}...\n")
        return f"Error generating summary: {e}"


def process_and_store_document(
    supabase: Client,
    file_path_host_os: Path, # Path on Anthony's machine
    source_uri: str, # Unique identifier for this document in the DB
    document_type: str,
    title: str,
    chunking_strategy: str = "recursive_char" # "markdown_header" or "recursive_char"
):
    print(f"\n--- Processing document: {title} ({source_uri}) ---")
    try:
        with open(file_path_host_os, "r", encoding="utf-8") as f:
            content = f.read()
        print(f"Read file: {file_path_host_os}, length: {len(content)} characters.")
    except FileNotFoundError:
        print(f"ERROR: File not found at {file_path_host_os}")
        return
    except Exception as e:
        print(f"ERROR reading file {file_path_host_os}: {e}")
        return

    content_hash = generate_content_hash(content)

    # Check if document with this hash already exists
    existing_doc_resp = supabase.table("documents").select("id, content_hash").eq("source_uri", source_uri).maybe_single().execute()
    
    doc_id = None
    if existing_doc_resp.data and existing_doc_resp.data.get("content_hash") == content_hash:
        print(f"Document '{title}' with identical content already ingested. Skipping chunking and summary generation.")
        doc_id = existing_doc_resp.data["id"]
        # Optionally, re-verify chunks exist or re-process if needed, for now we skip.
        # For a more robust system, one might still check if chunks exist for this doc_id.
        # For the MVP, if hash matches, assume it's fully processed to save LLM calls.
        print(f"Using existing document_id: {doc_id}")
        return # Skip further processing for this document
    elif existing_doc_resp.data: # Document exists but content changed, or no hash previously
        print(f"Document '{title}' exists but content has changed or hash mismatch. Re-processing.")
        doc_id = existing_doc_resp.data["id"]
        # Delete old chunks and embeddings associated with this document_id before re-ingesting
        print(f"Deleting old chunks for document_id: {doc_id}...")
        supabase.table("document_chunks").delete().eq("document_id", doc_id).execute() 
        # Embeddings will be deleted by cascade if foreign key is set up correctly.
        # Update the document entry with new hash and updated_at time
        doc_update_resp = supabase.table("documents").update({
            "full_text_content": content, # Storing full text for CAG and re-chunking flexibility
            "content_hash": content_hash,
            "last_updated_at": "now()"
        }).eq("id", doc_id).execute()
        if doc_update_resp.data:
            print(f"Updated existing document record for '{title}'.")
        else:
            print(f"Error updating document record for '{title}': {doc_update_resp.error}")
            return # Stop if document update failed
    else: # Document does not exist
        print(f"Document '{title}' not found in database. Inserting new record.")
        doc_data = {
            "source_uri": source_uri,
            "document_type": document_type,
            "title": title,
            "full_text_content": content, # Storing full text for CAG and re-chunking flexibility
            "metadata": {"file_path_original": str(file_path_host_os)},
            "content_hash": content_hash,
            # access_tags to be populated later based on roles/permissions
        }
        insert_doc_resp = supabase.table("documents").insert(doc_data).execute()
        if insert_doc_resp.data and len(insert_doc_resp.data) > 0:
            doc_id = insert_doc_resp.data["id"]
            print(f"Inserted new document record for '{title}', document_id: {doc_id}")
        else:
            print(f"ERROR inserting document '{title}': {insert_doc_resp.error}")
            return

    if not doc_id:
        print(f"ERROR: Could not obtain document_id for '{title}'. Skipping chunk processing.")
        return

    # Chunking
    chunks_with_text = []
    if chunking_strategy == "markdown_header":
        headers_to_split_on = [
            ("#", "H1"),
            ("##", "H2"),
            ("###", "H3"),
        ]
        markdown_splitter = MarkdownHeaderTextSplitter(headers_to_split_on=headers_to_split_on, strip_headers=False)
        docs_md = markdown_splitter.split_text(content)
        chunks_with_text = [doc.page_content for doc in docs_md if doc.page_content.strip()]
        print(f"Markdown chunking for '{title}' complete. {len(chunks_with_text)} chunks created.")
    elif chunking_strategy == "recursive_char":
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1200, # Adjusted for potentially better context per chunk
            chunk_overlap=150,
            length_function=len,
            is_separator_regex=False,
        )
        chunks_with_text = text_splitter.split_text(content)
        print(f"Recursive character chunking for '{title}' complete. {len(chunks_with_text)} chunks created.")
    else:
        print(f"Unknown chunking strategy: {chunking_strategy}")
        return

    if not chunks_with_text:
        print(f"No chunks generated for '{title}'. Check content or chunking strategy.")
        return

    print(f"Generating contextual summaries for {len(chunks_with_text)} chunks of '{title}' (this may take a while)...")
    
    # For very large documents, consider passing only relevant surrounding text instead of full_document_text
    # to manage context window for summary generation if the full document is >1M tokens.
    # For now, we pass up to the first 800k characters as a practical limit for the summary helper.
    context_for_summaries = content[:800000] 
    if len(content) > 800000:
        print(f"WARN: Full document content for '{title}' exceeds 800k chars, using truncated version for summary context.")

    chunk_data_to_insert = []
    for i, chunk_text in enumerate(chunks_with_text):
        print(f"  Processing chunk {i+1}/{len(chunks_with_text)} for '{title}'...")
        if not chunk_text.strip():
            print(f"    Skipping empty chunk {i+1}.")
            continue
        
        contextual_summary = get_contextual_summary(context_for_summaries, chunk_text, title)
        time.sleep(1) # Respect API rate limits for the summary generation model

        chunk_data_to_insert.append({
            "document_id": doc_id,
            "chunk_text": chunk_text,
            "chunk_sequence": i + 1,
            "contextual_summary": contextual_summary,
            "metadata": {"original_chunk_length": len(chunk_text)}
        })
        print(f"    Summary for chunk {i+1} generated.")

    if chunk_data_to_insert:
        print(f"Storing {len(chunk_data_to_insert)} chunks with summaries for '{title}' in Supabase...")
        try:
            insert_chunks_resp = supabase.table("document_chunks").insert(chunk_data_to_insert).execute()
            if insert_chunks_resp.data:
                print(f"Successfully stored {len(insert_chunks_resp.data)} chunks for '{title}'.")
            else:
                print(f"ERROR storing chunks for '{title}': {insert_chunks_resp.error}")
        except Exception as e_insert:
            print(f"EXCEPTION while inserting chunks for '{title}': {e_insert}")
    else:
        print(f"No valid chunks with summaries to store for '{title}'.")

    print(f"--- Finished processing document: {title} ---")

# --- Main Execution ---
def main():
    print("Starting Day 2: Document Ingestion & Contextualization Script...")

    # Define documents to process
    # Using Path objects for OS-independent path handling
    # These paths are on the HOST OS where the script is run (Anthony's machine)
    documents_to_process = [
        {
            "file_path_host_os": DOCS_DIR_HOST_OS / "Business_Plan_Dozer_V8.md",
            "source_uri": "dozers_blueprint_v8", # Unique DB identifier
            "document_type": "BUSINESS_PLAN",
            "title": "Dozer's Blueprint V8.0",
            "chunking_strategy": "markdown_header"
        },
        {
            "file_path_host_os": DOCS_DIR_HOST_OS / "DozerAI_Dev_Chat_History.txt",
            "source_uri": "dozerai_dev_chat_history_main", # Unique DB identifier
            "document_type": "CHAT_HISTORY",
            "title": "DozerAI Development Chat History (Main)",
            "chunking_strategy": "recursive_char"
        }
    ]

    for doc_info in documents_to_process:
        process_and_store_document(
            supabase_client,
            doc_info["file_path_host_os"],
            doc_info["source_uri"],
            doc_info["document_type"],
            doc_info["title"],
            doc_info["chunking_strategy"]
        )

    print("\nScript finished. Check Supabase 'documents' and 'document_chunks' tables.")

if __name__ == "__main__":
    main()
Use code with caution.
Python
Tasks for Anthony Pierce (CEO):
Update requirements.txt:
Open C:\Dozers\DozerAI_Code\requirements.txt.
APPEND the new libraries provided by DozerAI_Builder (for google-generativeai, markdown-it-py, langchain-text-splitters, tiktoken) to the existing content. Save the file.
Install New Dependencies:
Open your terminal (PowerShell or Git Bash).
Navigate to the application code root: cd C:\Dozers\DozerAI_Code\
Activate your Python virtual environment:
PowerShell: .\venv\Scripts\Activate.ps1
Git Bash / Cmd: source venv/Scripts/activate
Run: pip install -r requirements.txt
Confirm successful installation of the new packages.
Save the Ingestion Script:
Create the file C:\Dozers\DozerAI_Code\scripts\01_ingest_and_contextualize_docs.py.
Copy the complete Python script code provided above by DozerAI_Builder into this file. Save it.
Verify .env File:
Double-check C:\Dozers\DozerAI_Code\config\.env to ensure SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY, and GOOGLE_API_KEY are correctly populated with your actual keys. The script needs the Google API key for generating contextual summaries.
Run the Ingestion Script:
In your activated virtual environment, from C:\Dozers\DozerAI_Code\, run:
python scripts/01_ingest_and_contextualize_docs.py
Use code with caution.
Bash
Observe the output carefully. The script will print progress messages. It might take some time, especially for the contextual summary generation (due to LLM calls and rate limiting time.sleep(1)).
Note any errors.
Verify Data in Supabase:
After the script completes, go to your Supabase project dashboard.
Check the documents table: You should see two rows, one for "Dozer's Blueprint V8.0" and one for "DozerAI Development Chat History (Main)". Verify source_uri, document_type, title, and content_hash.
Check the document_chunks table: You should see multiple rows. Check a few to see if chunk_text looks reasonable and if contextual_summary contains a plausible summary.
Report to DozerAI_Builder:
"Day 2 Anthony tasks complete. Ingestion script ran. Status: [Success/Errors Encountered]. Verified data in Supabase documents and document_chunks tables. [Number] blueprint chunks and [Number] chat history chunks created."
Provide any error messages if the script failed or if data in Supabase looks incorrect.
Explanation of Day 2 Tasks:
This day is all about transforming our raw source documents (Business Plan and Chat History) into a structured, AI-ready format within "The Kennel."
Anthony's Tasks: Update Python packages, save the ingestion script provided by DozerAI_Builder, ensure the .env file is correct (especially the Google API key), run the script, and then verify the results in Supabase.
DozerAI_Builder's Tasks: Provide the updated requirements.txt and the complete Python script for ingestion. The script handles reading files, applying different chunking strategies (header-aware for Markdown, recursive for plain text), calling a Google LLM to generate a contextual summary for each chunk (the core of Anthropic's Contextual Retrieval), and then storing all this processed data into the documents and document_chunks tables in Supabase. It also includes a basic check to avoid re-processing identical documents based on a content hash.
Troubleshooting:
Python Script Errors:
ModuleNotFoundError: Ensure pip install -r requirements.txt in active venv was successful for all new packages.
API Key Errors (Google or Supabase): Verify .env file contents and paths. Ensure the Google API key allows for the Gemini model being called.
File Not Found: Ensure Business_Plan_Dozer_V8.md and DozerAI_Dev_Chat_History.txt are exactly at C:\Dozers\Docs\.
LLM Rate Limits for Summaries: The time.sleep(1) is a basic attempt to mitigate. If errors persist, we might need longer delays or batching for the summary generation.
Data Not Appearing in Supabase: Check script output for insertion errors. Verify Supabase credentials in .env. Check RLS policies on the tables (though for service_role key, RLS is usually bypassed by default for insertions, we ensured our policies from Day 1 are permissive for public schema where these tables live).
Advice for Implementation:
Anthony: The script may take a while to run due to the LLM calls for each chunk's summary. Let it run to completion. Monitor the console output for progress and any errors.
DozerAI_Builder: The contextual summary prompt is crucial. The quality of these summaries directly impacts RAG performance. The chunking strategies are also key. The script handles basic duplicate prevention via content hashing.
Advice for CursorAI (DozerAI_Builder):
Be mindful of the LLM context window when passing full_document_text to get_contextual_summary. The current script truncates it at 800k characters for the summary helper, which should be fine for Gemini 1.5 Flash's context capabilities for this specific task, but for extremely large single documents, a more sophisticated sliding window approach for context might be needed for the summary helper LLM. For Day 2, this approach is a good start.
Test:
Anthony: Primary test is visual inspection of the documents and document_chunks tables in Supabase Studio. Are there rows for both source documents? Do the chunks look sensible? Do the contextual_summary fields contain text?
DozerAI_Builder: Await Anthony's verification. Success means "The Kennel" is now populated with processable, context-enriched data.
Backup Plans:
If the script fails catastrophically, identify the failing part (file reading, chunking, summary gen, DB insert). We can debug the script. If only some chunks were inserted, the script's hash check (for full documents) might allow it to resume or re-process changed/missing parts, though the current script is more of a full re-process if the hash changes.
Challenges:
LLM API call costs/time for generating many contextual summaries. Robustness of Markdown header chunking for diverse Markdown structures. Ensuring Supabase insert operations are efficient for many chunks.
Out of the Box Ideas:
Batch insert chunks into Supabase for better performance (e.g., insert 50-100 chunks at a time).
Implement a more sophisticated check for existing chunks to allow resuming a failed ingestion process more gracefully.
Add more metadata during chunking (e.g., specific header text associated with a Markdown chunk).
Logs:
(DozerAI_Builder will log this after Anthony confirms successful completion of all his tasks for Day 2)
“Action: Starting Task for DozerAI/App: Day 2 - Kennel Ingestion MVP: Blueprint & Chat History with Contextual Retrieval (Stage 1), Rules reviewed: Yes, Guides (Creation/Dev) consulted: Yes, Env verified: Yes, Sequence verified: Yes, Timestamp: [YYYY-MM-DD HH:MM:SS]”
(Followed by)
“Milestone Completed (DozerAI/App): Day 2 - Kennel Ingestion MVP: Blueprint & Chat History with Contextual Retrieval (Stage 1). Next Task: Day 3 - Kennel Ingestion MVP: Embedding Enriched Chunks. Feeling: [Anthony's vibe]. Date: [YYYY-MM-DD]”
Commits:
(To be done by Anthony after successfully running the Python script, verifying data in Supabase, and all files (requirements.txt, 01_ingest_and_contextualize_docs.py) are saved in their correct locations)
# In C:\Dozers\
git add .
git commit -m "Day 2: Implement Stage 1 ingestion pipeline (parsing, chunking, contextual summaries) for Blueprint & Chat History. Update requirements."
git push origin main
Use code with caution.
Bash
Motivation:
"Dozer, old pal, today we're not just feeding you data, we're giving you understanding. Every piece of that Blueprint, every idea from our chats, is going to get its own little 'CliffsNotes' summary written by one of your AI cousins. This means when you need info, you won't just find a sentence, you'll know why that sentence matters. This is next-level brain food! It's gonna take a bit, but a smart doggo like you is worth the effort. Get ready to become an expert on... well, you and your amazing Bar'k & Grrr'ill!"


End Day 2
