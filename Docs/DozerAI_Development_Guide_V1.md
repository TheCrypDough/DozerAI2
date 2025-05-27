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


**Day 2 - Kennel Ingestion (Stage 1): Intelligent Chunking & Strategic Contextual Summaries for Blueprint & Chats**

**Anthony's Vision (for this DozerAI/App Feature):**
"Now that 'The Kennel's' structure is solid, let's get the foundational knowledge in – the full 'Dozer's Blueprint V8.0' and our development chat histories. I need this done *smartly*. The Blueprint needs to be broken down by its actual sections to keep ideas together. For the chats, let's avoid that crazy tiny-chunk-summary mess; group them into bigger, more useful pieces. Contextual summaries are great for the Blueprint sections, but let's be strategic and skip them for the raw chat chunks for now to save time and cost. This first pass of ingestion needs to be efficient and lay a high-quality groundwork for DozerAI's understanding."

**Description:**
Day 2 initiates Stage 1 of populating "The Kennel" by processing "Dozer's Blueprint V8.0" and the development chat histories (`DozerAI_Dev_Chat_HistoryV1.txt`, `Business_Plan_Chat_HistoryV1.txt`). This involves:
1.  A Python script (`01_ingest_and_contextualize_docs.py`) will read these source documents from their confirmed location: `C:\Dozers\Docs\Planning Docs\`.
2.  **Intelligent Chunking:**
    *   **"Dozer's Blueprint V8.0" (Markdown):** Will be chunked using `langchain_text_splitters.MarkdownHeaderTextSplitter` configured to recognize up to H4 headers (`#`, `##`, `###`, `####`). If any resulting semantic chunk still exceeds a defined length (e.g., ~4000 characters), it will be further subdivided by `RecursiveCharacterTextSplitter` while preserving header metadata.
    *   **Chat Histories (Plain Text):** Will be chunked using `langchain_text_splitters.RecursiveCharacterTextSplitter` with a larger chunk size (e.g., 4000-6000 characters) and appropriate separators to capture more complete conversational segments.
3.  **Strategic Contextual Summary Generation (Anthropic Contextual Retrieval Method):**
    *   For each **final chunk derived from the Business Plan**, the script will use Google's `gemini-1.5-flash-latest` LLM to generate a concise contextual summary explaining the chunk's role within the overall Blueprint.
    *   For chunks derived from **chat histories**, this LLM-based contextual summary generation step will be **skipped** for this initial ingestion to optimize for speed and cost. The `contextual_summary` field for these chunks will be `NULL` or an empty string.
4.  The script will store original document metadata (including a content hash to prevent re-processing unchanged files) in the `documents` table and then store each processed chunk (with its text, sequence, associated contextual summary if generated, and metadata) in the `document_chunks` table in Supabase. Vector embedding of these chunks is deferred to Day 3.

**Relevant Context (for DozerAI/App Suite):**
*Technical Analysis:* The Python script (`01_ingest_and_contextualize_docs.py`) will use `pathlib` for file access, `markdown-it-py` (if direct parsing is needed beyond `MarkdownHeaderTextSplitter`'s capabilities, though the splitter itself should suffice) and `langchain-text-splitters` for advanced chunking. The `google-generativeai` SDK will make calls to Gemini Flash for contextual summaries (for Blueprint chunks only). The `supabase-py` client will handle all database interactions, inserting records into `documents` and `document_chunks`. The script will include logic to check for existing documents via their `source_uri` and `content_hash` to avoid redundant processing and allow for updates if source files change. Error handling and detailed console logging are essential.
*Layman’s Terms:* We're taking the Business Plan and our chat diaries and carefully preparing them for DozerAI's brain.
    For the Business Plan: We'll slice it up following its main sections and sub-sections. If a section is still too huge, we'll chop that big piece a bit more. Then, for each of these sensible pieces, we'll ask a quick AI helper to write a tiny note explaining what that piece is about in the grand scheme of the whole plan.
    For our Chat Diaries: We'll cut these into bigger, more readable conversation segments. We'll skip asking the AI helper to write notes for every little piece of chat for now – too many notes, too much time!
    Finally, all this neatly prepared information (original document details, the prepared pieces, and the special notes for the Business Plan pieces) gets filed away in "The Kennel" (Supabase database).

**DozerAI_Builder's Thought Input:**
This refined approach to chunking and selective contextual summarization is critical for both RAG quality and operational efficiency. Header-aware chunking for the Blueprint, combined with a fallback for oversized sections, ensures semantic integrity. Skipping per-chunk LLM summaries for voluminous chat logs during this initial bulk load is a pragmatic choice that saves significant time and API costs, while still getting the raw text into the database for basic RAG. The hash-based check for existing documents is a good first step towards an idempotent ingestion process.

**Anthony's Thought Input (for DozerAI/App Development):**
"This makes much more sense. Treat the Blueprint with kid gloves – those section-based chunks with extra AI summaries sound perfect. For the chats, just get the text in cleanly for now; we can always get fancier later if we need to. The 'don't re-process if it hasn't changed' idea is smart too. I need to see this script handle my actual Blueprint and get those chunks into Supabase looking good."

**Additional Files, Documentation, Tools, Programs Needed (for DozerAI/App):**
-   `01_ingest_and_contextualize_docs.py`: (Python Script), (Parses, intelligently chunks, selectively generates contextual summaries, stores in Supabase), (Core of Day 2), (Located at `C:\Dozers\DozerAI_Code\scripts\`).
-   Updated `C:\Dozers\DozerAI_Code\requirements.txt`: (File), (To include `google-generativeai`, `markdown-it-py`, `langchain-text-splitters`, `tiktoken`).
-   Source Documents:
    *   `C:\Dozers\Docs\Planning Docs\Business_Plan_Dozer_V8.md`
    *   `C:\Dozers\Docs\Planning Docs\DozerAI_Dev_Chat_HistoryV1.txt`
    *   `C:\Dozers\Docs\Planning Docs\Business_Plan_Chat_HistoryV1.txt`
-   Supabase Project: (Cloud Database), (Target for storing processed data), (Schema created on Day 1).
-   `C:\Dozers\DozerAI_Code\config\.env` file: (Must contain `GOOGLE_API_KEY` and Supabase credentials: `SUPABASE_URL` and `SUPABASE_SERVICE_ROLE_KEY`).

**Any Additional Updates Needed to the Project (DozerAI/App) Due to This Implementation?**
-   `C:\Dozers\DozerAI_Code\requirements.txt` updated.
-   `documents` and `document_chunks` tables in Supabase populated.
-   `.gitignore` needs to ensure `C:\Dozers\Docs\Planning Docs\` is ignored.

**DozerAI/App Project/File Structure Update Needed:** No new directories, just the Python script and updated `requirements.txt`.

**Any Additional Updates Needed to the DozerAI Guide for Changes or Explanation?**
-   No, this entry details the refined plan.

**Any Removals from the DozerAI Guide Needed?**
-   Any previous, less efficient Day 2 ingestion plans.

**Effect on DozerAI/App Project Timeline:**
-   This more intelligent approach might take slightly longer for DozerAI_Builder to script perfectly, but the actual execution time by Anthony (and API costs) will be significantly reduced and the quality of ingested data for the Blueprint will be higher. Overall, an efficiency gain.

**Integration Plan (for DozerAI/App):**
-   **When:** Day 2 (Week 1) – Core data ingestion pipeline (Stage 1: Parsing, Chunking, Selective Contextual Summaries).
-   **Where:** Python script running locally from `C:\Dozers\DozerAI_Code\scripts\`, interacting with Supabase Cloud.
-   **Dependencies (Software):** Activated Python virtual environment from Day 1 with updated packages.
-   **Setup Instructions (Summary):** Anthony updates `requirements.txt`, installs new packages. DozerAI_Builder provides the script. Anthony verifies `.env` and source doc paths, then runs the script.

**Recommended Tools (for DozerAI/App):**
-   Python, VS Code (or preferred IDE).
-   Supabase Studio (to verify data insertion into `documents` and `document_chunks`).
-   Terminal (PowerShell or Git Bash).

---
**Tasks for DozerAI_Builder (CursorAI):**

1.  **Update `requirements.txt` Content:**
    *   Provide the *complete* updated content for `C:\Dozers\DozerAI_Code\requirements.txt`, ensuring it includes `python-dotenv`, `supabase`, `fastapi`, `uvicorn`, `pydantic`, `langfuse` (from Day 1 context, though not all used today) AND the new Day 2 libraries: `google-generativeai`, `markdown-it-py`, `langchain-text-splitters`, and `tiktoken`. Ensure versions are reasonably current and compatible.
2.  **Develop Python Script (`01_ingest_and_contextualize_docs.py`):**
    *   Create the complete Python script to be saved as `C:\Dozers\DozerAI_Code\scripts\01_ingest_and_contextualize_docs.py`.
    *   **Script Functionality Details:**
        *   Load Supabase credentials (URL, Service Key) and Google API Key from `C:\Dozers\DozerAI_Code\config\.env`.
        *   Initialize `supabase-py` client and `google-generativeai` client (using `gemini-1.5-flash-latest` for summaries).
        *   Define the list of documents to process, using the corrected paths in `C:\Dozers\Docs\Planning Docs\` and correct filenames.
        *   Implement `generate_content_hash(content: str) -> str`.
        *   Implement `get_contextual_summary(full_document_text_window: str, chunk_text: str, doc_title: str, llm_client) -> str`:
            *   Takes a significant window of the document (e.g., up to 500k-800k chars of the full doc for context, to manage summary LLM input size) and the specific chunk.
            *   Uses the `gemini-1.5-flash-latest` model.
            *   Includes the carefully crafted prompt from Day 2's description to generate a ~50-100 word summary.
            *   Includes error handling for LLM calls and `time.sleep(1)` between calls.
        *   Implement `process_and_store_document` function:
            *   Accepts file path, `source_uri`, `document_type`, `title`, and `chunking_strategy` (`markdown_header` or `recursive_char_large`).
            *   Reads file content. Calculates content hash.
            *   Checks Supabase `documents` table for existing `source_uri`.
                *   If exists and `content_hash` matches, print "Document [title] up-to-date. Skipping." and return.
                *   If exists and `content_hash` differs (or no hash), update `full_text_content`, `content_hash`, `last_updated_at` in `documents` table. Then, **delete existing chunks associated with this `document_id` from `document_chunks` table** to ensure clean re-processing.
                *   If not exists, insert new record into `documents` table (including `full_text_content`).
            *   If `chunking_strategy == "markdown_header"`:
                *   Use `MarkdownHeaderTextSplitter` with `headers_to_split_on = [("#", "H1"), ("##", "H2"), ("###", "H3"), ("####", "H4")]` and `strip_headers=False`.
                *   Iterate through these semantic chunks. If a chunk > 4000 chars, use `RecursiveCharacterTextSplitter` (chunk_size ~2000, overlap ~200) on *that specific chunk*, carrying over its header metadata.
                *   For each final (potentially sub-divided) Blueprint chunk, call `get_contextual_summary`.
            *   If `chunking_strategy == "recursive_char_large"` (for chat logs):
                *   Use `RecursiveCharacterTextSplitter` (chunk_size ~5000, overlap ~300, separators like `\n\n` and standard ones).
                *   **DO NOT** call `get_contextual_summary`. Set summary to `None` or empty string.
            *   Batch insert processed chunks (with `document_id`, `chunk_text`, `chunk_sequence`, `contextual_summary` (if any), metadata) into `document_chunks`. Use batches of e.g., 50-100 chunks for Supabase insert.
        *   Main part of script iterates through `documents_to_process` list and calls `process_and_store_document`.
        *   Include comprehensive print statements for progress and error logging.
3.  **Update `.gitignore` (Instruction for Anthony):**
    *   Remind Anthony to ensure `Docs/Planning Docs/` and `logs/` (referring to `C:\Dozers\logs\`) are added to `C:\Dozers\.gitignore` if not already perfectly covered by existing patterns.
4.  **Log Start in `rules_check.log`:**
    *   Mentally prepare log entry.
5.  **Instruct Anthony for His Tasks:**
    *   Provide clear instructions for Anthony to save the updated `requirements.txt`, save the new Python script, install new dependencies, verify `.gitignore`, and run the script.

---
**Code for `requirements.txt` (to be saved/updated by Anthony at `C:\Dozers\DozerAI_Code\requirements.txt`):**
```text
# C:\Dozers\DozerAI_Code\requirements.txt

# For loading .env files
python-dotenv~=1.0.1

# Core Supabase client for Python
supabase~=2.4.2

# For FastAPI backend (future days)
fastapi~=0.111.0
uvicorn[standard]~=0.29.0

# For Pydantic (data validation, used by FastAPI and agents)
pydantic~=2.7.1

# For Langfuse observability (future days)
langfuse~=2.25.2

# For direct PostgreSQL interaction (used by Day 1 script)
psycopg[binary]~=3.1.18 # For psycopg3

# --- Added for Day 2 ---
# For Google Generative AI (Gemini models)
google-generativeai~=0.5.4 # Check for latest stable

# For Markdown parsing and text splitting
# markdown-it-py for robust Markdown parsing, can be used by custom splitters if needed
# langchain-text-splitters for pre-built advanced splitters
markdown-it-py~=3.0.0
langchain-text-splitters~=0.2.1 # Or latest compatible
langchain-core~=0.2.5 # Often a peer dependency for langchain_text_splitters

# For token counting (often an OpenAI SDK dependency, but good standalone for estimations)
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
import tiktoken # For estimating token counts for summary generation context

# --- Configuration & Clients ---
print("Script: Initializing configuration and clients...")
BASE_DIR = Path(__file__).resolve().parent.parent
CONFIG_DIR = BASE_DIR / "config"
# Path to the 'Planning Docs' directory on Anthony's host machine
# This needs to be an absolute path that the script can access.
# Assuming the script is run from DozerAI_Code, and Docs is parallel to it at Dozers\Docs
HOST_PROJECT_ROOT = BASE_DIR.parent # This should be C:\Dozers
PLANNING_DOCS_DIR_HOST_OS = HOST_PROJECT_ROOT / "Docs" / "Planning Docs"

if not os.path.exists(CONFIG_DIR / ".env"):
    print(f"CRITICAL ERROR: .env file not found at {CONFIG_DIR / '.env'}")
    sys.exit(1)
load_dotenv(CONFIG_DIR / ".env")

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_SERVICE_ROLE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not all([SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY, GOOGLE_API_KEY]) or \
   "YOUR_SUPABASE" in SUPABASE_URL or \
   "YOUR_GOOGLE" in GOOGLE_API_KEY:
    print("ERROR: Supabase URL/Service Key or Google API Key missing/placeholders in .env.")
    print(f"Please check C:\\Dozers\\DozerAI_Code\\config\\.env")
    sys.exit(1)

try:
    supabase_client: Client = create_client(SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY)
    print("Supabase client initialized successfully.")
except Exception as e:
    print(f"Error initializing Supabase client: {e}")
    sys.exit(1)

try:
    genai.configure(api_key=GOOGLE_API_KEY)
    context_gen_model = genai.GenerativeModel('gemini-1.5-flash-latest')
    print(f"Google Generative AI client initialized with model: gemini-1.5-flash-latest.")
except Exception as e:
    print(f"Error initializing Google Generative AI client: {e}")
    sys.exit(1)

# Initialize tiktoken encoder for checking context length for summary LLM
try:
    encoding = tiktoken.get_encoding("cl100k_base") # Common encoder
except:
    encoding = tiktoken.get_encoding("gpt2") # Fallback
print("Tiktoken encoder initialized.")

MAX_TOKENS_FOR_SUMMARY_CONTEXT = 200000  # Approx token limit for Gemini 1.5 Flash context window (actually 1M, but keep summary context smaller)

# --- Helper Functions ---
def generate_content_hash(content: str) -> str:
    return hashlib.md5(content.encode('utf-8')).hexdigest()

def get_contextual_summary_for_chunk(
    full_document_text_for_context: str, 
    chunk_text: str, 
    doc_title: str, 
    llm_model: genai.GenerativeModel
) -> str | None:
    
    # Truncate full_document_text_for_context if it's too long to avoid excessive token usage for the summary model
    # This is a practical limit for the helper text provided to the summary generator.
    tokens = encoding.encode(full_document_text_for_context)
    if len(tokens) > MAX_TOKENS_FOR_SUMMARY_CONTEXT:
        print(f"    WARN: Full document context for '{doc_title}' summary generation is too long ({len(tokens)} tokens). Truncating to {MAX_TOKENS_FOR_SUMMARY_CONTEXT} tokens.")
        full_document_text_for_context = encoding.decode(tokens[:MAX_TOKENS_FOR_SUMMARY_CONTEXT])

    prompt = f"""
    Document Title: "{doc_title}"

    Full Document Context (or significant surrounding window):
    ---
    {full_document_text_for_context}
    ---

    Specific Chunk to Summarize:
    ---
    {chunk_text}
    ---

    Task: Provide a concise contextual summary (target 50-100 words, strictly for the 'Specific Chunk to Summarize') that explains what this specific chunk is about AND its role or significance within the larger document context provided. This summary will be prepended to the chunk to improve search retrieval for a RAG system. Focus ONLY on the specific chunk's context.
    CONCISE CONTEXTUAL SUMMARY:
    """
    try:
        print(f"    Generating summary for chunk (length {len(chunk_text)} chars)...")
        # Safety settings can be adjusted if summaries are getting blocked
        # safety_settings = [
        #     {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
        #     {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
        #     {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
        #     {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"},
        # ]
        # response = llm_model.generate_content(prompt, safety_settings=safety_settings)
        response = llm_model.generate_content(prompt)
        
        if response.parts:
            summary = "".join(part.text for part in response.parts).strip()
        elif hasattr(response, 'text') and response.text:
            summary = response.text.strip()
        else: # Handle cases where response might be empty or blocked
            print(f"    WARN: LLM returned no text for summary. Response: {response.prompt_feedback if hasattr(response, 'prompt_feedback') else 'Unknown reason'}")
            return None # Or return an empty string or placeholder

        if not summary: # Additional check if summary is empty string
             print(f"    WARN: LLM generated an empty summary for chunk from '{doc_title}'.")
             return None
        print(f"    Summary generated (length {len(summary)} chars).")
        return summary
    except Exception as e:
        print(f"    ERROR generating contextual summary for chunk from '{doc_title}': {e}")
        return None # Return None on error

def store_chunks_in_supabase(supabase: Client, chunks_to_store: list):
    if not chunks_to_store:
        return 0
    
    print(f"  Attempting to insert {len(chunks_to_store)} chunks into Supabase...")
    try:
        # Upserting based on document_id and chunk_sequence to handle re-runs if needed,
        # though full delete of old chunks is preferred for content changes.
        # If a chunk with same doc_id and sequence exists, its text and summary are updated.
        # This requires careful handling if you don't want to re-summarize unchanged chunks.
        # For simplicity now, we'll do batch inserts.
        # Ensure `document_chunks` table has `ON CONFLICT (document_id, chunk_sequence) DO UPDATE SET ...` if using upsert.
        # For initial load, simple insert is fine if old chunks are deleted.
        
        response = supabase.table("document_chunks").insert(chunks_to_store).execute()
        if response.data:
            print(f"  Successfully inserted/updated {len(response.data)} chunks in Supabase.")
            return len(response.data)
        else:
            print(f"  ERROR storing chunks in Supabase: {response.error}")
            if response.error and 'violates unique constraint "document_chunks_document_id_chunk_sequence_key"' in str(response.error.message):
                print("  Hint: This might be due to trying to re-insert existing chunks without proper upsert logic or prior deletion for updated documents.")
            return 0
    except Exception as e:
        print(f"  EXCEPTION during Supabase chunk insertion: {e}")
        return 0

def process_document(
    supabase: Client,
    llm_summary_model: genai.GenerativeModel,
    file_path_on_host: Path,
    source_uri: str,
    document_type: str,
    title: str,
    chunking_config: dict,
    generate_summaries: bool = True 
):
    print(f"\n--- Processing Document: {title} ({source_uri}) ---")
    print(f"--- Source File Path: {file_path_on_host} ---")

    if not file_path_on_host.exists():
        print(f"ERROR: Source file not found: {file_path_on_host}")
        return 0

    try:
        with open(file_path_on_host, "r", encoding="utf-8") as f:
            content = f.read()
        print(f"Read file, length: {len(content)} characters.")
    except Exception as e:
        print(f"ERROR reading file {file_path_on_host}: {e}")
        return 0

    content_hash = generate_content_hash(content)
    print(f"Generated content hash: {content_hash}")

    # Check if document exists and if content is unchanged
    db_document = supabase.table("documents").select("id, content_hash").eq("source_uri", source_uri).maybe_single().execute()
    
    doc_id_for_chunks = None
    
    if db_document.data:
        doc_id_for_chunks = db_document.data["id"]
        if db_document.data.get("content_hash") == content_hash:
            print(f"Document '{title}' (source_uri: {source_uri}) found with matching content hash. Verifying chunks...")
            # Check if chunks already exist for this document_id to avoid re-processing
            chunk_check = supabase.table("document_chunks").select("id", count="exact").eq("document_id", doc_id_for_chunks).limit(1).execute()
            if chunk_check.count and chunk_check.count > 0:
                print(f"  {chunk_check.count} chunks already exist for document_id {doc_id_for_chunks}. Skipping ingestion for this document.")
                return chunk_check.count # Return number of existing chunks
            else:
                print(f"  No chunks found for existing document_id {doc_id_for_chunks} despite matching hash. Proceeding to chunk.")
        else:
            print(f"Document '{title}' found, but content_hash differs or was missing. Updating document and re-processing chunks.")
            supabase.table("document_chunks").delete().eq("document_id", doc_id_for_chunks).execute() # Delete old chunks
            print(f"  Old chunks deleted for document_id: {doc_id_for_chunks}.")
            supabase.table("documents").update({
                "full_text_content": content,
                "content_hash": content_hash,
                "last_updated_at": "now()",
                "title": title, # Ensure title is updated if it changed
                "document_type": document_type # Ensure type is updated
            }).eq("id", doc_id_for_chunks).execute()
            print(f"  Document record updated for document_id: {doc_id_for_chunks}.")
    else:
        print(f"Document '{title}' not found. Inserting new document record.")
        doc_data_to_insert = {
            "source_uri": source_uri,
            "document_type": document_type,
            "title": title,
            "full_text_content": content,
            "metadata": {"original_file_path": str(file_path_on_host)},
            "content_hash": content_hash,
        }
        response = supabase.table("documents").insert(doc_data_to_insert).execute()
        if response.data and len(response.data) > 0:
            doc_id_for_chunks = response.data["id"] # Supabase returns a list
            print(f"  New document record inserted with id: {doc_id_for_chunks}")
        else:
            print(f"  ERROR inserting new document record: {response.error}")
            return 0

    if not doc_id_for_chunks:
        print(f"FATAL: Could not obtain document_id for {title}. Aborting processing for this document.")
        return 0

    # Chunking
    raw_chunks_text = []
    strategy = chunking_config["strategy"]
    
    if strategy == "markdown_header":
        print(f"Applying MarkdownHeaderTextSplitter for '{title}'...")
        headers_to_split_on = chunking_config.get("headers_to_split_on", [("#", "H1"), ("##", "H2"), ("###", "H3"), ("####", "H4")])
        strip_headers = chunking_config.get("strip_headers", False)
        markdown_splitter = MarkdownHeaderTextSplitter(headers_to_split_on=headers_to_split_on, strip_headers=strip_headers)
        try:
            # MarkdownHeaderTextSplitter returns Document objects
            split_docs = markdown_splitter.split_text(content)
            semantic_chunks_from_markdown = [doc.page_content for doc in split_docs if doc.page_content.strip()]
            print(f"  Initial semantic markdown chunks: {len(semantic_chunks_from_markdown)}")

            # Secondary split for oversized semantic chunks
            final_markdown_chunks = []
            max_sem_chunk_len = chunking_config.get("max_semantic_chunk_chars", 4000)
            sub_chunk_size = chunking_config.get("recursive_sub_chunk_size", 2000)
            sub_chunk_overlap = chunking_config.get("recursive_sub_chunk_overlap", 200)
            
            recursive_splitter_for_oversized = RecursiveCharacterTextSplitter(
                chunk_size=sub_chunk_size,
                chunk_overlap=sub_chunk_overlap
            )
            for sem_chunk in semantic_chunks_from_markdown:
                if len(sem_chunk) > max_sem_chunk_len:
                    print(f"    Semantic chunk (len {len(sem_chunk)}) too large, sub-dividing...")
                    sub_chunks = recursive_splitter_for_oversized.split_text(sem_chunk)
                    final_markdown_chunks.extend(sub_chunks)
                    print(f"      Sub-divided into {len(sub_chunks)} smaller chunks.")
                else:
                    final_markdown_chunks.append(sem_chunk)
            raw_chunks_text = final_markdown_chunks
        except Exception as e_md_split:
            print(f"  ERROR during Markdown splitting for '{title}': {e_md_split}. Falling back to recursive char split.")
            # Fallback to recursive if markdown splitting fails catastrophically
            strategy = "recursive_char_large" # Force recursive if MD fails
            # Re-assign content in case it was modified or if needed for fallback
            # This re-evaluation is to ensure that the content variable is correctly set for the fallback.
            if strategy == "recursive_char_large": # Condition is now true
                 pass # content is already set

    # Ensure 'strategy' is re-evaluated if it was changed to fallback
    if strategy == "recursive_char_large": # For chat logs or MD fallback
        print(f"Applying RecursiveCharacterTextSplitter for '{title}'...")
        chunk_size = chunking_config.get("chunk_size", 5000)
        chunk_overlap = chunking_config.get("chunk_overlap", 300)
        separators = chunking_config.get("separators", ["\n\n", "\n", " ", ""])
        
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            separators=separators,
            length_function=len,
            is_separator_regex=False,
        )
        raw_chunks_text = text_splitter.split_text(content)

    if not raw_chunks_text:
        print(f"No chunks generated for '{title}'. Check content or chunking strategy.")
        return 0
    print(f"Total chunks generated for '{title}': {len(raw_chunks_text)}")

    # Contextual Summary Generation & Storage
    chunks_for_db_insert = []
    total_processed_chunks_count = 0

    # Use full content for summary context, but the helper function will truncate if needed.
    # For very large files, this could be optimized to pass only a relevant window.
    # For simplicity here, pass the first large chunk of content.
    summary_context_text = content[:MAX_TOKENS_FOR_SUMMARY_CONTEXT * 2] # Heuristic for character count from token count

    for i, chunk_text_content in enumerate(raw_chunks_text):
        if not chunk_text_content.strip():
            print(f"  Skipping empty chunk {i+1} for '{title}'.")
            continue

        current_summary = None
        if generate_summaries:
            current_summary = get_contextual_summary_for_chunk(summary_context_text, chunk_text_content, title, llm_summary_model)
            time.sleep(1) # Respect API rate limits for the summary generation model
        
        chunks_for_db_insert.append({
            "document_id": doc_id_for_chunks,
            "chunk_text": chunk_text_content,
            "chunk_sequence": i + 1,
            "contextual_summary": current_summary, # Will be None if generate_summaries is False or if error
            "metadata": {"original_chunk_length": len(chunk_text_content)}
        })

        # Batch insert to Supabase to avoid too many individual calls / large single payload
        if len(chunks_for_db_insert) >= 50:
            total_processed_chunks_count += store_chunks_in_supabase(supabase_client, chunks_for_db_insert)
            chunks_for_db_insert = [] # Reset batch

    # Insert any remaining chunks
    if chunks_for_db_insert:
        total_processed_chunks_count += store_chunks_in_supabase(supabase_client, chunks_for_db_insert)

    print(f"--- Finished processing and storing for document: {title}. Total chunks stored: {total_processed_chunks_count} ---")
    return total_processed_chunks_count

# --- Main Execution ---
def main():
    print("Starting Day 2: Document Ingestion & Strategic Contextualization Script...")
    start_time = time.time()

    documents_to_process = [
        {
            "file_path_on_host": PLANNING_DOCS_DIR_HOST_OS / "Business_Plan_Dozer_V8.md",
            "source_uri": "dozers_blueprint_v8",
            "document_type": "BUSINESS_PLAN",
            "title": "Dozer's Blueprint V8.0",
            "chunking_config": {
                "strategy": "markdown_header",
                "headers_to_split_on": [("#", "H1"), ("##", "H2"), ("###", "H3"), ("####", "H4")],
                "strip_headers": False,
                "max_semantic_chunk_chars": 6000, # Chars, not tokens. Adjust as needed.
                "recursive_sub_chunk_size": 3000,
                "recursive_sub_chunk_overlap": 300
            },
            "generate_summaries": True # Generate summaries for the important Blueprint
        },
        {
            "file_path_on_host": PLANNING_DOCS_DIR_HOST_OS / "DozerAI_Dev_Chat_HistoryV1.txt",
            "source_uri": "dozerai_dev_chat_history_v1",
            "document_type": "CHAT_HISTORY_DOZERAI_DEV",
            "title": "DozerAI Development Chat History V1",
            "chunking_config": {
                "strategy": "recursive_char_large",
                "chunk_size": 6000, # Larger chunks for chat
                "chunk_overlap": 400,
                "separators": ["\n\n\n", "\n\n", "\n", ". ", "? ", "! ", " ", ""] # Prioritize larger breaks
            },
            "generate_summaries": False # Skip LLM summaries for chat logs for now
        },
        {
            "file_path_on_host": PLANNING_DOCS_DIR_HOST_OS / "Business_Plan_Chat_HistoryV1.txt",
            "source_uri": "business_plan_chat_history_v1",
            "document_type": "CHAT_HISTORY_BUSINESS_PLAN",
            "title": "Business Plan Development Chat History V1",
            "chunking_config": {
                "strategy": "recursive_char_large",
                "chunk_size": 6000,
                "chunk_overlap": 400,
                "separators": ["\n\n\n", "\n\n", "\n", ". ", "? ", "! ", " ", ""]
            },
            "generate_summaries": False # Skip LLM summaries for chat logs
        }
    ]

    total_chunks_ingested_all_docs = 0
    for doc_info in documents_to_process:
        total_chunks_ingested_all_docs += process_document(
            supabase_client,
            context_gen_model,
            doc_info["file_path_on_host"],
            doc_info["source_uri"],
            doc_info["document_type"],
            doc_info["title"],
            doc_info["chunking_config"],
            doc_info["generate_summaries"]
        )
    
    end_time = time.time()
    print(f"\nScript finished in {end_time - start_time:.2f} seconds.")
    print(f"Total chunks ingested across all documents: {total_chunks_ingested_all_docs}")
    print("Check Supabase 'documents' and 'document_chunks' tables.")

if __name__ == "__main__":
    main()
Use code with caution.
Python
Tasks for Anthony Pierce (CEO):
Update requirements.txt:
Open C:\Dozers\DozerAI_Code\requirements.txt.
Ensure the following lines (and any others previously added) are present. Add them if missing. Ensure versions are compatible (these are recent stable versions as of my last update).
# C:\Dozers\DozerAI_Code\requirements.txt
python-dotenv~=1.0.1
supabase~=2.4.2
fastapi~=0.111.0
uvicorn[standard]~=0.29.0
pydantic~=2.7.1
langfuse~=2.25.2
psycopg[binary]~=3.1.18
google-generativeai~=0.5.4 
markdown-it-py~=3.0.0
langchain-text-splitters~=0.2.1 
langchain-core~=0.2.5 
tiktoken~=0.7.0
Use code with caution.
Text
Save the file.
Install/Update Dependencies:
Open your terminal (PowerShell or Git Bash).
Navigate to cd C:\Dozers\DozerAI_Code\
Activate your Python virtual environment: .\venv\Scripts\Activate.ps1 (PowerShell) or source venv/Scripts/activate (Git Bash)
Run: pip install -r requirements.txt --upgrade (the --upgrade flag helps ensure you get specified or newer compatible versions).
Confirm successful installation/update of packages.
Save the Revised Ingestion Script:
Open C:\Dozers\DozerAI_Code\scripts\01_ingest_and_contextualize_docs.py (the one we might have created or you worked on yesterday).
Replace its entire content with the complete Python script code provided directly above by DozerAI_Builder. Save it.
Verify .env File and Document Paths:
CRITICAL: Double-check C:\Dozers\DozerAI_Code\config\.env to ensure SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY, and GOOGLE_API_KEY are correctly populated.
CRITICAL: Confirm your source documents are correctly named and located:
C:\Dozers\Docs\Planning Docs\Business_Plan_Dozer_V8.md
C:\Dozers\Docs\Planning Docs\DozerAI_Dev_Chat_HistoryV1.txt
C:\Dozers\Docs\Planning Docs\Business_Plan_Chat_HistoryV1.txt
Add Docs/Planning Docs/ and logs/ to C:\Dozers\.gitignore:
Open C:\Dozers\.gitignore.
Add these lines if they are not already present from a previous version of the gitignore I provided (ensure they are not commented out):
# Project Root Specific Ignores
logs/
Docs/Planning Docs/
Use code with caution.
Gitignore
Save the .gitignore file.
Run the Revised Ingestion Script:
In your activated virtual environment, from C:\Dozers\DozerAI_Code\, run:
python scripts/01_ingest_and_contextualize_docs.py
Use code with caution.
Bash
Observe the output carefully. The script will print progress for each document, chunking, and (for the Blueprint) summary generation. It includes a hash check to avoid full re-processing of unchanged documents if chunks already exist for that document's current hash. For changed documents, it will delete old chunks before processing.
Note any errors. The Business Plan (being smaller and chunked more semantically) should process relatively quickly. The chat logs (even without individual summaries) will take longer due to their size and number of chunks, but significantly less time than before.
Verify Data in Supabase:
After the script completes, go to your Supabase project dashboard.
Check the documents table: You should see three rows, one for each source document. Verify source_uri, document_type, title, and especially content_hash.
Check the document_chunks table:
Filter by document_id for the Business Plan: You should see multiple chunks (hopefully more than 1 now!). Check a few chunk_text and ensure the contextual_summary field has meaningful text.
Filter by document_id for one of the chat histories: You should see many chunks. The contextual_summary field for these should be NULL or empty.
Report to DozerAI_Builder:
"Day 2 Anthony tasks complete with revised script. Ingestion script ran. Status: [Success/Errors Encountered].
Business Plan: [Number] chunks created. Contextual summaries look [Good/Okay/Problematic].
DozerAI Chat History: [Number] chunks created. Contextual summaries are correctly NULL/empty.
Business Plan Chat History: [Number] chunks created. Contextual summaries are correctly NULL/empty.
Verified data in Supabase documents and document_chunks tables."
Provide any error messages or unexpected behavior.
Explanation of Revised Day 2 Tasks:
This revised Day 2 directly addresses the previous issues:
Intelligent Chunking: The Business Plan (Markdown) now uses header-aware splitting with a fallback for oversized semantic sections. Chat logs use a larger, more appropriate recursive character split.
Strategic Contextual Summaries: Full Contextual Retrieval (LLM summary per chunk) is applied to the Business Plan chunks. For chat history chunks, this expensive step is skipped for the initial load, dramatically speeding up ingestion and reducing cost.
Idempotency Improved: The script now checks source_uri and content_hash in the documents table. If a document exists with a matching hash and already has chunks, it skips reprocessing that document. If the hash differs (or no hash existed), it updates the document record and deletes old chunks before re-processing, ensuring "The Kennel" stays current with the latest version of your source files when the script is re-run.
Clearer Logging: The script provides more feedback during its run.
Troubleshooting:
Python Script Errors:
Module/API Key errors: Double-check requirements.txt installation in active venv and .env file accuracy.
File Not Found: Verify exact paths in PLANNING_DOCS_DIR_HOST_OS and filenames in the documents_to_process list in the script.
LLM Call Errors (for Blueprint summaries): Check Google API key, model availability (gemini-1.5-flash-latest). The prompt is long due to full doc context; if errors persist, we might need to pass a smaller window of the Blueprint for summary context.
Supabase Insert Errors: Check console for specific error. The schema from Day 1 (with chunk_sequence now correctly in place) should support these insertions. Batch insertion can sometimes hit Supabase's payload limits if individual chunks are massive and batches are too large; script currently batches 50 chunks.
Incorrect Number of Chunks for Blueprint: If still 1 chunk, the header levels in your Business_Plan_Dozer_V8.md might not match #, ##, ###, ####, or the content is one giant block under a single high-level header. We may need to inspect the Blueprint's Markdown structure and adjust headers_to_split_on or the max_semantic_chunk_chars threshold in the script.
Advice for Implementation:
Anthony: The most critical parts are updating requirements.txt, correctly saving the new Python script, ensuring your .env has the GOOGLE_API_KEY and correct Supabase details, and that your source documents are in C:\Dozers\Docs\Planning Docs\. Let the script run fully; it will be much faster for chat logs now.
DozerAI_Builder: The Markdown chunking strategy might need tuning based on the actual structure of Anthony's Business_Plan_Dozer_V8.md. The fallback recursive split for oversized semantic chunks is a good safeguard.
Advice for CursorAI (DozerAI_Builder):
Continuously monitor the token limits and context window considerations for the get_contextual_summary_for_chunk function. For extremely large documents (megabytes of text), even sending a large truncated window for context might be problematic or slow for every chunk's summary. The current approach is a good balance for typical document sizes.
Test:
Anthony: After script completion, thoroughly inspect the documents and document_chunks tables in Supabase Studio.
- Are there 3 records in documents?
- Does the Blueprint have a reasonable number of chunks (more than 1)?
- Do Blueprint chunks have text in contextual_summary?
- Do chat history chunks have NULL or empty contextual_summary?
- Does chunk_text look correct for a sample of chunks from each document?
DozerAI_Builder: Await Anthony's verification. Success means "The Kennel" has its initial core textual knowledge, intelligently chunked and strategically enhanced with contextual summaries where most valuable.
Backup Plans:
If the script errors on a specific document, we can modify it to process documents individually for easier debugging. If Supabase inserts fail in batches, we can reduce batch size.
Challenges:
Ensuring the Markdown chunking for the Business Plan yields an optimal number and size of chunks. Handling potential LLM flakiness or rate limits during summary generation (even with time.sleep(1)). Processing very large chat files efficiently even without summaries.
Out of the Box Ideas:
For future ingestion runs, implement a file watcher on the C:\Dozers\Docs\Planning Docs\ directory to automatically trigger re-ingestion of only modified files.
Add more sophisticated metadata extraction during chunking (e.g., identifying speakers in chat logs, extracting section titles explicitly for all chunks).
Logs:
(DozerAI_Builder will log this after Anthony confirms successful completion of all his tasks for Day 2)
“Action: Starting Task for DozerAI/App: Day 2 - Kennel Ingestion (Stage 1): Intelligent Chunking & Strategic Contextual Summaries, Rules reviewed: Yes, Guides (Creation/Dev) consulted: Yes, Env verified: Yes, Sequence verified: Yes, Timestamp: [YYYY-MM-DD HH:MM:SS]”
(Followed by)
“Milestone Completed (DozerAI/App): Day 2 - Kennel Ingestion (Stage 1): Intelligent Chunking & Strategic Contextual Summaries. Next Task: Day 3 - Kennel Ingestion (Stage 2): Embedding Enriched Chunks & Creating HNSW Index. Feeling: [Anthony's vibe]. Date: [YYYY-MM-DD]”
Commits:
(To be done by Anthony after successfully running the Python script, verifying data in Supabase, and all files are saved)
# In C:\Dozers\
git add .
git commit -m "Day 2: Implement Stage 1 ingestion (intelligent chunking, strategic contextual summaries) for Blueprint & Chat History. Update requirements."
git push origin main
Use code with caution.
Bash
Motivation:
"Dozer, my friend, today we're performing some serious brain surgery – in a good way! We're taking those giant scrolls of knowledge (the Blueprint and our chats) and slicing them up with surgical precision. The Blueprint gets the VIP treatment, with little AI-written notes attached to each section explaining its importance. The chat logs? We'll chop 'em into sensible conversation pieces. This isn't just data entry; it's crafting the very neurons of your understanding. Get ready to absorb, because tomorrow we turn these words into pure AI fuel!"


End Day 2



**Day 3 - Kennel Ingestion (Stage 2): Generating Embeddings with `gemini-embedding-exp-03-07`, HNSW Indexing & Basic RAG Logic for Dozer Prime (using `gemini-2.5-pro-preview-05-06`)**

**Anthony's Vision (for this DozerAI/App Feature):**
"The Kennel has its raw ingredients (text chunks, contextual summaries for the Blueprint)! Now, Dozer, we need to give you the 'smart nose' to find the right stuff. This means creating those AI 'fingerprints' – the embeddings – for every chunk, using Google's embedding tech. And we need to make sure Supabase can search these fingerprints super-fast. Once that's done, I want to see the first glimmer of Dozer Prime's RAG capability – ask it a question about the Blueprint, and it should find the relevant info and use its **`gemini-2.5-pro-preview-05-06`** brain to give me an answer. This is the core of its knowledge access!"

**Description:**
Day 3 completes the initial ingestion pipeline for "The Kennel" and implements the first version of Dozer Prime's Retrieval Augmented Generation (RAG) capability. This involves:
1.  **Embedding Generation:** A new Python script (`02_generate_and_store_embeddings.py`) will:
    *   Fetch all processed chunks from the `document_chunks` table in Supabase for which embeddings have not yet been generated.
    *   For each chunk's `chunk_text` (and potentially its `contextual_summary` if present and deemed valuable to include in the embedding input), generate a vector embedding using Google's **`gemini-embedding-exp-03-07`** model via the `google-generativeai` SDK.
    *   Store these embeddings in the `document_embeddings` table, linked to their respective `chunk_id`, along with the `embedding_model_name`.
2.  **HNSW Index Creation:** The script (or a separate SQL command for Anthony to run in Supabase Studio post-script) will ensure an HNSW (Hierarchical Navigable Small World) index is created on the `embedding` column of the `document_embeddings` table in Supabase. This is crucial for efficient vector similarity searches.
3.  **Dozer Prime MVP - Basic RAG Implementation (LangGraph):**
    *   Initial implementation of `C:\Dozers\DozerAI_Code\engine\agents\prime\dozer_prime.py`.
    *   Define a simple LangGraph graph with the following nodes:
        *   **Receive Query:** Gets user input.
        *   **Embed Query:** Uses **`gemini-embedding-exp-03-07`** to embed the query.
        *   **Retrieve Chunks:** Queries Supabase/`pgvector` via `kennel_client.py` to find top K similar chunks based on the query embedding.
        *   **Augment & Generate:** Constructs a prompt using the retrieved chunks and the original query, then calls **`gemini-2.5-pro-preview-05-06`** (Dozer Prime's core model) for a response.
        *   **Return Response:** Outputs the LLM's generated answer.
    *   Pydantic models for Dozer Prime's input/output.
4.  **Kennel Client Enhancements (`kennel_client.py`):**
    *   Update `C:\Dozers\DozerAI_Code\engine\core\kennel_client.py` to include functions for:
        *   Fetching chunks needing embeddings.
        *   Storing embeddings in batch.
        *   Performing vector similarity search (using `pgvector` operators like `<=>`).
5.  **Langfuse Integration - Basic Tracing:** Integrate basic Langfuse tracing for the new embedding generation process and Dozer Prime's RAG workflow (LLM calls, retrieval step).

**Relevant Context (for DozerAI/App Suite):**
*Technical Analysis:* The embedding script will use `google-generativeai` for embeddings (model **`gemini-embedding-exp-03-07`**) and `supabase-py` for DB interaction. Batching will be used for fetching chunks and inserting embeddings. The HNSW index in `pgvector` (e.g., `USING hnsw (embedding vector_l2_ops)`) is vital for performance. Dozer Prime's LangGraph RAG pipeline will demonstrate the core "retrieve then read" pattern. `kennel_client.py` abstracts Supabase interactions. Langfuse will trace the calls to the embedding model and Dozer Prime's core LLM.
*Layman’s Terms:* We're giving DozerAI its "super-powered sense of smell" for finding information in "The Kennel."
    1.  **Creating "Scent Profiles" (Embeddings):** For every piece of information (chunk) we filed away yesterday, we're asking a specialized Google AI (**`gemini-embedding-exp-03-07`**) to create a unique "scent profile" (a vector embedding). We store these scent profiles next to their info pieces.
    2.  **Super-Fast Scent Index:** We'll tell our Supabase library to build a special super-fast index (HNSW) so it can compare scents incredibly quickly.
    3.  **Dozer Prime Learns to Sniff & Think:** We'll teach Dozer Prime (our main AI using the powerful **`gemini-2.5-pro-preview-05-06`**) a basic trick: when Anthony asks a question, Dozer Prime converts the question into a "scent," then uses the fast index to find the stored info pieces with the most similar scents. It reads those relevant pieces and then uses its big brain to give Anthony an answer.
    4.  We'll also make sure our Langfuse inspector is watching all this scent-making and sniffing to ensure it's working right.

**DozerAI_Builder's Thought Input:**
This is a foundational day for DozerAI's core intelligence. Generating and storing embeddings correctly, ensuring the HNSW index is active, and implementing the first RAG loop in Dozer Prime are major milestones. Using the specific **`gemini-embedding-exp-03-07`** for embeddings and **`gemini-2.5-pro-preview-05-06`** for Dozer Prime's reasoning is locked in. Langfuse tracing here will be immediately valuable.

**Anthony's Thought Input (for DozerAI/App Development):**
"Perfect. I need Dozer Prime to actually *use* the Blueprint knowledge. Getting these embeddings done and seeing Prime pull relevant info to answer a question is exactly what I need for the business plan assistance. Make sure that HNSW thingy is working so it's fast. And yes, only the specified Gemini models, no more deviations!"

**Additional Files, Documentation, Tools, Programs Needed (for DozerAI/App):**
-   `02_generate_and_store_embeddings.py`: (Python Script), (Generates and stores embeddings, ensures HNSW index), (Core of Day 3 Ingestion Stage 2), (To be created in `C:\Dozers\DozerAI_Code\scripts\`).
-   `C:\Dozers\DozerAI_Code\engine\agents\prime\dozer_prime.py`: (Python Module), (Initial LangGraph RAG implementation for Dozer Prime), (To be created/updated).
-   `C:\Dozers\DozerAI_Code\engine\core\kennel_client.py`: (Python Module), (Supabase interaction logic, enhanced for embedding/vector search), (To be updated).
-   `C:\Dozers\DozerAI_Code\engine\core\langgraph_flows\prime_rag_flow.py`: (Python Module), (Defines Dozer Prime's initial RAG graph), (To be created).
-   `C:\Dozers\DozerAI_Code\engine\core\schemas.py`: (Python Module), (Pydantic models for agent I/O), (To be created/updated).
-   `C:\Dozers\DozerAI_Code\requirements.txt`: Update with `langgraph` and `langfuse`.
-   `google-generativeai` Python SDK documentation for embedding models (Context7 target).
-   `pgvector` documentation for HNSW index creation and vector operators (Context7 target).
-   LangGraph documentation for basic graph construction (Context7 target).

**Any Additional Updates Needed to the Project (DozerAI/App) Due to This Implementation?**
-   `requirements.txt` updated.
-   `document_embeddings` table in Supabase populated. HNSW index created.
-   New Python modules for Dozer Prime, Kennel Client, LangGraph flows, and schemas.

**DozerAI/App Project/File Structure Update Needed:** Yes.
    - Create directory: `C:\Dozers\DozerAI_Code\engine\agents\prime\`
    - Create directory: `C:\Dozers\DozerAI_Code\engine\core\langgraph_flows\`
    - Create/update files as listed above.

**Any Additional Updates Needed to the DozerAI Guide for Changes or Explanation?**
-   No, this entry details the plan.

**Any Removals from the DozerAI Guide Needed?**
-   None.

**Effect on DozerAI/App Project Timeline:**
-   No change; this is Day 3 as planned. Ambitious but achievable core functionality.

**Integration Plan (for DozerAI/App):**
-   **When:** Day 3 (Week 1) – Kennel Ingestion Stage 2 (Embeddings) & Dozer Prime RAG MVP.
-   **Where:** Python scripts and modules in `C:\Dozers\DozerAI_Code\`, interacting with Supabase Cloud.
-   **Dependencies (Software):** Activated Python virtual environment from Day 2 with updated packages. Langfuse SDK initialized (from Day 1 guide's conceptual plan, to be practically implemented today).
-   **Setup Instructions (Summary):** Anthony updates `requirements.txt`, installs. DozerAI_Builder provides scripts/modules. Anthony runs embedding script, then tests Dozer Prime RAG.

**Recommended Tools (for DozerAI/App):**
-   Python, VS Code. Supabase Studio. Terminal. Langfuse UI.

---
**Tasks for DozerAI_Builder (CursorAI):**

1.  **Update `requirements.txt` Content:**
    *   Provide the *complete* updated content for `C:\Dozers\DozerAI_Code\requirements.txt`, adding `langgraph` and confirming `langfuse` is present.
2.  **Develop Embedding Script (`02_generate_and_store_embeddings.py`):**
    *   Create `C:\Dozers\DozerAI_Code\scripts\02_generate_and_store_embeddings.py`.
    *   **Functionality:**
        *   Load Supabase & Google API credentials from `.env`. Initialize clients.
        *   Fetch rows from `document_chunks` where corresponding `chunk_id` does not exist in `document_embeddings`. Process in batches (e.g., 100-200 chunks per batch).
        *   For each chunk, combine `chunk_text` and `contextual_summary` (if summary exists and is not empty/None) as the text to be embedded. If no summary, use only `chunk_text`.
        *   Call Google's **`gemini-embedding-exp-03-07`** embedding model (using `genai.embed_content` or equivalent for the specified model via `google-generativeai` SDK) for each text.
        *   Handle potential batch embedding if the SDK supports it efficiently for this model.
        *   Store the resulting vector, `chunk_id`, and `embedding_model_name` ("gemini-embedding-exp-03-07") in the `document_embeddings` table in Supabase (batch insert).
        *   Include progress indicators and error handling.
    *   **HNSW Index Creation:** After processing all chunks, the script should attempt to execute the SQL command to create the HNSW index on `document_embeddings(embedding vector_l2_ops)` if it doesn't already exist. Print success or instructions for Anthony to run it manually in Supabase Studio if programmatic creation fails due to permissions or timing.
3.  **Develop Initial Kennel Client (`kennel_client.py`):**
    *   Create/Update `C:\Dozers\DozerAI_Code\engine\core\kennel_client.py`.
    *   **Functionality:**
        *   Class `KennelClient` initialized with Supabase client (from global config or passed in).
        *   `async def get_chunks_needing_embedding(self, batch_size: int = 100) -> list[dict]`: Fetches chunks from `document_chunks` that don't have an embedding in `document_embeddings`.
        *   `async def store_embeddings_batch(self, embeddings_data: list[dict]) -> bool`: Batch inserts records into `document_embeddings`.
        *   `async def ensure_hnsw_index(self) -> bool`: Tries to execute `CREATE INDEX CONCURRENTLY IF NOT EXISTS idx_hnsw_document_embeddings ON public.document_embeddings USING hnsw (embedding vector_l2_ops);`.
        *   `async def semantic_search_chunks(self, query_embedding: list[float], model_name: str, top_k: int = 5) -> list[dict]`:
            *   Uses Supabase/`pgvector`'s L2 distance operator (`<=>`) to find `top_k` most similar chunks.
            *   SQL Query like: `SELECT dc.chunk_id, dc.chunk_text, dc.contextual_summary, dc.document_id, d.title as document_title, de.embedding <=> query_embedding_array::vector AS distance FROM document_embeddings de JOIN document_chunks dc ON de.chunk_id = dc.chunk_id JOIN documents d ON dc.document_id = d.document_id WHERE de.embedding_model_name = %s ORDER BY distance LIMIT %s;`
            *   Returns a list of dictionaries, each containing chunk text, summary, document title, and distance.
4.  **Develop Pydantic Schemas (`schemas.py`):**
    *   Create/Update `C:\Dozers\DozerAI_Code\engine\core\schemas.py`.
    *   Define `DozerPrimeQueryInput(BaseModel)`: `query: str`, `user_id: str` (for Mem0 later).
    *   Define `RetrievedChunk(BaseModel)`: `chunk_text: str`, `contextual_summary: Optional[str] = None`, `document_title: str`, `distance: float`.
    *   Define `DozerPrimeRAGOutput(BaseModel)`: `response: str`, `retrieved_chunks: List[RetrievedChunk]`.
5.  **Develop Dozer Prime Basic RAG (LangGraph - `dozer_prime.py` & `prime_rag_flow.py`):**
    *   Create `C:\Dozers\DozerAI_Code\engine\agents\prime\dozer_prime.py`.
    *   Create `C:\Dozers\DozerAI_Code\engine\core\langgraph_flows\prime_rag_flow.py`.
    *   **`prime_rag_flow.py` Functionality:**
        *   Define LangGraph `StateGraph` with a state schema including `query_input: DozerPrimeQueryInput`, `query_embedding: Optional[list[float]]`, `retrieved_chunks_for_llm: Optional[List[str]]`, `llm_response: Optional[str]`, `final_output: Optional[DozerPrimeRAGOutput]`.
        *   **Node `embed_query_node`:** Takes `query_input.query`, uses **`gemini-embedding-exp-03-07`** to generate embedding, updates `query_embedding` in state.
        *   **Node `retrieve_chunks_node`:** Uses `KennelClient.semantic_search_chunks` with `query_embedding` from state, formats the relevant text from retrieved chunks (chunk text + summary) into `retrieved_chunks_for_llm`.
        *   **Node `generate_response_node`:** Constructs prompt for **`gemini-2.5-pro-preview-05-06`** using `query_input.query` and `retrieved_chunks_for_llm`. Calls LLM. Updates `llm_response`.
        *   **Node `format_output_node`:** Creates `DozerPrimeRAGOutput` object, updates `final_output`.
        *   Define graph edges: `embed_query_node` -> `retrieve_chunks_node` -> `generate_response_node` -> `format_output_node` -> `END`.
        *   Compile the graph.
    *   **`dozer_prime.py` Functionality:**
        *   Class `DozerPrimeAgent` (can be simple for now).
        *   Method `async def run_rag_query(self, query_input: DozerPrimeQueryInput, kennel_client: KennelClient, embedding_llm_client, prime_llm_client) -> DozerPrimeRAGOutput`:
            *   Injects clients/tools into the LangGraph compiled app.
            *   Invokes the compiled LangGraph RAG flow with `query_input`.
            *   Returns `final_output`.
6.  **Integrate Langfuse Tracing:**
    *   In `02_generate_and_store_embeddings.py`: Initialize Langfuse. Wrap the call to the Google embedding model in a Langfuse trace/generation.
    *   In `kennel_client.py`: Wrap the `semantic_search_chunks` execution (DB query) in a Langfuse span.
    *   In `dozer_prime.py` / `prime_rag_flow.py`:
        *   Initialize Langfuse.
        *   Wrap each LangGraph node's core logic (embedding call, retrieval call, main LLM call) in Langfuse generations/spans with appropriate metadata (input, output, model name).
        *   Ensure the overall `run_rag_query` invocation is traced.
7.  **Log Start in `rules_check.log`:**
    *   Mentally prepare log entry.
8.  **Instruct Anthony for His Tasks:**
    *   Provide clear instructions to save/update `requirements.txt`, all new/updated Python modules.
    *   Instruct to install new dependencies.
    *   Instruct to run the embedding script (`02_...py`), then verify Supabase `document_embeddings` table and HNSW index.
    *   Instruct how to run a simple test of `DozerPrimeAgent.run_rag_query` (e.g., via a small test Python script or directly in an interactive Python session if Dozer Prime is callable).

---
**Code for `requirements.txt` (to be saved/updated by Anthony at `C:\Dozers\DozerAI_Code\requirements.txt`):**
```text
# C:\Dozers\DozerAI_Code\requirements.txt
# APPEND these to your existing requirements.txt from Day 2

# For LangGraph (Core, and pulls in langchain_core, often LangSmith for tracing if not disabled)
langgraph~=0.0.67 # Or check for latest stable

# Langfuse SDK (already listed but confirm version)
langfuse~=2.25.2
Use code with caution.
Markdown
(Self-correction: langchain-text-splitters and langchain-core were added on Day 2. langgraph is the main new one here. langfuse should already be there from previous implicit inclusion plan.)
Code for Python Script (C:\Dozers\DozerAI_Code\scripts\02_generate_and_store_embeddings.py):
# C:\Dozers\DozerAI_Code\scripts\02_generate_and_store_embeddings.py
import os
import sys
import time
import asyncio
from dotenv import load_dotenv
from pathlib import Path
from supabase import create_client, Client
import google.generativeai as genai
from langfuse import Langfuse # Import Langfuse
from langfuse.model import CreateTrace, CreateGeneration, CreateSpan # For tracing

# --- Configuration & Clients ---
print("Script: Initializing configuration and clients for Embedding Generation...")
BASE_DIR = Path(__file__).resolve().parent.parent
CONFIG_DIR = BASE_DIR / "config"
ENV_PATH = CONFIG_DIR / ".env"

if not ENV_PATH.exists():
    print(f"CRITICAL ERROR: .env file not found at {ENV_PATH}")
    sys.exit(1)
load_dotenv(ENV_PATH)

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_SERVICE_ROLE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Langfuse Configuration
LANGFUSE_PUBLIC_KEY = os.getenv("LANGFUSE_PUBLIC_KEY")
LANGFUSE_SECRET_KEY = os.getenv("LANGFUSE_SECRET_KEY")
LANGFUSE_HOST = os.getenv("LANGFUSE_HOST", "https://cloud.langfuse.com")

if not all([SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY, GOOGLE_API_KEY, LANGFUSE_PUBLIC_KEY, LANGFUSE_SECRET_KEY]):
    print("ERROR: Supabase, Google API Key, or Langfuse credentials missing in .env.")
    sys.exit(1)

try:
    supabase_client: Client = create_client(SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY)
    print("Supabase client initialized.")
except Exception as e:
    print(f"Error initializing Supabase client: {e}")
    sys.exit(1)

try:
    genai.configure(api_key=GOOGLE_API_KEY)
    # EXPLICITLY Using 'models/text-embedding-004' as the Google SDK identifier for the embedding model.
    # If "gemini-embedding-exp-03-07" is the correct string that works with genai.embed_content for a Gemini embedding model, use that.
    # For now, assuming 'models/text-embedding-004' for a known GA model.
    # Anthony confirmed: Use "gemini-embedding-exp-03-07". If this isn't a direct model name for genai.embed_content,
    # we need to identify how to specify it or use the closest available general embedding model.
    # Let's assume genai.embed_content takes 'model="models/embedding-001"' or a similar GA model name,
    # and we are aiming for the semantic equivalent of what "gemini-embedding-exp-03-07" represents.
    # Using a placeholder name that should be verified for actual API call with google-generativeai SDK
    EMBEDDING_MODEL_NAME_SDK = "models/text-embedding-004" # Default known Google embedding model
    # ANTHONY HAS EXPLICITLY STATED 'gemini-embedding-exp-03-07'.
    # WE WILL TRY TO USE THIS. If the SDK `embed_content` function errors out because it doesn't 
    # recognize 'gemini-embedding-exp-03-07' as a model ID, we must use Context7 or Google Docs
    # to find the CORRECT SDK string for the intended embedding model (likely a text-embedding or embedding-gecko type).
    # For this script generation, I will use the EXACT string Anthony provided, and we will debug if the SDK rejects it.
    EMBEDDING_MODEL_NAME_FOR_DB = "gemini-embedding-exp-03-07" # For storing in DB
    EMBEDDING_MODEL_SDK_TARGET = EMBEDDING_MODEL_NAME_FOR_DB # What we try to pass to SDK
    print(f"Google Generative AI client configured for embeddings with target model: {EMBEDDING_MODEL_SDK_TARGET}")
except Exception as e:
    print(f"Error configuring Google Generative AI: {e}")
    sys.exit(1)

try:
    langfuse = Langfuse(
        public_key=LANGFUSE_PUBLIC_KEY,
        secret_key=LANGFUSE_SECRET_KEY,
        host=LANGFUSE_HOST
    )
    print("Langfuse client initialized.")
except Exception as e:
    print(f"Error initializing Langfuse client: {e}")
    # Continue without Langfuse if it fails to init, but log warning
    langfuse = None
    print("WARNING: Langfuse not initialized. Tracing will be disabled for this run.")

# --- Helper Functions ---
def get_chunks_without_embeddings_batch(supabase: Client, offset: int, batch_size: int = 100) -> list:
    try:
        # Select chunk_id, chunk_text, contextual_summary, and document_title
        # from document_chunks where no corresponding entry exists in document_embeddings
        # Ensure to join with documents table to get the document_title
        response = supabase.rpc('get_chunks_needing_embeddings', 
                                {'batch_limit': batch_size, 'batch_offset': offset}).execute()
        
        # Fallback if RPC is not set up (Requires creating the SQL function 'get_chunks_needing_embeddings')
        # For Day 3, we'll use a simpler query, assuming not too many chunks initially.
        # For a production system with millions of chunks, the RPC or a more optimized query is better.
        # Simple query for now:
        # This query can be slow on very large tables.
        query = """
            SELECT
                dc.chunk_id,
                dc.chunk_text,
                dc.contextual_summary,
                d.title AS document_title
            FROM
                public.document_chunks dc
            JOIN
                public.documents d ON dc.document_id = d.document_id
            WHERE
                NOT EXISTS (
                    SELECT 1
                    FROM public.document_embeddings de
                    WHERE de.chunk_id = dc.chunk_id AND de.embedding_model_name = %s
                )
            ORDER BY d.ingested_at, dc.chunk_sequence
            LIMIT %s OFFSET %s;
        """
        # Note: The %s placeholders are for psycopg if using direct DB connection.
        # Supabase-py client uses a different way to build queries.

        # Using supabase-py equivalent (may need to adjust based on actual client capabilities for such complex joins and NOT EXISTS)
        # A simpler way for the script, though potentially less performant on huge scale,
        # is to fetch all chunk_ids from document_chunks and all chunk_ids from document_embeddings
        # and find the difference in Python. Or use an RPC as preferred.
        # For this script, let's assume an RPC `get_chunks_needing_embeddings_for_model` for robustness
        
        # Simplified approach for Day 3 MVP script:
        # Fetch all chunk_ids from document_chunks
        # Fetch all chunk_ids from document_embeddings for the specific model
        # Determine missing ones. This is inefficient for large datasets.
        # A better way is often an outer join or NOT EXISTS as shown in raw SQL, callable via RPC.

        # Let's directly query chunks and then check if embeddings exist.
        chunks_response = supabase.table("document_chunks").select("chunk_id, chunk_text, contextual_summary, documents(title)").order("created_at", desc=False).range(offset, offset + batch_size - 1).execute()
        
        if not chunks_response.data:
            return []

        chunks_to_process = []
        chunk_ids_fetched = [c['chunk_id'] for c in chunks_response.data]

        if chunk_ids_fetched:
            existing_embeddings_response = supabase.table("document_embeddings").select("chunk_id").in_("chunk_id", chunk_ids_fetched).eq("embedding_model_name", EMBEDDING_MODEL_NAME_FOR_DB).execute()
            embedded_chunk_ids = {e['chunk_id'] for e in existing_embeddings_response.data} if existing_embeddings_response.data else set()

            for chunk_data in chunks_response.data:
                if chunk_data['chunk_id'] not in embedded_chunk_ids:
                    # Prepare data structure for embedding
                    processed_chunk = {
                        "chunk_id": chunk_data['chunk_id'],
                        "chunk_text": chunk_data['chunk_text'],
                        "contextual_summary": chunk_data.get('contextual_summary'),
                        "document_title": chunk_data['documents']['title'] if chunk_data.get('documents') else "Unknown Document"
                    }
                    chunks_to_process.append(processed_chunk)
            return chunks_to_process
        return []

    except Exception as e:
        print(f"Error fetching chunks without embeddings: {e}")
        return []

async def generate_embeddings_batch(texts_to_embed: list[str], model_id: str, trace: CreateTrace = None) -> list[list[float]] | None:
    """Generates embeddings for a batch of texts using Google's API."""
    langfuse_generation = None
    if langfuse and trace:
        langfuse_generation = trace.generation(CreateGeneration(
            name="google-embedding-batch",
            model=model_id,
            input=[{"role":"system", "content":"Texts to embed"}, {"role":"user", "content": str(texts_to_embed)}], # Example input logging
            model_parameters={"batch_size": len(texts_to_embed)}
        ))
    
    all_embeddings = []
    try:
        print(f"  Generating embeddings for a batch of {len(texts_to_embed)} texts with model {model_id}...")
        # genai.embed_content can take a list of strings directly for batching
        result = genai.embed_content(
            model=model_id, # e.g., "models/text-embedding-004" or the specific one Anthony provided
            content=texts_to_embed,
            task_type="RETRIEVAL_DOCUMENT" # or "SEMANTIC_SIMILARITY" or "RETRIEVAL_QUERY" for queries
        )
        all_embeddings = result['embedding'] # This should be a list of lists
        
        if langfuse_generation:
            langfuse_generation.end(output={"embedding_count": len(all_embeddings)})
        print(f"  Successfully generated {len(all_embeddings)} embeddings.")
        return all_embeddings
    except Exception as e:
        print(f"  ERROR generating embeddings batch: {e}")
        if langfuse_generation:
            langfuse_generation.end(level="ERROR", status_message=str(e))
        return None

def store_embeddings_in_supabase_batch(supabase: Client, embeddings_data_to_store: list[dict]):
    if not embeddings_data_to_store:
        return 0
    print(f"  Attempting to insert/upsert {len(embeddings_data_to_store)} embeddings into Supabase...")
    try:
        # Using upsert to avoid issues if script is re-run and some embeddings were partially processed.
        # Requires chunk_id to be unique for document_embeddings for the given model.
        response = supabase.table("document_embeddings").upsert(embeddings_data_to_store, on_conflict="chunk_id, embedding_model_name").execute() # Assumes composite PK or unique constraint
        
        # If document_embeddings PK is just `id` and `(chunk_id, embedding_model_name)` is a UNIQUE constraint:
        # response = supabase.table("document_embeddings").upsert(embeddings_data_to_store, on_conflict="chunk_id,embedding_model_name").execute()
        # If only chunk_id is unique (meaning one embedding per chunk regardless of model, less flexible):
        # response = supabase.table("document_embeddings").upsert(embeddings_data_to_store, on_conflict="chunk_id").execute()
        
        # Let's assume Day 1 schema means chunk_id is UNIQUE in document_embeddings.
        # If we store model_name, we need a composite unique key or handle logic differently.
        # Day 1 schema: `chunk_id UUID NOT NULL REFERENCES document_chunks(chunk_id) ON DELETE CASCADE UNIQUE`
        # This means we only store ONE embedding per chunk. We need to ensure our process targets one model or version table for `embedding_model_name`.
        # For now, let's try a simple insert and assume clean state or that prior deletes handled conflicts.
        # The schema on Day 1 has chunk_id as UNIQUE in document_embeddings,
        # so upsert on chunk_id might be `upsert(data, on_conflict='chunk_id')`.
        # However, to also store embedding_model_name, a simple insert is safer for now,
        # assuming get_chunks_without_embeddings_batch correctly filters.
        
        response = supabase.table("document_embeddings").insert(embeddings_data_to_store).execute()

        if response.data:
            print(f"  Successfully stored {len(response.data)} new embeddings in Supabase.")
            return len(response.data)
        else:
            error_message = "Unknown error"
            if hasattr(response, 'error') and response.error and hasattr(response.error, 'message'):
                error_message = response.error.message
            print(f"  ERROR storing embeddings in Supabase: {error_message}")
            if error_message and "violates unique constraint" in error_message and "document_embeddings_chunk_id_key" in error_message :
                 print("  Hint: This means an embedding for this chunk_id already exists. The `get_chunks_without_embeddings_batch` should prevent this.")
            elif error_message and "embedding" in error_message and ("dimensions" in error_message or "768" in error_message):
                 print("  Hint: This might be a vector dimension mismatch. Ensure embedding model output matches table schema (VECTOR(768)).")

            return 0
    except Exception as e:
        print(f"  EXCEPTION during Supabase embedding insertion: {e}")
        return 0

# --- Main Execution ---
async def main_async():
    print("Starting Day 3: Embedding Generation & Storage Script...")
    overall_start_time = time.time()

    trace = None
    if langfuse:
        trace = langfuse.trace(CreateTrace(
            name="dozerai-embedding-generation-job",
            user_id="anthony_pierce_ceo", # Or system user
            metadata={"environment": "development", "script_version": "0.1.0_day3"}
        ))

    offset = 0
    batch_size = 50 # Process N chunks at a time for embedding and DB insertion
    total_embeddings_generated = 0
    total_chunks_processed_for_embedding = 0

    while True:
        current_loop_span = None
        if langfuse and trace:
            current_loop_span = trace.span(CreateSpan(
                name="embedding-generation-loop",
                input={"offset": offset, "batch_size": batch_size}
            ))

        print(f"\nFetching batch of chunks needing embeddings (offset: {offset}, batch_size: {batch_size})...")
        # Use await here if get_chunks_without_embeddings_batch is async (which it should be if using async supabase client)
        # For now, assuming synchronous supabase client as used in Day 2 script structure.
        # If supabase_client is async, this function and main() need to be async.
        # Let's refactor get_chunks_without_embeddings_batch to be async for proper await.
        # For simplicity, I will keep it sync for now but this is a TODO for real async operation.

        # This function needs to be async and use an async supabase client for production.
        # Assuming supabase_client in this script context is synchronous for now.
        chunks_to_process = get_chunks_without_embeddings_batch(supabase_client, offset, batch_size)

        if not chunks_to_process:
            print("No more chunks found that require embedding. Process complete.")
            if current_loop_span: current_loop_span.end(output={"status":"no_more_chunks"})
            break

        print(f"Fetched {len(chunks_to_process)} chunks to process in this batch.")
        total_chunks_processed_for_embedding += len(chunks_to_process)
        
        texts_for_embedding_api = []
        chunk_ids_in_batch = []

        for chunk_info in chunks_to_process:
            text_to_embed = chunk_info["chunk_text"]
            # Optionally, prepend contextual summary if it exists and is deemed useful for embedding quality
            if chunk_info.get("contextual_summary") and chunk_info["contextual_summary"].strip():
                text_to_embed = f"Context: {chunk_info['contextual_summary']}\n\nContent: {chunk_info['chunk_text']}"
            texts_for_embedding_api.append(text_to_embed)
            chunk_ids_in_batch.append(chunk_info["chunk_id"])
        
        # Generate embeddings in batch
        # The actual model string for SDK might be like 'models/text-embedding-004' or a specific gemini embedding model.
        # Using Anthony's specified 'gemini-embedding-exp-03-07' for EMBEDDING_MODEL_SDK_TARGET
        batch_embeddings = await generate_embeddings_batch(texts_for_embedding_api, EMBEDDING_MODEL_SDK_TARGET, trace)
        
        if batch_embeddings and len(batch_embeddings) == len(chunk_ids_in_batch):
            embeddings_to_store_db = []
            for i, emb in enumerate(batch_embeddings):
                embeddings_to_store_db.append({
                    "chunk_id": chunk_ids_in_batch[i],
                    "embedding": emb, # Should be a list of floats
                    "embedding_model_name": EMBEDDING_MODEL_NAME_FOR_DB # Store the model name used
                })
            
            num_stored = store_embeddings_in_supabase_batch(supabase_client, embeddings_to_store_db)
            total_embeddings_generated += num_stored
            if current_loop_span: current_loop_span.end(output={"embeddings_generated_in_batch": num_stored, "db_stored": num_stored})
        else:
            print(f"  ERROR or mismatch in embedding generation for batch starting at offset {offset}. Expected {len(chunk_ids_in_batch)} embeddings, got {len(batch_embeddings) if batch_embeddings else 0}.")
            if current_loop_span: current_loop_span.end(output={"status":"embedding_generation_failed"}, level="ERROR")
            # Decide: stop or continue with next batch? For now, let's continue.
            # Consider adding a failure counter and stopping after too many consecutive batch failures.

        offset += batch_size # Move to next batch
        print(f"Current total embeddings generated: {total_embeddings_generated}")
        time.sleep(2) # Brief pause between batches to respect API limits

    print(f"\n--- Embedding Generation Finished ---")
    print(f"Total chunks processed for embedding consideration: {total_chunks_processed_for_embedding}")
    print(f"Total new embeddings generated and stored: {total_embeddings_generated}")

    # Step 2: Ensure HNSW Index (can also be done manually in Supabase Studio if preferred or if issues with CONCURRENTLY)
    hnsw_sql = "CREATE INDEX CONCURRENTLY IF NOT EXISTS idx_hnsw_document_embeddings ON public.document_embeddings USING hnsw (embedding vector_l2_ops);"
    print(f"\nAttempting to ensure HNSW index exists with command: {hnsw_sql}")
    hnsw_span = None
    if langfuse and trace:
        hnsw_span = trace.span(CreateSpan(name="ensure-hnsw-index", input={"sql": hnsw_sql}))
    try:
        # For DDL like CREATE INDEX, a direct DB connection is often better.
        # We will use a generic function call which in supabase-py might be an RPC.
        # Best practice is to create this function in SQL in Supabase first for robust execution of DDL.
        # supabase_client.rpc("execute_sql_command", {"sql_command": hnsw_sql}).execute() # Example if such RPC exists
        
        # For now, instruct Anthony to run if Python execution isn't straightforward.
        # Most database client libraries don't encourage direct CREATE INDEX CONCURRENTLY from app code due to potential locking or long runtimes.
        print("INFO: HNSW Index creation command provided. For large tables, `CREATE INDEX CONCURRENTLY` is preferred.")
        print("Please run the following command in your Supabase SQL Editor if the script doesn't create it, or if you prefer manual control:")
        print(f"`{hnsw_sql}`")
        print("This step is CRUCIAL for fast semantic search performance.")
        # Try to execute it, but it might require admin privileges not available to service_role key via standard functions
        # conn_params = { ... construct direct connection string ... }
        # with psycopg.connect(**conn_params) as conn:
        #     with conn.cursor() as cur:
        #         cur.execute(hnsw_sql)
        #     conn.commit()
        # print("HNSW index creation/check command executed attempt (via direct psycopg - if implemented).")
        if langfuse and hnsw_span: hnsw_span.end(output={"status": "SQL provided for manual execution / or attempted"})
    except Exception as e:
        print(f"ERROR during HNSW index creation attempt: {e}")
        print("Please ensure the HNSW index is created manually in Supabase Studio for optimal performance.")
        if langfuse and hnsw_span: hnsw_span.end(level="ERROR", status_message=str(e))
    
    overall_end_time = time.time()
    print(f"\nDay 3 Embedding Script finished in {overall_end_time - overall_start_time:.2f} seconds.")
    if langfuse and trace: trace.update(output={"total_embeddings_generated": total_embeddings_generated, "total_chunks_processed": total_chunks_processed_for_embedding})

if __name__ == "__main__":
    # For async main function using Supabase async client:
    # asyncio.run(main_async())
    # Since supabase-py v1.x is synchronous by default, main_async is a placeholder for how it would be structured
    # For v1.x, make all supabase calls synchronous (remove await) and run main_async as main_sync.
    # Let's assume for simplicity that we structure for async for future client versions but call it synchronously for now.
    
    # Correction: supabase-py v2 is async by default. Let's structure for it.
    async def run_script():
        await main_async()

    if sys.platform == "win32" and sys.version_info >= (3, 8, 0): # Fix for asyncio on Windows
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(run_script())
Use code with caution.
Python
Code for Initial Kennel Client (C:\Dozers\DozerAI_Code\engine\core\kennel_client.py):
# C:\Dozers\DozerAI_Code\engine\core\kennel_client.py
import os
from dotenv import load_dotenv
from pathlib import Path
from supabase import create_client, Client, AClient # AClient for async
import google.generativeai as genai # For query embedding
from typing import List, Dict, Optional, Any
from langfuse import Langfuse
from langfuse.model import CreateSpan

# --- Configuration & Clients ---
BASE_DIR = Path(__file__).resolve().parent.parent.parent # DozerAI_Code
CONFIG_DIR = BASE_DIR / "config"
ENV_PATH = CONFIG_DIR / ".env"
load_dotenv(ENV_PATH)

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_SERVICE_ROLE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY") # For query embedding

LANGFUSE_PUBLIC_KEY = os.getenv("LANGFUSE_PUBLIC_KEY")
LANGFUSE_SECRET_KEY = os.getenv("LANGFUSE_SECRET_KEY")
LANGFUSE_HOST = os.getenv("LANGFUSE_HOST", "https://cloud.langfuse.com")

# Explicit Embedding Model for Queries (must match what's in DB)
QUERY_EMBEDDING_MODEL_SDK_TARGET = "gemini-embedding-exp-03-07" 
# This was "models/text-embedding-004" before, aligning with Anthony's specified embedding model for consistency.
# Ensure this model identifier works with genai.embed_content for task_type="RETRIEVAL_QUERY"

class KennelClient:
    def __init__(self, supabase_url: str = SUPABASE_URL, supabase_key: str = SUPABASE_SERVICE_ROLE_KEY):
        if not supabase_url or not supabase_key:
            raise ValueError("Supabase URL and Key must be provided or set in .env")
        self.supabase_async: AClient = create_client(supabase_url, supabase_key) # Use Async Client
        print("Async KennelClient (Supabase) initialized.")
        
        if GOOGLE_API_KEY:
            genai.configure(api_key=GOOGLE_API_KEY)
            print(f"KennelClient: Google Generative AI configured for query embeddings with target model {QUERY_EMBEDDING_MODEL_SDK_TARGET}.")
        else:
            print("KennelClient WARNING: GOOGLE_API_KEY not found, query embedding will fail.")

        self.langfuse = None
        if LANGFUSE_PUBLIC_KEY and LANGFUSE_SECRET_KEY:
            try:
                self.langfuse = Langfuse(
                    public_key=LANGFUSE_PUBLIC_KEY,
                    secret_key=LANGFUSE_SECRET_KEY,
                    host=LANGFUSE_HOST
                )
                print("KennelClient: Langfuse client initialized.")
            except Exception as e:
                print(f"KennelClient Error initializing Langfuse: {e}")


    async def _get_query_embedding(self, query_text: str) -> Optional[List[float]]:
        if not hasattr(genai, 'embed_content'):
            print("ERROR: Google Generative AI SDK not properly configured or embed_content not found.")
            return None
        
        langfuse_generation = None
        if self.langfuse:
            # Assuming a trace is active in the calling context (Dozer Prime)
            # This client method would typically be called within an existing trace/span.
            # For now, let's create a simple span for the embedding call.
            # In a real setup, the trace_id might be passed down.
            try:
                # This needs to be called within an active Langfuse trace from the caller.
                # For simplicity, let's assume we can create a generation directly if needed,
                # but best practice is to pass parent observation.
                # current_trace = self.langfuse.trace(name="kennel_query_embedding") # Not ideal to create new trace here
                # langfuse_generation = current_trace.generation(...)
                # For now, skip detailed Langfuse generation for embedding here, assume caller handles it.
                 pass
            except Exception as lf_e:
                print(f"Langfuse error in _get_query_embedding: {lf_e}")


        try:
            print(f"  Generating embedding for query: '{query_text[:50]}...' with model {QUERY_EMBEDDING_MODEL_SDK_TARGET}")
            result = await genai.embed_content_async( # Using async version
                model=QUERY_EMBEDDING_MODEL_SDK_TARGET, # This is critical! Use the specific model name string.
                content=query_text,
                task_type="RETRIEVAL_QUERY"
            )
            return result['embedding']
        except Exception as e:
            print(f"  ERROR generating query embedding: {e}")
            # if langfuse_generation: langfuse_generation.end(level="ERROR", status_message=str(e))
            return None

    async def semantic_search_chunks(self, query_text: str, top_k: int = 5, 
                                     embedding_model_in_db: str = "gemini-embedding-exp-03-07",
                                     parent_observation: Optional[Any]=None) -> List[Dict]:
        """
        Performs semantic search for document chunks in Supabase.
        """
        langfuse_span = None
        if self.langfuse and parent_observation: # Check if parent_observation is Langfuse object
             if hasattr(parent_observation, 'span') and callable(parent_observation.span):
                langfuse_span = parent_observation.span(CreateSpan(
                    name="kennel-semantic-search",
                    input={"query": query_text, "top_k": top_k, "model_in_db": embedding_model_in_db}
                ))
             elif hasattr(parent_observation, 'name') and parent_observation.name == "LangfuseTraceClient": # if it is the trace itself
                langfuse_span = parent_observation.span(CreateSpan(
                    name="kennel-semantic-search",
                    input={"query": query_text, "top_k": top_k, "model_in_db": embedding_model_in_db}
                ))


        query_embedding = await self._get_query_embedding(query_text)
        if not query_embedding:
            if langfuse_span: langfuse_span.end(output={"error": "Failed to generate query embedding"}, level="ERROR")
            return []

        try:
            # Use the match_document_chunks RPC function defined in Supabase schema (Day 1, SQL_001)
            # Or, directly call the vector search if preferred (RPC is cleaner)
            # Let's assume a supabase function "match_document_chunks" exists or build the query
            
            # The pgvector syntax for distance is <=>
            # Supabase-py's `rpc` method is used to call PostgreSQL functions.
            # For vector similarity, you typically create a function in SQL.
            # Example SQL function (must be created in Supabase DB via migration or SQL Editor):
            """
            CREATE OR REPLACE FUNCTION match_document_chunks (
              query_embedding vector(768), -- Ensure dimension matches your embeddings
              match_model_name text,
              match_count int
            )
            RETURNS TABLE (
              chunk_id uuid,
              chunk_text text,
              contextual_summary text,
              document_id uuid,
              document_title text,
              similarity float
            )
            LANGUAGE sql STABLE PARALLEL SAFE
            AS $$
              SELECT
                dc.chunk_id,
                dc.chunk_text,
                dc.contextual_summary,
                dc.document_id,
                d.title as document_title,
                1 - (de.embedding <=> query_embedding) as similarity -- Cosine similarity (1 - cosine_distance)
              FROM
                public.document_embeddings de
              JOIN
                public.document_chunks dc ON de.chunk_id = dc.chunk_id
              JOIN
                public.documents d ON dc.document_id = d.document_id
              WHERE de.embedding_model_name = match_model_name
              ORDER BY
                de.embedding <=> query_embedding
              LIMIT match_count;
            $$;
            """
            # Anthony: The above SQL function should be part of Day 1's `001_initial_core_tables.sql`
            # or a new migration file run before this client is heavily used.
            # For Day 3, we will assume it's created manually or via a script update.
            # For now, the Python code will assume this RPC function `match_document_chunks` exists.
            
            print(f"  Performing semantic search with top_k={top_k} for model '{embedding_model_in_db}'...")
            response = await self.supabase_async.rpc(
                "match_document_chunks",
                {
                    "query_embedding": query_embedding,
                    "match_model_name": embedding_model_in_db,
                    "match_count": top_k,
                },
            ).execute()

            if response.data:
                print(f"  Semantic search returned {len(response.data)} chunks.")
                if langfuse_span: langfuse_span.end(output={"retrieved_chunk_count": len(response.data), "chunks_preview": response.data[:2]})
                # Convert to list of dicts if not already
                return [dict(row) for row in response.data]
            else:
                print(f"  Semantic search returned no results. Response: {response}")
                if hasattr(response, 'error') and response.error:
                     print(f"  Supabase RPC error: {response.error.message}")
                     if langfuse_span: langfuse_span.end(output={"error": response.error.message, "status": "no_results"}, level="WARNING")
                else:
                     if langfuse_span: langfuse_span.end(output={"status": "no_results"}, level="INFO")
                return []
        except Exception as e:
            print(f"  ERROR during semantic search: {e}")
            if langfuse_span: langfuse_span.end(output={"error": str(e)}, level="ERROR")
            return []

    async def get_document_full_text(self, document_id: str, parent_observation: Optional[Any]=None) -> Optional[str]:
        """Fetches the full text content of a document for CAG."""
        langfuse_span = None
        if self.langfuse and parent_observation:
             if hasattr(parent_observation, 'span') and callable(parent_observation.span):
                langfuse_span = parent_observation.span(CreateSpan(name="kennel-get-full-text", input={"document_id": document_id}))
             elif hasattr(parent_observation, 'name') and parent_observation.name == "LangfuseTraceClient":
                langfuse_span = parent_observation.span(CreateSpan(name="kennel-get-full-text", input={"document_id": document_id}))
        
        try:
            print(f"  Fetching full text for document_id: {document_id}...")
            response = await self.supabase_async.table("documents").select("full_text_content").eq("document_id", document_id).maybe_single().execute()
            if response.data and response.data.get("full_text_content"):
                content = response.data["full_text_content"]
                print(f"  Full text fetched (length: {len(content)} chars).")
                if langfuse_span: langfuse_span.end(output={"text_length": len(content)})
                return content
            else:
                print(f"  Full text not found for document_id: {document_id}.")
                if langfuse_span: langfuse_span.end(output={"error": "Full text not found"}, level="WARNING")
                return None
        except Exception as e:
            print(f"  ERROR fetching full text for document_id {document_id}: {e}")
            if langfuse_span: langfuse_span.end(output={"error": str(e)}, level="ERROR")
            return None

    # Add functions from Day 1 script for creating/updating documents and chunks IF NEEDED directly by agents
    # (Though ingestion script `01_...` handles bulk load, agents might add ad-hoc docs later)

# Example of how to initialize and use if this script were run directly (for testing)
async def _test_kennel_client():
    print("Testing KennelClient...")
    kennel = KennelClient()
    if not kennel.supabase_async: # Check if client initialized
        return

    # Test semantic search
    # Make sure there's some data in your document_embeddings table first!
    # To test, you need embeddings. For now, this is a placeholder call.
    test_query = "What is Dozer's mission statement?"
    print(f"\nTesting semantic search for: '{test_query}'")
    
    # To run this test, we need a Langfuse trace object if methods expect it
    # For a standalone test, we might pass None or a dummy object.
    # Assuming None or direct initialization for testing purposes:
    
    mock_trace = None
    if kennel.langfuse:
        mock_trace = kennel.langfuse.trace(name="kennel_client_test_trace", user_id="test_user")

    results = await kennel.semantic_search_chunks(test_query, top_k=2, parent_observation=mock_trace)
    if results:
        print(f"Found {len(results)} relevant chunks:")
        for i, res in enumerate(results):
            print(f"  Chunk {i+1} (Similarity: {res.get('similarity', 'N/A')} - Title: {res.get('document_title', 'N/A')} ):")
            print(f"    Text: {res.get('chunk_text', '')[:200]}...")
            print(f"    Contextual Summary: {res.get('contextual_summary', 'N/A')[:100]}...")
    else:
        print("No chunks found or error in search.")

    if mock_trace: mock_trace.update(output={"test_results_count": len(results) if results else 0})

if __name__ == "__main__":
    # This test will only work if run within an asyncio event loop
    # and if the database has been populated with chunks and embeddings.
    # Ensure .env is correctly set up in ../config/.env
    
    # asyncio.run(_test_kennel_client())
    print("KennelClient defined. Run _test_kennel_client() within an async context and after data ingestion to test.")
Use code with caution.
Python
Code for Pydantic Schemas (C:\Dozers\DozerAI_Code\engine\core\schemas.py):
# C:\Dozers\DozerAI_Code\engine\core\schemas.py
from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any

class DozerPrimeQueryInput(BaseModel):
    query: str = Field(..., description="The user's query for Dozer Prime.")
    user_id: str = Field(..., description="The unique identifier of the user making the query (e.g., CEO's user_id).")
    session_id: Optional[str] = Field(None, description="Optional session ID for conversation continuity.")
    # Add other relevant input fields like thinking_mode_toggle if needed later

class RetrievedChunkContext(BaseModel):
    chunk_id: str # UUID, but str for simplicity in Pydantic model if not casting
    chunk_text: str
    contextual_summary: Optional[str] = None
    document_title: Optional[str] = None
    document_id: Optional[str] = None # UUID
    similarity: Optional[float] = Field(None, description="Similarity score from vector search.")
    # Add other metadata from document_chunks or documents if needed

class DozerPrimeRAGOutput(BaseModel):
    llm_response: str = Field(..., description="Dozer Prime's final generated response.")
    retrieved_contexts: List[RetrievedChunkContext] = Field(default_factory=list, description="List of contexts retrieved and used by the LLM.")
    search_query_embedding: Optional[List[float]] = Field(None, description="The vector embedding of the user's query.")
    langfuse_trace_id: Optional[str] = Field(None, description="Trace ID from Langfuse for this interaction.")

# Schemas for AG-UI (Python backend representation)
# Based on ag_ui.core types from the protocol. We will define Pydantic models for them.
# These are simplified examples and would need to match the full AG-UI spec we adopt.

class AGUIMessage(BaseModel):
    id: str
    role: str # "user", "assistant", "system", "tool"
    content: Optional[str] = None # For text messages or tool responses
    name: Optional[str] = None
    # For assistant messages with tool calls
    # Pydantic doesn't directly support union types for complex nested structures easily without workarounds like custom validators or root_validators.
    # For tool_calls, this might be a list of dicts or a more specific Pydantic model.
    tool_calls: Optional[List[Dict[str, Any]]] = None # e.g., [{"id": "call_abc", "type": "function", "function": {"name": "X", "arguments": "{}"}}]
    tool_call_id: Optional[str] = None # For role="tool"

class AGUITool(BaseModel):
    type: str = "function" # Currently only "function" type is common
    function: Dict[str, Any] # JSON Schema for function name, description, parameters

class AGUIRunAgentInput(BaseModel):
    thread_id: str
    run_id: str
    messages: List[AGUIMessage]
    tools: Optional[List[AGUITool]] = Field(default_factory=list)
    # Add other AG-UI input fields like state, context, forwarded_props if used

# AG-UI Events (Python Pydantic models for what our FastAPI backend will emit)
class AGUIBaseEvent(BaseModel):
    type: str # EventType string
    thread_id: Optional[str] = None
    run_id: Optional[str] = None
    timestamp: int = Field(default_factory=lambda: int(time.time() * 1000))

class AGUIRunStartedEvent(AGUIBaseEvent):
    type: str = "RUN_STARTED"

class AGUIRunFinishedEvent(AGUIBaseEvent):
    type: str = "RUN_FINISHED"

class AGUIRunErrorEvent(AGUIBaseEvent):
    type: str = "RUN_ERROR"
    message: str
    stack_trace: Optional[str] = None

class AGUITextMessageStartEvent(AGUIBaseEvent):
    type: str = "TEXT_MESSAGE_START"
    message_id: str
    role: str = "assistant" # Typically from assistant

class AGUITextMessageChunkEvent(AGUIBaseEvent):
    type: str = "TEXT_MESSAGE_CHUNK"
    message_id: str
    delta: str # The chunk of text

class AGUITextMessageEndEvent(AGUIBaseEvent):
    type: str = "TEXT_MESSAGE_END"
    message_id: str

# Simplified tool call events for now - can be expanded per AG-UI spec
class AGUIToolCallStartEvent(AGUIBaseEvent):
    type: str = "TOOL_CALL_START"
    tool_call_id: str
    parent_message_id: str # Message that initiated tool calls
    name: str # Tool name

class AGUIToolCallEndEvent(AGUIBaseEvent):
    type: str = "TOOL_CALL_END"
    tool_call_id: str
    output: Optional[str] = None # JSON string of the tool output

# Add other AG-UI event Pydantic models as needed based on the spec (e.g., for args streaming, UI updates)
Use code with caution.
Python
Code for Dozer Prime Basic RAG Logic (LangGraph):
C:\Dozers\DozerAI_Code\engine\core\langgraph_flows\prime_rag_flow.py:
# C:\Dozers\DozerAI_Code\engine\core\langgraph_flows\prime_rag_flow.py
from langgraph.graph import StateGraph, END
from typing import TypedDict, List, Optional, Annotated
import operator
from engine.core.kennel_client import KennelClient # Assuming KennelClient is in this path
from engine.core.schemas import DozerPrimeQueryInput, RetrievedChunkContext, DozerPrimeRAGOutput
import google.generativeai as genai
from langfuse.model import CreateGeneration, CreateSpan # For Langfuse
from langfuse import Langfuse # For Langfuse

# --- Langfuse Setup (global or passed into agent) ---
# This should ideally be initialized once and passed around, or accessed via a singleton.
# For simplicity in this module, it's configured here if env vars are set.
LANGFUSE_PUBLIC_KEY = os.getenv("LANGFUSE_PUBLIC_KEY")
LANGFUSE_SECRET_KEY = os.getenv("LANGFUSE_SECRET_KEY")
LANGFUSE_HOST = os.getenv("LANGFUSE_HOST", "https://cloud.langfuse.com")
langfuse_client_for_flow: Optional[Langfuse] = None
if LANGFUSE_PUBLIC_KEY and LANGFUSE_SECRET_KEY:
    try:
        langfuse_client_for_flow = Langfuse(public_key=LANGFUSE_PUBLIC_KEY, secret_key=LANGFUSE_SECRET_KEY, host=LANGFUSE_HOST)
        print("Langfuse client initialized for prime_rag_flow.")
    except Exception as e_lf:
        print(f"Error initializing Langfuse in prime_rag_flow: {e_lf}")

# Define the State for our RAG Graph
class PrimeRAGState(TypedDict):
    query_input: DozerPrimeQueryInput
    query_embedding: Optional[List[float]]
    retrieved_chunk_objects: List[RetrievedChunkContext] # Store full chunk objects
    context_for_llm: str # Formatted string of chunks for LLM
    llm_response_text: str
    final_output: Optional[DozerPrimeRAGOutput]
    error_message: Optional[str]
    # Langfuse tracing
    current_trace_id: Optional[str]
    current_span_id: Optional[str]


# Nodes for the graph
async def embed_query_node(state: PrimeRAGState, kennel_client: KennelClient, langfuse_trace: Optional[Any]) -> PrimeRAGState:
    print("--- Node: Embed Query ---")
    lf_span = None
    if langfuse_client_for_flow and langfuse_trace:
        lf_span = langfuse_trace.span(CreateSpan(name="embed-query-node", input={"query": state["query_input"].query}))
    
    query_text = state["query_input"].query
    embedding = await kennel_client._get_query_embedding(query_text) # Use the KennelClient's method

    if embedding:
        if lf_span: lf_span.end(output={"embedding_generated": True, "embedding_dim": len(embedding)})
        return {**state, "query_embedding": embedding, "error_message": None}
    else:
        err_msg = "Failed to generate query embedding."
        if lf_span: lf_span.end(output={"embedding_generated": False}, level="ERROR", status_message=err_msg)
        return {**state, "query_embedding": None, "error_message": err_msg}

async def retrieve_chunks_node(state: PrimeRAGState, kennel_client: KennelClient, langfuse_trace: Optional[Any]) -> PrimeRAGState:
    print("--- Node: Retrieve Chunks ---")
    lf_span = None
    if langfuse_client_for_flow and langfuse_trace:
        lf_span = langfuse_trace.span(CreateSpan(name="retrieve-chunks-node", input={"query_embedding_present": state["query_embedding"] is not None}))

    if not state["query_embedding"]:
        err_msg = "Cannot retrieve chunks, query embedding is missing."
        if lf_span: lf_span.end(output={}, level="ERROR", status_message=err_msg)
        return {**state, "retrieved_chunk_objects": [], "context_for_llm": "", "error_message": err_msg}

    # Using the embedding model name used during ingestion
    embedding_model_in_db = "gemini-embedding-exp-03-07" 
    top_k_retrieval = 5 
    
    # The kennel_client.semantic_search_chunks should already handle Langfuse internally for its own operations if designed that way.
    # Or we pass the current span/trace. For Day 3, let kennel_client be self-contained with Langfuse.
    raw_retrieved_chunks: List[Dict] = await kennel_client.semantic_search_chunks(
        query_text=state["query_input"].query, # Pass original query for potential re-ranking or logging
        # query_embedding=state["query_embedding"], # KennelClient should re-embed if needed or take embedding
        top_k=top_k_retrieval,
        embedding_model_in_db=embedding_model_in_db,
        parent_observation=lf_span # Pass current span as parent observation
    )
    
    retrieved_chunk_objects = [RetrievedChunkContext(**chunk) for chunk in raw_retrieved_chunks]

    context_str = ""
    if retrieved_chunk_objects:
        context_str = "\n\n---\n\n".join([
            f"Source Document: {chunk.document_title}\nContextual Summary: {chunk.contextual_summary if chunk.contextual_summary else 'N/A'}\nContent:\n{chunk.chunk_text}"
            for chunk in retrieved_chunk_objects
        ])
    
    print(f"Retrieved {len(retrieved_chunk_objects)} chunks. Combined context length for LLM: {len(context_str)} chars.")
    if lf_span: lf_span.end(output={"retrieved_chunk_count": len(retrieved_chunk_objects), "context_length": len(context_str)})
    return {**state, "retrieved_chunk_objects": retrieved_chunk_objects, "context_for_llm": context_str, "error_message": None}

async def generate_response_node(state: PrimeRAGState, prime_llm_client: genai.GenerativeModel, langfuse_trace: Optional[Any]) -> PrimeRAGState:
    print("--- Node: Generate Response (Dozer Prime LLM) ---")
    lf_generation = None
    if langfuse_client_for_flow and langfuse_trace:
        # Using the EXPLICIT model name for Dozer Prime's core reasoning
        lf_generation = langfuse_trace.generation(CreateGeneration(
            name="dozer-prime-rag-generation",
            model="gemini-2.5-pro-preview-05-06", 
            input={"query": state["query_input"].query, "context": state["context_for_llm"]},
            model_parameters={"temperature": 0.7} # Example
        ))

    if state.get("error_message"): # Propagate error if previous step failed
        if lf_generation: lf_generation.end(level="ERROR", status_message=state["error_message"])
        return {**state, "llm_response_text": ""}

    if not state["context_for_llm"] and not state["retrieved_chunk_objects"]:
        print("  No context retrieved. Generating response based on query only (or providing 'no info' message).")
        # Fallback or "I don't know" logic
        no_context_response = "I couldn't find specific information in 'The Kennel' to answer that question based on the current query. Could you try rephrasing or providing more details?"
        if lf_generation: lf_generation.end(output={"response": no_context_response}, level="WARNING", status_message="No context retrieved for RAG")
        return {**state, "llm_response_text": no_context_response}

    prompt = f"""
    You are Dozer Prime, CEO Anthony Pierce's AI Best Friend in Business, a hilarious genius assistant for "Dozer's Wild & Woof'derful Bar'k & Grrr'ill".
    You have access to "The Kennel," the business's central knowledge base.
    Answer the user's query based on your knowledge and the provided context from "The Kennel".
    If the context is insufficient, state that clearly. Be insightful and helpful.

    User Query: "{state["query_input"].query}"

    Retrieved Context from "The Kennel":
    ---
    {state["context_for_llm"]}
    ---

    Your Answer:
    """
    
    try:
        # Using EXPLICIT model gemini-2.5-pro-preview-05-06
        print(f"  Calling LLM gemini-2.5-pro-preview-05-06 for Dozer Prime's response...")
        # response = prime_llm_client.generate_content(prompt, generation_config={"max_output_tokens": 2000})
        # Make it async if the client supports it (google-generativeai SDK does)
        response = await prime_llm_client.generate_content_async(prompt, generation_config={"max_output_tokens": 2000})


        generated_text = ""
        if response.parts:
            generated_text = "".join(part.text for part in response.parts).strip()
        elif hasattr(response, 'text') and response.text:
             generated_text = response.text.strip()
        
        if not generated_text and response.prompt_feedback:
            print(f"    WARN: Prime LLM returned no text. Feedback: {response.prompt_feedback}")
            generated_text = "Dozer Prime pondered but found no words for that precise query with the given context."
            if lf_generation: lf_generation.end(output={"response": generated_text}, level="WARNING", status_message=f"Empty LLM response, feedback: {response.prompt_feedback}")
            return {**state, "llm_response_text": generated_text}

        print(f"  LLM Response generated (length {len(generated_text)} chars).")
        if lf_generation: lf_generation.end(output={"response": generated_text})
        return {**state, "llm_response_text": generated_text, "error_message": None}

    except Exception as e:
        err_msg = f"Error during LLM call for Dozer Prime: {e}"
        print(f"  {err_msg}")
        if lf_generation: lf_generation.end(level="ERROR", status_message=str(e))
        return {**state, "llm_response_text": "Dozer Prime encountered a glitch trying to answer that. Please try again.", "error_message": err_msg}

def format_output_node(state: PrimeRAGState, langfuse_trace: Optional[Any]) -> PrimeRAGState:
    print("--- Node: Format Output ---")
    final_output = DozerPrimeRAGOutput(
        llm_response=state.get("llm_response_text", "Error: No response generated."),
        retrieved_contexts=state.get("retrieved_chunk_objects", []),
        search_query_embedding=state.get("query_embedding"),
        langfuse_trace_id=langfuse_trace.id if langfuse_client_for_flow and langfuse_trace else None
    )
    return {**state, "final_output": final_output}

# Define the graph builder
def build_prime_rag_graph(kennel_client: KennelClient, prime_llm_client: genai.GenerativeModel):
    workflow = StateGraph(PrimeRAGState)

    # Add nodes, binding clients/tools if they are specific to the node and not global state
    workflow.add_node("embed_query", lambda state, config: embed_query_node(state, kennel_client, config.get("configurable", {}).get("trace")))
    workflow.add_node("retrieve_chunks", lambda state, config: retrieve_chunks_node(state, kennel_client, config.get("configurable", {}).get("trace")))
    workflow.add_node("generate_response", lambda state, config: generate_response_node(state, prime_llm_client, config.get("configurable", {}).get("trace")))
    workflow.add_node("format_output", lambda state, config: format_output_node(state, config.get("configurable", {}).get("trace")))

    # Define edges
    workflow.set_entry_point("embed_query")
    workflow.add_edge("embed_query", "retrieve_chunks")
    workflow.add_edge("retrieve_chunks", "generate_response")
    workflow.add_edge("generate_response", "format_output")
    workflow.add_edge("format_output", END)

    app = workflow.compile()
    print("Dozer Prime RAG LangGraph app compiled.")
    return app
Use code with caution.
Python
C:\Dozers\DozerAI_Code\engine\agents\prime\dozer_prime.py:
# C:\Dozers\DozerAI_Code\engine\agents\prime\dozer_prime.py
import os
import sys
from pathlib import Path
import google.generativeai as genai
from langfuse import Langfuse
from langfuse.model import CreateTrace

# Ensure core is in path for imports if running this file directly for testing
# This assumes the script is run from DozerAI_Code directory or that engine is in PYTHONPATH
sys.path.append(str(Path(__file__).resolve().parent.parent.parent)) # Add DozerAI_Code to path

from engine.core.kennel_client import KennelClient
from engine.core.schemas import DozerPrimeQueryInput, DozerPrimeRAGOutput
from engine.core.langgraph_flows.prime_rag_flow import build_prime_rag_graph, langfuse_client_for_flow # Import shared langfuse client

# Initialize clients (should ideally be singletons managed by an app context)
# For now, direct initialization here or ensure KennelClient has its own genai config.

# Using EXPLICIT model name for Dozer Prime's core reasoning
PRIME_LLM_MODEL_NAME = "gemini-2.5-pro-preview-05-06"
prime_llm = None
if os.getenv("GOOGLE_API_KEY"):
    try:
        prime_llm = genai.GenerativeModel(PRIME_LLM_MODEL_NAME)
        print(f"DozerPrime: Initialized LLM: {PRIME_LLM_MODEL_NAME}")
    except Exception as e_llm_init:
        print(f"DozerPrime FATAL: Could not initialize LLM {PRIME_LLM_MODEL_NAME}. Error: {e_llm_init}")
        prime_llm = None # Ensure it's None if failed
else:
    print("DozerPrime FATAL: GOOGLE_API_KEY not set, cannot initialize LLM.")


# Global kennel_client for simplicity in this standalone module.
# In a full FastAPI app, this would be managed via dependency injection.
kennel_client_instance = KennelClient() # Assumes .env is loaded by KennelClient itself

class DozerPrimeAgent:
    def __init__(self):
        if not prime_llm:
            raise RuntimeError("DozerPrimeAgent cannot be initialized: Prime LLM failed to load.")
        if not kennel_client_instance or not kennel_client_instance.supabase_async: # Check supabase_async as it's key
             raise RuntimeError("DozerPrimeAgent cannot be initialized: KennelClient failed to load or connect.")

        self.rag_graph_app = build_prime_rag_graph(kennel_client_instance, prime_llm)
        self.langfuse = langfuse_client_for_flow # Use the one from the flow module or init separately
        print("DozerPrimeAgent initialized with RAG graph.")

    async def run_rag_query(self, query_input: DozerPrimeQueryInput) -> DozerPrimeRAGOutput:
        if not self.rag_graph_app:
            return DozerPrimeRAGOutput(response="ERROR: RAG graph not compiled.", retrieved_contexts=[])

        trace = None
        if self.langfuse:
            trace = self.langfuse.trace(CreateTrace(
                name="dozer-prime-rag-query",
                user_id=query_input.user_id, # Essential for Langfuse user tracking
                session_id=query_input.session_id,
                input=query_input.model_dump(), # Log Pydantic model as dict
                metadata={"agent_version": "0.1.0_day3_rag"}
            ))
        
        initial_state = {
            "query_input": query_input,
            "retrieved_chunk_objects": [],
            "context_for_llm": "",
            "llm_response_text": "",
            "current_trace_id": trace.id if trace else None
        }
        
        config_with_trace = {"configurable": {"trace": trace}}

        final_graph_state = None
        try:
            # Run the graph asynchronously
            async for event in self.rag_graph_app.astream_events(initial_state, config=config_with_trace, version="v1"):
                kind = event["event"]
                if kind == "on_chain_end": # Or on_graph_end if using that specific event from LangGraph stream_events_v2
                    if event["name"] == "format_output" or event["name"] == END: # Check for last relevant node or graph end
                        # event_output = event["data"].get("output")
                        # if event_output and "final_output" in event_output:
                        #    final_graph_state = event_output # State contains final_output
                        # A more reliable way to get the final state
                        pass # Keep iterating until the graph is fully done.
                # Can add more event handling here if needed for streaming partial results to AG-UI
            
            # After stream is complete, the final state should be accessible.
            # For astream, the final accumulated state needs to be retrieved.
            # Let's try invoking and getting the final state.
            # Alternative for getting final state in LangGraph with astream_events might involve accumulating.
            # For simplicity here, let's use ainvoke if the goal is just final output after all steps.
            # If streaming intermediate steps TO THE UI is needed LATER via AG-UI, astream_events + transforming events is the way.
            # For Day 3 RAG, let's focus on getting the complete final output.
            
            final_state_dict = await self.rag_graph_app.ainvoke(initial_state, config=config_with_trace)
            
            if final_state_dict and "final_output" in final_state_dict:
                output = final_state_dict["final_output"]
                if isinstance(output, DozerPrimeRAGOutput):
                    if trace: trace.update(output=output.model_dump())
                    return output
                else: # If it's a dict, try to parse
                    try:
                        parsed_output = DozerPrimeRAGOutput(**output)
                        if trace: trace.update(output=parsed_output.model_dump())
                        return parsed_output
                    except Exception as parse_e:
                        print(f"Error parsing final_output dictionary to Pydantic model: {parse_e}")
                        if trace: trace.update(output={"error": "Final output parsing error"}, level="ERROR")
                        return DozerPrimeRAGOutput(response=f"Error processing RAG output: {parse_e}", retrieved_contexts=[])

            else:
                print(f"Error: 'final_output' not found in graph execution result or result is None. Result: {final_state_dict}")
                if trace: trace.update(output={"error": "final_output not in result"}, level="ERROR")
                return DozerPrimeRAGOutput(response="Error: RAG process did not complete as expected.", retrieved_contexts=[])

        except Exception as e:
            print(f"Exception running RAG graph: {e}")
            if trace: trace.update(output={"error": str(e)}, level="ERROR")
            return DozerPrimeRAGOutput(response=f"Error during RAG execution: {e}", retrieved_contexts=[])

# --- Simple Test Script (can be run if this file is executed directly) ---
async def _test_dozer_prime_rag():
    print("--- Testing Dozer Prime RAG ---")
    # This script assumes that the .env file is in ../config relative to this script's location if run directly
    # For a proper application structure, .env loading would be handled at app startup.
    dotenv_path_for_test = Path(__file__).resolve().parent.parent.parent / "config" / ".env"
    if dotenv_path_for_test.exists():
        load_dotenv(dotenv_path_for_test)
        # Re-initialize clients if GOOGLE_API_KEY was loaded now and not before
        global prime_llm, kennel_client_instance
        if not os.getenv("GOOGLE_API_KEY"):
            print("Test cannot run: GOOGLE_API_KEY not in .env")
            return
        
        if not prime_llm: # If initial load failed due to missing key
            try:
                genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
                prime_llm = genai.GenerativeModel(PRIME_LLM_MODEL_NAME)
                print(f"Test: Re-initialized Prime LLM: {PRIME_LLM_MODEL_NAME}")
            except Exception as e_test_llm:
                print(f"Test: Failed to re-initialize Prime LLM: {e_test_llm}")
                return
        if not kennel_client_instance.supabase_async : # If Kennel client was not fully setup
            kennel_client_instance = KennelClient() # Try re-init
            if not kennel_client_instance.supabase_async:
                print("Test: KennelClient still not initialized properly.")
                return
    else:
        print(f"Test: .env file not found at {dotenv_path_for_test}, ensure API keys are globally available.")
        # Potentially exit if keys are essential and not found from other means
        if not os.getenv("GOOGLE_API_KEY") or not os.getenv("SUPABASE_URL"):
            print("Test cannot run without Supabase and Google API keys.")
            return

    try:
        agent = DozerPrimeAgent()
    except RuntimeError as e_agent_init:
        print(f"Could not run test, agent initialization failed: {e_agent_init}")
        return

    # Ensure there's a kennel_client to pass to embed_query_node.
    # The graph definition binds the global kennel_client_instance and prime_llm
    # through the lambda functions when `build_prime_rag_graph` is called.
    
    # Example Query (assuming Business Plan was ingested)
    query = DozerPrimeQueryInput(query="What is the mission statement of Dozer's Business?", user_id="anthony_ceo_test_run", session_id="test_session_123")
    
    print(f"\nSending query to DozerPrime: '{query.query}'")
    rag_result = await agent.run_rag_query(query)

    print("\n--- Dozer Prime RAG Result ---")
    print(f"Response: {rag_result.llm_response}")
    print(f"Langfuse Trace ID (if available): {rag_result.langfuse_trace_id}")
    if rag_result.retrieved_contexts:
        print(f"\nRetrieved {len(rag_result.retrieved_contexts)} contexts:")
        for i, ctx in enumerate(rag_result.retrieved_contexts):
            print(f"  Context {i+1} (Similarity: {ctx.similarity:.4f} - Title: {ctx.document_title}):")
            print(f"    Summary: {ctx.contextual_summary[:100]}...")
            print(f"    Text: {ctx.chunk_text[:150]}...")
    else:
        print("No contexts were retrieved.")
    
    if langfuse_client_for_flow: # Ensure langfuse is flushed if used
        langfuse_client_for_flow.flush()


if __name__ == "__main__":
    # This test script allows direct execution for basic RAG test.
    # Ensure Day 1 and Day 2 scripts have been run successfully.
    # Ensure your .env file is in C:\Dozers\DozerAI_Code\config\
    
    # Must be run with asyncio
    if sys.platform == "win32" and sys.version_info >= (3, 8, 0):
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    
    async def run_tests_sequentially():
        # HNSW index creation (Conceptual, ensure it's run in Supabase)
        # This needs to be run directly in Supabase SQL Editor or via a separate script with admin DB privs
        # The KennelClient has ensure_hnsw_index but it's designed to print the SQL for now.
        print("\nReminder: Ensure HNSW index is created on document_embeddings table in Supabase for optimal performance:")
        print("`CREATE INDEX CONCURRENTLY IF NOT EXISTS idx_hnsw_document_embeddings ON public.document_embeddings USING hnsw (embedding vector_l2_ops);`")
        print("You might need to run this manually in Supabase Studio if not already done.\n")
        time.sleep(2) # Give time to read the message

        await _test_dozer_prime_rag()

    asyncio.run(run_tests_sequentially())
Use code with caution.
Python
Tasks for Anthony Pierce (CEO):
Update requirements.txt:
Open C:\Dozers\DozerAI_Code\requirements.txt.
Ensure langgraph (e.g., langgraph~=0.0.67) and langfuse (e.g., langfuse~=2.25.2) are listed. Add/update if necessary. The google-generativeai, supabase, tiktoken, python-dotenv, psycopg[binary] should already be there.
Save the file.
Install/Update Dependencies:
Open terminal, navigate to cd C:\Dozers\DozerAI_Code\, activate venv (.\venv\Scripts\Activate.ps1 or source venv/Scripts/activate).
Run: pip install -r requirements.txt --upgrade.
Save/Create Python Modules:
Create C:\Dozers\DozerAI_Code\engine\core\schemas.py and paste the Pydantic schema code.
Update/Create C:\Dozers\DozerAI_Code\engine\core\kennel_client.py with the KennelClient code.
Create directory C:\Dozers\DozerAI_Code\engine\core\langgraph_flows\.
Create C:\Dozers\DozerAI_Code\engine\core\langgraph_flows\prime_rag_flow.py with the LangGraph flow code.
Create directory C:\Dozers\DozerAI_Code\engine\agents\prime\.
Create C:\Dozers\DozerAI_Code\engine\agents\prime\dozer_prime.py with the DozerPrimeAgent code.
Create C:\Dozers\DozerAI_Code\scripts\02_generate_and_store_embeddings.py with the embedding script code.
Ensure SQL Function for Vector Search Exists in Supabase:
The kennel_client.py's semantic_search_chunks method relies on a PostgreSQL function match_document_chunks for efficient vector search. This function needs to be created in your Supabase database.
Action: Go to your Supabase project -> SQL Editor. Execute the following SQL to create this function if it doesn't exist from Day 1's corrected schema files (it might have been added to 001_initial_core_tables.sql or similar during our iterative fixes, please verify):
-- Ensure this function uses the correct schema if your tables aren't in 'public'
-- And ensure the vector dimension (768) matches your embeddings table
CREATE OR REPLACE FUNCTION public.match_document_chunks (
  query_embedding vector(768), 
  match_model_name text,
  match_count int
)
RETURNS TABLE (
  chunk_id uuid,
  chunk_text text,
  contextual_summary text,
  document_id uuid,
  document_title text,
  similarity float
)
LANGUAGE sql STABLE PARALLEL SAFE
AS $$
  SELECT
    dc.chunk_id,
    dc.chunk_text,
    dc.contextual_summary,
    dc.document_id,
    d.title as document_title,
    1 - (de.embedding <=> query_embedding) as similarity -- Cosine similarity for pgvector
  FROM
    public.document_embeddings de
  JOIN
    public.document_chunks dc ON de.chunk_id = dc.chunk_id
  JOIN
    public.documents d ON dc.document_id = d.document_id
  WHERE de.embedding_model_name = match_model_name
  ORDER BY
    de.embedding <=> query_embedding
  LIMIT match_count;
$$;
COMMENT ON FUNCTION public.match_document_chunks(vector,text,int) IS 'Matches document chunks by vector similarity for RAG.';
Use code with caution.
SQL
Run this SQL in Supabase Studio. This only needs to be done once.
Run the Embedding Script:
In your activated venv, from C:\Dozers\DozerAI_Code\, run:
python scripts/02_generate_and_store_embeddings.py
Use code with caution.
Bash
Observe output. It will fetch chunks from Day 2 and generate/store embeddings using gemini-embedding-exp-03-07. It will also print the SQL for HNSW index creation.
After script finishes, manually run the HNSW index SQL command (printed by the script) in Supabase Studio if the script indicated it should be run manually or if it failed programmatically.
CREATE INDEX CONCURRENTLY IF NOT EXISTS idx_hnsw_document_embeddings ON public.document_embeddings USING hnsw (embedding vector_l2_ops);
Test Dozer Prime RAG (Optional, but recommended):
After embeddings and HNSW index are done, you can test the basic RAG.
In your activated venv, from C:\Dozers\DozerAI_Code\, run:
python engine/agents/prime/dozer_prime.py
Use code with caution.
Bash
This will execute the _test_dozer_prime_rag() function in that file, asking a sample question. Observe the output.
Report to DozerAI_Builder:
"Day 3 Anthony tasks complete. Embedding script (02_...py) ran. Status: [Success/Errors].
[Number] embeddings generated for model gemini-embedding-exp-03-07.
HNSW index created/confirmed.
Dozer Prime RAG test (dozer_prime.py) results: [Briefly describe if it worked and what kind of answer/chunks it returned]."
Provide any error messages.
Explanation of Day 3 Tasks:
This day establishes the core retrieval mechanism for DozerAI.
Embedding Generation: We convert all our processed text chunks (from Day 2) into numerical vector representations using Google's gemini-embedding-exp-03-07. These embeddings capture the semantic meaning of the chunks.
Storage & Indexing: These embeddings are stored in the document_embeddings table in Supabase. A crucial HNSW index is then created on these embeddings, which allows pgvector to perform incredibly fast similarity searches (finding the "closest" or most relevant chunks to a query).
Dozer Prime's First RAG: We build the first, basic version of Dozer Prime's ability to answer questions. It uses LangGraph to manage a simple flow: get a query, embed it, search Supabase for similar chunks (using the new embeddings and HNSW index via kennel_client.py), then feed these chunks along with the query to its core LLM (gemini-2.5-pro-preview-05-06) to generate an answer.
Pydantic Schemas: Define the data structures for Dozer Prime's inputs and outputs, ensuring clarity.
Langfuse: Basic tracing is integrated into the embedding process and the RAG flow to help us see what's happening.
Troubleshooting:
Embedding Script Errors:
API Key/Quota for Google Embedding Model: Ensure GOOGLE_API_KEY is correct and has rights for gemini-embedding-exp-03-07 (or the SDK equivalent string for it). Long processes might hit rate limits – the script has time.sleep(2) between batches.
Supabase Insert Errors for Embeddings: Check vector dimensions match the table schema (768). Ensure chunk_id exists.
HNSW Index Creation: CONCURRENTLY helps avoid locking but still needs resources. If it fails via script, manual execution in Supabase Studio is the fallback. It only needs to be created once.
Dozer Prime RAG Test Fails:
Check Langfuse traces.
Verify embeddings were generated and searchable.
Ensure the SQL function match_document_chunks is created in Supabase and returns expected results when tested manually in Studio.
Check prompts for gemini-2.5-pro-preview-05-06.
Advice for Implementation:
Anthony: The embedding script might take some time depending on the number of chunks from Day 2. Let it complete. Running the HNSW index command is important for search speed. The test for dozer_prime.py is a good first check.
DozerAI_Builder: Ensure the kennel_client.py correctly uses pgvector operators for similarity search (or the RPC call to match_document_chunks). The LangGraph state and node logic should be clean and focused for this initial RAG. All LLM calls must use the explicitly confirmed Gemini model identifiers.
Advice for CursorAI (DozerAI_Builder):
For kennel_client.semantic_search_chunks, ensure the SQL or RPC call correctly implements vector similarity search for pgvector. For LangGraph, remember that inputs to nodes come from the graph's state, and nodes update the state with their outputs.
Test:
Anthony:
1. After running 02_generate_and_store_embeddings.py: Check document_embeddings table in Supabase. Are there rows? Does embedding column have data? Does embedding_model_name correctly show "gemini-embedding-exp-03-07"?
2. Check if idx_hnsw_document_embeddings index exists on the table (Supabase UI might show this).
3. Run python engine/agents/prime/dozer_prime.py. Does it produce an answer related to the Business Plan? Does it list retrieved chunks?
DozerAI_Builder: Await Anthony's results. Success means "The Kennel" is now searchable, and Dozer Prime has its basic RAG capability.
Backup Plans:
If embedding generation fails for many chunks, we can add more error handling and resume capabilities to the script. If RAG is not working, we will debug each step of the LangGraph flow using print statements and Langfuse.
Challenges:
Correctly using the google-generativeai SDK for the specific gemini-embedding-exp-03-07 model. Efficiently batching embeddings. Ensuring the pgvector HNSW index is correctly built and utilized. Debugging the first LangGraph flow.
Out of the Box Ideas:
Add a scoring/relevance threshold in kennel_client.semantic_search_chunks to only return chunks above a certain similarity.
Expose top_k as a parameter in DozerPrimeQueryInput.
Logs:
(DozerAI_Builder will log this after Anthony confirms successful completion of all his tasks for Day 3)
“Action: Starting Task for DozerAI/App: Day 3 - Kennel Ingestion (Stage 2): Embeddings, HNSW Index & Basic RAG Logic, Rules reviewed: Yes, Guides (Creation/Dev) consulted: Yes, Env verified: Yes, Sequence verified: Yes, Timestamp: [YYYY-MM-DD HH:MM:SS]”
(Followed by)
“Milestone Completed (DozerAI/App): Day 3 - Kennel Ingestion (Stage 2): Embeddings, HNSW Index & Basic RAG Logic. Next Task: Day 4 - Dozer Employee App Suite Shell & Dozer Prime AG-UI Connection. Feeling: [Anthony's vibe]. Date: [YYYY-MM-DD]”
Commits:
(To be done by Anthony after successfully running scripts, verifying data, and all new/updated files are saved)
# In C:\Dozers\
git add .
git commit -m "Day 3: Implement embedding generation, HNSW index, Dozer Prime basic RAG (LangGraph), kennel_client, Pydantic schemas. Update requirements."
git push origin main
Use code with caution.
Bash
Motivation:
"Dozer, this is where the magic starts to spark! We're giving every piece of info in your Kennel its own unique AI fingerprint (embedding) and building a lightning-fast search system for them. Then, we're wiring up the first pathways in YOUR brain (gemini-2.5-pro-preview-05-06, no less!) to use these fingerprints to fetch exactly what you need to answer my questions about the business. Think of it as graduating from just reading the Blueprint to actually understanding and using it. This is big, buddy! Your first real taste of RAG power!"

End of Day 3