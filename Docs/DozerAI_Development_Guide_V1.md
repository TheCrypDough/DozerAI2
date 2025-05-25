# DozerAI & Dozer Employee App Suite - Development Guide V1.0

## Phase 0: Foundation & Core MVPs for Business Plan Assistance (Target: Days 1-7)

---

**Day 1 - Kennel Foundation: Supabase Setup & "The Kennel" Initial Schema, Environment Configuration**

**Anthony's Vision (for this DozerAI/App Feature):**
"The Kennel" must be the unshakeable foundation of DozerAI's intelligence. It needs to securely store every piece of business knowledge, operational data, and employee information. Supabase, with its PostgreSQL power and integrated vector capabilities, feels like the right start. For Day 1, let's get our Supabase project live, define the absolute core database structure for ingesting the Blueprint, our chat history, and basic user/role management for the future App Suite. It needs to be ready to receive data tomorrow. We also need our `.env` file ready for all the API keys.

**Description:**
This crucial first day focuses on establishing the cloud-based data infrastructure for "The Kennel" using Supabase. We will create a new Supabase project, enable necessary extensions like `pgvector`, and define the initial PostgreSQL database schemas. These schemas will cover:
1.  Storage for raw documents (like "Dozer's Blueprint V8.0" and our development chat history).
2.  Tables for chunked document content, ready for embedding.
3.  Tables for storing vector embeddings using `pgvector`.
4.  Basic tables for future User Authentication, Roles, and Permissions to support the Dozer Employee App Suite and DozerAI's Role-Based Access Control (RBAC).
5.  Initial tables for the integrated Team Messenger functionality of the App Suite.
6.  Initial tables for Task Management and Time Clock features of the App Suite.
Additionally, we will prepare the local project configuration file (`.env`) to hold all necessary API keys and connection strings.

**Relevant Context (for DozerAI/App Suite):**
*Technical Analysis:* We are using Supabase (a cloud-hosted PostgreSQL provider) as our primary datastore ("The Kennel"). PostgreSQL's relational capabilities are ideal for structured business data, while the `pgvector` extension allows us to store and query vector embeddings directly within the same database, simplifying our RAG/CAG pipeline initially. Supabase also provides built-in authentication, Row-Level Security (RLS), object storage, and real-time capabilities crucial for the Dozer Employee App Suite.
*Layman’s Terms:* We're building the main digital library and filing cabinet for DozerAI ("The Kennel"). We're using a powerful cloud service called Supabase, which is like a super-organized warehouse with special shelves for different types of information – regular files, and special "smart index cards" (vector embeddings) that will help DozerAI find information incredibly fast. We're also setting up the basic sections for employee accounts, team chat rooms, task lists, and time sheets for the future employee app. Today also involves creating the secret lockbox (`.env` file) where we'll keep the keys to all our services.

**DozerAI_Builder's Thought Input:**
This is the most logical first step. A solid, well-structured database is non-negotiable. Supabase with `pgvector` provides a powerful and integrated solution for both structured data and our RAG/CAG needs. Defining the schemas for future App Suite features now, even if basic, helps in planning the overall data architecture. Getting the `.env` file structure ready is also critical for all subsequent API integrations.

**Anthony's Thought Input (for DozerAI/App Development):**
Anthony is keen to get "The Kennel" established so that critical business information can be ingested quickly. He emphasizes the need for scalability and security from day one. The idea of an integrated database that can handle both standard business data and AI-specific vector embeddings is appealing. He's also eager to see the groundwork for the Employee App Suite features like chat, tasks, and time clock, as these are core to his vision of an AI-integrated workforce.

**Additional Files, Documentation, Tools, Programs Needed (for DozerAI/App):**
-   Supabase Account: (Tool), (Cloud Database Service), (Primary data store for "The Kennel"), (Needed for all data persistence, auth, RAG), ([supabase.com](https://supabase.com)), (Store credentials in `.env`).
-   PostgreSQL Client (Optional but Recommended): (Tool), (e.g., pgAdmin, DBeaver, or Supabase Studio UI), (Database management & querying tool), (For direct database inspection and schema verification), (Respective websites), (Install locally).
-   `Business_Plan_Dozer_V8.md`: (Document), (Located at `C:\Dozers\Docs\Business_Plan_Dozer_V8.md`), (Core business plan for schema inspiration and future ingestion).
-   `DozerAI_Dev_Chat_History.txt`: (Document), (Located at `C:\Dozers\Docs\DozerAI_Dev_Chat_History.txt`), (Our development chat history for schema inspiration and future ingestion).

**Any Additional Updates Needed to the Project (DozerAI/App) Due to This Implementation?**
-   A `.env` file will be created in `C:\Dozers\DozerAI_Code\config\` and added to `.gitignore`.
-   The `project_structure.md` will be confirmed to include this `config/.env` path.

**DozerAI/App Project/File Structure Update Needed:** Yes.
    - Create directory: `C:\Dozers\DozerAI_Code\config\`
    - Create file: `C:\Dozers\DozerAI_Code\config\.env`
    - Create directory: `C:\Dozers\DozerAI_Code\scripts\db_schemas\`
    - The SQL DDL scripts will be created in `C:\Dozers\DozerAI_Code\scripts\db_schemas\`.

**Any Additional Updates Needed to the DozerAI Guide for Changes or Explanation?**
-   No, this entry is the primary explanation.

**Any Removals from the DozerAI Guide Needed?**
-   None.

**Effect on DozerAI/App Project Timeline:**
-   No change; this is Day 1 as planned.

**Integration Plan (for DozerAI/App):**
-   **When:** Day 1 (Week 1) – Foundational database setup.
-   **Where:** Supabase Cloud platform, local configuration files.
-   **Dependencies (Software):** Web browser (for Supabase UI), Text editor (for `.env` and SQL scripts).
-   **Setup Instructions (Summary):** Anthony creates Supabase project and populates `.env`. DozerAI_Builder provides SQL schemas. Anthony executes SQL in Supabase Studio.

**Recommended Tools (for DozerAI/App):**
-   Supabase Studio (SQL Editor within Supabase dashboard).
-   Text Editor (VS Code, Notepad++, etc.) for `.env` and local SQL script files.

---
**Tasks for Anthony Pierce (CEO):**

1.  **Sign Up/Log In to Supabase:**
    *   Go to [supabase.com](https://supabase.com).
    *   If you don't have an account, sign up for a free tier account.
    *   If you have an account, log in.
2.  **Create a New Supabase Project for DozerAI ("The Kennel"):**
    *   In the Supabase dashboard, create a new project.
    *   Name it something like `dozerai-kennel` or `dozers-business-db`.
    *   Choose a strong database password (save this securely, you'll need it for the `.env` file).
    *   Select the region closest to your anticipated user base or your location (e.g., US East).
    *   Wait for the project to be provisioned.
3.  **Gather Supabase Project Credentials:**
    *   Once the project is ready, navigate to `Project Settings` (usually a gear icon).
    *   Go to `API`.
    *   Note down the following (DO NOT share these publicly or commit them to Git):
        *   **Project URL** (looks like `https://<your-project-ref>.supabase.co`)
        *   **Project API Key (anon public key)** (this one is safe to expose in frontend clients)
        *   **Project API Key (service_role secret key)** (this one is highly confidential, for backend use only)
4.  **Create and Populate `.env` File:**
    *   Navigate to `C:\Dozers\DozerAI_Code\config\` in your file explorer.
    *   Create a new file named `.env`.
    *   Open `.env` in a text editor and add the following lines, replacing placeholders with your actual Supabase credentials, Google API key, and Langfuse keys (get these from your accounts if you haven't already; placeholders for others for now):
        ```env
        # Supabase Configuration
        SUPABASE_URL="YOUR_SUPABASE_PROJECT_URL"
        SUPABASE_ANON_KEY="YOUR_SUPABASE_ANON_PUBLIC_KEY"
        SUPABASE_SERVICE_ROLE_KEY="YOUR_SUPABASE_SERVICE_ROLE_SECRET_KEY"
        SUPABASE_DB_PASSWORD="YOUR_CHOSEN_DATABASE_PASSWORD_DURING_PROJECT_SETUP"

        # LLM API Keys
        GOOGLE_API_KEY="YOUR_GOOGLE_AI_STUDIO_API_KEY"
        OPENAI_API_KEY="YOUR_OPENAI_API_KEY_IF_ANY_OR_LEAVE_BLANK"
        ANTHROPIC_API_KEY="YOUR_ANTHROPIC_API_KEY_IF_ANY_OR_LEAVE_BLANK"
        OPENROUTER_API_KEY="YOUR_OPENROUTER_API_KEY_IF_ANY_OR_LEAVE_BLANK" # FYI

        # Observability
        LANGFUSE_PUBLIC_KEY="YOUR_LANGFUSE_PUBLIC_KEY"
        LANGFUSE_SECRET_KEY="YOUR_LANGFUSE_SECRET_KEY"
        LANGFUSE_HOST="https://cloud.langfuse.com" # Or your self-hosted URL

        # External Services
        ELEVENLABS_API_KEY="YOUR_ELEVENLABS_API_KEY_IF_ANY_OR_LEAVE_BLANK"
        # Add other API keys as needed (e.g., for n8n to connect to external services)

        # n8n Self-Hosted Configuration (Placeholder until n8n setup on Day 2)
        N8N_WEBHOOK_URL_BASE="http://localhost:5678/webhook/" # Example, will be your self-hosted n8n URL
        N8N_API_KEY_DOZERAI_TRIGGER="YOUR_SECURE_N8N_API_KEY_FOR_DOZERAI_TO_USE" # You will generate this in n8n

        # Neo4j Configuration (Placeholder until Neo4j setup)
        NEO4J_URI="bolt://localhost:7687" # Example for local Docker
        NEO4J_USERNAME="neo4j"
        NEO4J_PASSWORD="YOUR_NEO4J_PASSWORD"

        # Application Settings
        PYTHON_BACKEND_PORT="8090" # As per project_structure.md for FastAPI/Uvicorn
        # Add any other global settings DozerAI might need
        ```
    *   **Save the `.env` file.**
    *   **CRITICAL:** Ensure `config/.env` is listed in your `C:\Dozers\DozerAI_Code\.gitignore` file (DozerAI_Builder will provide the content for `.gitignore` in a subsequent task for this day).
5.  **Enable `pgvector` Extension in Supabase:**
    *   In your Supabase project dashboard, go to `Database` -> `Extensions`.
    *   Search for `vector` and enable the `vector` extension. This is essential for storing AI embeddings.
6.  **Create SQL Schema Files:**
    *   In `C:\Dozers\DozerAI_Code\scripts\db_schemas\`, create the following empty SQL files (DozerAI_Builder will provide their content next):
        *   `001_initial_core_tables.sql`
        *   `002_users_roles_permissions.sql`
        *   `003_documents_chunks_embeddings.sql`
        *   `004_app_messenger_tables.sql`
        *   `005_app_tasks_tables.sql`
        *   `006_app_time_clock_tables.sql`
        *   `007_app_meeting_notes_tables.sql`
        *   `008_app_suggestions_tables.sql`
7.  **Execute SQL Schemas in Supabase Studio:**
    *   Wait for DozerAI_Builder to provide the SQL content for the files created in the previous step.
    *   Once provided, open your Supabase project dashboard.
    *   Navigate to the `SQL Editor`.
    *   Click `+ New query`.
    *   Copy the content of `001_initial_core_tables.sql` into the editor and click `RUN`. Verify success.
    *   Repeat for `002` through `008` **IN ORDER**.
    *   **Notify DozerAI_Builder upon successful execution of all SQL scripts.**

---
**Tasks for DozerAI_Builder (CursorAI):**

1.  **Provide `.gitignore` Content:** Generate a comprehensive `.gitignore` file content suitable for a Python backend and a JavaScript/TypeScript frontend project (React/Vite/Electron), ensuring `config/.env`, `node_modules/`, `venv/`, `__pycache__/`, build artifacts, local data directories (`local_mem0_cache/`, `local_graphiti_db/`, `local_neo4j_data/`), and OS-specific files are ignored. Present this for Anthony to save as `C:\Dozers\DozerAI_Code\.gitignore`.
2.  **Generate SQL Schema DDL - `001_initial_core_tables.sql`:**
    *   Create SQL DDL (Data Definition Language) for foundational tables that might not fit into other specific categories but are needed early. For now, this might just include enabling `uuid-ossp` if not already enabled by Supabase default, and a placeholder table for `project_settings` or `app_configuration` if we anticipate needing one.
    *   Focus on PostgreSQL syntax compatible with Supabase. Include primary keys, appropriate data types, and `NOT NULL` constraints where necessary. Add comments explaining each table and key columns.
    ```sql
    -- SQL for 001_initial_core_tables.sql
    -- Enable UUID generation if not already enabled (Supabase usually has this)
    CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

    -- Placeholder for general application or project-level settings, if needed later.
    -- For now, most settings will be in config/.env or config/settings.toml
    -- CREATE TABLE IF NOT EXISTS app_global_settings (
    --     setting_key TEXT PRIMARY KEY,
    --     setting_value JSONB,
    --     description TEXT,
    --     last_updated_at TIMESTAMPTZ DEFAULT now()
    -- );
    -- COMMENT ON TABLE app_global_settings IS 'Stores global configuration settings for DozerAI and App Suite if not covered by .env/settings.toml.';

    -- You can add other truly core, miscellaneous tables here if identified.
    -- For now, enabling uuid-ossp is the main action if needed. Supabase projects often have it pre-enabled.
    SELECT '001_initial_core_tables.sql executed successfully' AS status;
    ```
3.  **Generate SQL Schema DDL - `002_users_roles_permissions.sql`:**
    *   Create SQL DDL for `roles`, `users` (linking to Supabase Auth users via UUID), and a `user_roles` join table. Also, a `permissions` table and a `role_permissions` join table.
    *   `roles`: `id (SERIAL PK)`, `role_name (TEXT UNIQUE NOT NULL, e.g., 'CEO', 'Manager', 'BarkRanger', 'Chef')`, `description (TEXT)`.
    *   `users`: `id (UUID PK, references auth.users(id) ON DELETE CASCADE)`, `full_name (TEXT)`, `email (TEXT UNIQUE)`, `employee_id (TEXT UNIQUE, nullable)`, `created_at (TIMESTAMPTZ DEFAULT now())`, `updated_at (TIMESTAMPTZ DEFAULT now())`.
    *   `user_roles`: `user_id (UUID FK references users(id))`, `role_id (INT FK references roles(id))`, `PRIMARY KEY (user_id, role_id)`.
    *   `permissions`: `id (SERIAL PK)`, `permission_name (TEXT UNIQUE NOT NULL, e.g., 'view_financial_reports', 'edit_schedules', 'approve_time_off', 'access_all_kennel_data')`, `description (TEXT)`.
    *   `role_permissions`: `role_id (INT FK references roles(id))`, `permission_id (INT FK references permissions(id))`, `PRIMARY KEY (role_id, permission_id)`.
    *   Include comments.
    ```sql
    -- SQL for 002_users_roles_permissions.sql

    -- Roles Table: Defines different job roles within Dozer's Business
    CREATE TABLE IF NOT EXISTS roles (
        id SERIAL PRIMARY KEY,
        role_name TEXT UNIQUE NOT NULL,
        description TEXT,
        created_at TIMESTAMPTZ DEFAULT now(),
        updated_at TIMESTAMPTZ DEFAULT now()
    );
    COMMENT ON TABLE roles IS 'Defines different job roles within Dozer''s Business (e.g., CEO, Manager, BarkRanger).';

    -- Users Table: Stores additional information for authenticated users, linking to Supabase auth.users
    -- The actual user authentication is handled by Supabase Auth. This table stores app-specific user details.
    CREATE TABLE IF NOT EXISTS users (
        id UUID PRIMARY KEY REFERENCES auth.users(id) ON DELETE CASCADE, -- Links to Supabase auth.users table
        full_name TEXT,
        -- Email is already in auth.users, but can be denormalized here if frequently needed by app logic not hitting auth schema.
        -- For simplicity, we'll assume email is primarily fetched from auth.users or passed with JWT.
        -- email TEXT UNIQUE, 
        employee_id TEXT UNIQUE, -- Optional: For internal employee identification
        job_title TEXT, -- Free-text job title, can complement roles
        profile_picture_url TEXT, -- URL to user's profile picture
        created_at TIMESTAMPTZ DEFAULT now(),
        updated_at TIMESTAMPTZ DEFAULT now()
    );
    COMMENT ON TABLE users IS 'Stores application-specific profile information for users, linked to Supabase auth.users.';

    -- User_Roles Junction Table: Assigns users to one or more roles
    CREATE TABLE IF NOT EXISTS user_roles (
        user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
        role_id INTEGER NOT NULL REFERENCES roles(id) ON DELETE CASCADE,
        assigned_at TIMESTAMPTZ DEFAULT now(),
        PRIMARY KEY (user_id, role_id) -- Ensures a user has a role only once
    );
    COMMENT ON TABLE user_roles IS 'Junction table mapping users to their assigned roles.';

    -- Permissions Table: Defines specific actions or access rights within the system
    CREATE TABLE IF NOT EXISTS permissions (
        id SERIAL PRIMARY KEY,
        permission_name TEXT UNIQUE NOT NULL, -- e.g., 'view_financial_reports', 'edit_employee_schedules', 'approve_time_off_requests'
        description TEXT,
        created_at TIMESTAMPTZ DEFAULT now()
    );
    COMMENT ON TABLE permissions IS 'Defines specific granular permissions within the DozerAI system and App Suite.';

    -- Role_Permissions Junction Table: Assigns permissions to roles
    CREATE TABLE IF NOT EXISTS role_permissions (
        role_id INTEGER NOT NULL REFERENCES roles(id) ON DELETE CASCADE,
        permission_id INTEGER NOT NULL REFERENCES permissions(id) ON DELETE CASCADE,
        assigned_at TIMESTAMPTZ DEFAULT now(),
        PRIMARY KEY (role_id, permission_id) -- Ensures a role has a permission only once
    );
    COMMENT ON TABLE role_permissions IS 'Junction table mapping roles to their granted permissions.';

    -- Trigger function to automatically update 'updated_at' columns
    CREATE OR REPLACE FUNCTION trigger_set_timestamp()
    RETURNS TRIGGER AS $$
    BEGIN
      NEW.updated_at = NOW();
      RETURN NEW;
    END;
    $$ LANGUAGE plpgsql;

    -- Apply the trigger to tables with 'updated_at'
    CREATE TRIGGER set_timestamp_roles
    BEFORE UPDATE ON roles
    FOR EACH ROW
    EXECUTE PROCEDURE trigger_set_timestamp();

    CREATE TRIGGER set_timestamp_users
    BEFORE UPDATE ON users
    FOR EACH ROW
    EXECUTE PROCEDURE trigger_set_timestamp();

    -- Seed some initial roles (CEO will be assigned manually to Anthony's Supabase Auth user ID later)
    INSERT INTO roles (role_name, description) VALUES
        ('CEO', 'Chief Executive Officer, full system access.'),
        ('Manager', 'General management responsibilities.'),
        ('PackLeaderAgent', 'AI Department Lead Sub-Agent (System Role)'),
        ('PackMemberAgent', 'AI Employee Assistant (System Role)'),
        ('Unassigned', 'Default role for new users until properly assigned.')
    ON CONFLICT (role_name) DO NOTHING;

    SELECT '002_users_roles_permissions.sql executed successfully' AS status;
    ```
4.  **Generate SQL Schema DDL - `003_documents_chunks_embeddings.sql`:**
    *   Create SQL DDL for `documents` (source_uri, type, full_text, metadata JSONB, access_permissions JSONB for RBAC tags), `document_chunks` (document_id FK, chunk_text, chunk_sequence, metadata JSONB, contextual_summary TEXT), and `document_embeddings` (chunk_id FK, embedding VECTOR(1536) - assuming OpenAI `text-embedding-ada-002` or similar size from Google, model_name TEXT).
    *   Ensure `pgvector` is enabled (Anthony's task) before this script is run.
    *   Include comments.
    ```sql
    -- SQL for 003_documents_chunks_embeddings.sql
    -- Assumes 'vector' extension is enabled: CREATE EXTENSION IF NOT EXISTS vector; (Anthony's task)

    -- Documents Table: Stores source documents for "The Kennel"
    CREATE TABLE IF NOT EXISTS documents (
        id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
        source_uri TEXT UNIQUE NOT NULL, -- e.g., file path, URL, internal ID for 'Dozer's Blueprint V8.0'
        document_type TEXT NOT NULL, -- e.g., 'business_plan', 'chat_history', 'sop', 'tax_code', 'website_scrape'
        full_text_content TEXT, -- Can be NULL if content is too large and stored elsewhere, or for parent docs
        title TEXT,
        metadata JSONB, -- Original filename, author, creation date, version, etc.
        -- RBAC tags: array of role_ids or permission_names that can access this document
        -- Example: '{"roles":, "permissions": ["view_all_sops"]}'
        -- This will be used by backend logic in conjunction with Supabase RLS
        access_tags JSONB, 
        ingested_at TIMESTAMPTZ DEFAULT now(),
        last_updated_at TIMESTAMPTZ DEFAULT now(),
        content_hash TEXT -- MD5 or SHA256 hash of the content to detect changes
    );
    COMMENT ON TABLE documents IS 'Stores source documents (Blueprint, SOPs, chat history, web scrapes, etc.) for The Kennel.';
    CREATE INDEX IF NOT EXISTS idx_documents_type ON documents(document_type);
    CREATE INDEX IF NOT EXISTS idx_documents_source_uri ON documents(source_uri);

    -- Document_Chunks Table: Stores processed text chunks from documents
    CREATE TABLE IF NOT EXISTS document_chunks (
        id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
        document_id UUID NOT NULL REFERENCES documents(id) ON DELETE CASCADE,
        chunk_text TEXT NOT NULL,
        chunk_sequence INTEGER NOT NULL, -- Order of the chunk within the document
        contextual_summary TEXT, -- Generated by Anthropic Contextual Retrieval method
        metadata JSONB, -- e.g., page number, section header
        created_at TIMESTAMPTZ DEFAULT now(),
        UNIQUE (document_id, chunk_sequence)
    );
    COMMENT ON TABLE document_chunks IS 'Stores processed text chunks from documents, ready for embedding, including contextual summaries.';
    CREATE INDEX IF NOT EXISTS idx_chunks_document_id ON document_chunks(document_id);

    -- Document_Embeddings Table: Stores vector embeddings for document chunks
    -- Embedding dimension depends on the model used (e.g., OpenAI ada-002 is 1536, Google's might differ)
    -- We will use 768 as a common dimension for many sentence-transformer models or some Google models for flexibility.
    -- This can be adjusted when specific embedding model is finalized for non-OpenAI.
    -- For Gemini text-embedding-004, it's 768.
    CREATE TABLE IF NOT EXISTS document_embeddings (
        id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
        chunk_id UUID NOT NULL REFERENCES document_chunks(id) ON DELETE CASCADE UNIQUE, -- Ensures one embedding per chunk
        embedding VECTOR(768) NOT NULL, -- Dimension for Gemini text-embedding-004 (or other chosen model)
        embedding_model_name TEXT NOT NULL, -- e.g., 'google-text-embedding-004', 'openai-text-embedding-ada-002'
        created_at TIMESTAMPTZ DEFAULT now()
    );
    COMMENT ON TABLE document_embeddings IS 'Stores vector embeddings for document chunks, enabling semantic search.';
    CREATE INDEX IF NOT EXISTS idx_embeddings_chunk_id ON document_embeddings(chunk_id);

    -- Create an HNSW index for fast similarity search on embeddings
    -- USING hnsw (embedding vector_l2_ops) - l2_ops for Euclidean distance
    -- This needs to be created AFTER pgvector is enabled and table has some data, or may error.
    -- Or create it now and it will be used once data is populated.
    -- For optimal performance, m and ef_construction parameters might need tuning based on dataset size.
    -- CREATE INDEX IF NOT EXISTS idx_hnsw_document_embeddings ON document_embeddings USING hnsw (embedding vector_l2_ops);

    -- Trigger function to automatically update 'last_updated_at' on documents table
    CREATE TRIGGER set_timestamp_documents
    BEFORE UPDATE ON documents
    FOR EACH ROW
    EXECUTE PROCEDURE trigger_set_timestamp(); -- Assumes trigger_set_timestamp() created in 002

    SELECT '003_documents_chunks_embeddings.sql executed successfully' AS status;
    ```
5.  **Generate SQL Schema DDL - `004_app_messenger_tables.sql`:**
    *   Create SQL DDL for `chat_channels` (id, name, description, type ENUM('PUBLIC_CHANNEL', 'PRIVATE_GROUP', 'DIRECT_MESSAGE'), created_by_user_id FK), `channel_members` (channel_id FK, user_id FK, joined_at), `messages` (id, channel_id FK, sender_user_id FK, content_text, sent_at, metadata JSONB for reactions/threads).
    *   Enable RLS on these tables.
    *   Include comments.
    ```sql
    -- SQL for 004_app_messenger_tables.sql

    -- Chat Channels Table: Stores information about different chat channels or direct message threads
    CREATE TYPE channel_type AS ENUM ('PUBLIC_CHANNEL', 'PRIVATE_GROUP', 'DIRECT_MESSAGE');
    CREATE TABLE IF NOT EXISTS chat_channels (
        id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
        channel_name TEXT, -- Can be NULL for direct messages, or derived from participant names
        description TEXT,
        channel_type channel_type NOT NULL,
        created_by_user_id UUID REFERENCES users(id) ON DELETE SET NULL, -- User who initiated the channel/DM
        created_at TIMESTAMPTZ DEFAULT now(),
        updated_at TIMESTAMPTZ DEFAULT now()
    );
    COMMENT ON TABLE chat_channels IS 'Stores chat channels, private groups, or direct message threads for the App Suite messenger.';
    CREATE INDEX IF NOT EXISTS idx_chat_channels_type ON chat_channels(channel_type);

    -- Channel Members Junction Table: Maps users to the channels they are part of
    CREATE TABLE IF NOT EXISTS channel_members (
        channel_id UUID NOT NULL REFERENCES chat_channels(id) ON DELETE CASCADE,
        user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
        joined_at TIMESTAMPTZ DEFAULT now(),
        last_read_at TIMESTAMPTZ, -- For unread message indicators
        notifications_enabled BOOLEAN DEFAULT TRUE,
        PRIMARY KEY (channel_id, user_id)
    );
    COMMENT ON TABLE channel_members IS 'Maps users to chat channels they belong to, with join date and read status.';

    -- Messages Table: Stores individual chat messages
    CREATE TABLE IF NOT EXISTS messages (
        id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
        channel_id UUID NOT NULL REFERENCES chat_channels(id) ON DELETE CASCADE,
        sender_user_id UUID REFERENCES users(id) ON DELETE SET NULL, -- Can be NULL for system messages
        content_text TEXT NOT NULL,
        sent_at TIMESTAMPTZ DEFAULT now(),
        updated_at TIMESTAMPTZ, -- For edited messages
        metadata JSONB -- For reactions, threads parent_message_id, read receipts, message type (text, image_url, file_url)
                       -- e.g., '{"reactions": {"👍": ["user_uuid1", "user_uuid2"]}, "thread_parent_id": "message_uuid_parent"}'
    );
    COMMENT ON TABLE messages IS 'Stores individual chat messages within channels/DMs.';
    CREATE INDEX IF NOT EXISTS idx_messages_channel_id_sent_at ON messages(channel_id, sent_at DESC);
    CREATE INDEX IF NOT EXISTS idx_messages_sender_user_id ON messages(sender_user_id);

    -- Apply the trigger to tables with 'updated_at'
    CREATE TRIGGER set_timestamp_chat_channels
    BEFORE UPDATE ON chat_channels
    FOR EACH ROW
    EXECUTE PROCEDURE trigger_set_timestamp(); -- Assumes trigger_set_timestamp() created in 002

    CREATE TRIGGER set_timestamp_messages_updated
    BEFORE UPDATE ON messages
    FOR EACH ROW
    EXECUTE PROCEDURE trigger_set_timestamp();

    -- Enable Row Level Security (RLS) for messenger tables
    ALTER TABLE chat_channels ENABLE ROW LEVEL SECURITY;
    ALTER TABLE channel_members ENABLE ROW LEVEL SECURITY;
    ALTER TABLE messages ENABLE ROW LEVEL SECURITY;

    -- RLS Policies (Examples - to be refined based on detailed app logic)
    -- Users can see channels they are members of.
    CREATE POLICY "Users can see their own channels" ON chat_channels
        FOR SELECT USING (
            EXISTS (
                SELECT 1 FROM channel_members
                WHERE channel_members.channel_id = chat_channels.id
                AND channel_members.user_id = auth.uid()
            ) OR channel_type = 'PUBLIC_CHANNEL' -- Or if it's a public channel (if we add this concept later)
        );
    
    -- Users can manage channels they created (simplified, needs more granular control for adding members etc.)
    CREATE POLICY "Users can manage channels they created" ON chat_channels
        FOR ALL USING (created_by_user_id = auth.uid())
        WITH CHECK (created_by_user_id = auth.uid());

    -- Users can see their own channel memberships.
    CREATE POLICY "Users can see their own channel memberships" ON channel_members
        FOR SELECT USING (user_id = auth.uid());
    CREATE POLICY "Channel creators/admins can manage memberships" ON channel_members -- TODO: More complex policy needed
        FOR ALL USING (
            EXISTS (
                SELECT 1 FROM chat_channels
                WHERE chat_channels.id = channel_members.channel_id AND chat_channels.created_by_user_id = auth.uid()
            )
        );

    -- Users can see messages in channels they are members of.
    CREATE POLICY "Users can see messages in their channels" ON messages
        FOR SELECT USING (
            EXISTS (
                SELECT 1 FROM channel_members
                WHERE channel_members.channel_id = messages.channel_id
                AND channel_members.user_id = auth.uid()
            )
        );

    -- Users can insert messages into channels they are members of.
    CREATE POLICY "Users can insert messages in their channels" ON messages
        FOR INSERT WITH CHECK (
            EXISTS (
                SELECT 1 FROM channel_members
                WHERE channel_members.channel_id = messages.channel_id
                AND channel_members.user_id = auth.uid()
            ) AND sender_user_id = auth.uid() -- Ensure sender is the authenticated user
        );

    -- Users can only update/delete their own messages (simplified)
    CREATE POLICY "Users can update_delete their own messages" ON messages
        FOR UPDATE USING (sender_user_id = auth.uid())
        WITH CHECK (sender_user_id = auth.uid());
    CREATE POLICY "Users can delete their own messages" ON messages
        FOR DELETE USING (sender_user_id = auth.uid());
        
    -- Ensure Supabase Realtime is enabled on these tables via the Supabase Dashboard
    -- (Database -> Replication -> Source -> Add tables to publication)

    SELECT '004_app_messenger_tables.sql executed successfully' AS status;
    ```
6.  **Generate SQL Schema DDL - `005_app_tasks_tables.sql`:**
    *   Create SQL DDL for `projects` (id, name, description, owner_user_id FK), `tasks` (id, project_id FK, title, description, status ENUM('TODO', 'IN_PROGRESS', 'DONE', 'BLOCKED'), priority ENUM, due_date, assigned_to_user_id FK, created_by_user_id FK), `task_dependencies` (task_id FK, depends_on_task_id FK), `task_signoffs` (task_id FK, signed_off_by_user_id FK, signed_off_at, comments).
    *   Enable RLS. Include comments.
    ```sql
    -- SQL for 005_app_tasks_tables.sql

    -- Projects Table: To group tasks
    CREATE TABLE IF NOT EXISTS projects (
        id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
        project_name TEXT NOT NULL,
        description TEXT,
        owner_user_id UUID REFERENCES users(id) ON DELETE SET NULL,
        status TEXT DEFAULT 'Active', -- e.g., Active, Completed, On Hold
        created_at TIMESTAMPTZ DEFAULT now(),
        updated_at TIMESTAMPTZ DEFAULT now()
    );
    COMMENT ON TABLE projects IS 'Stores projects to logically group tasks within the App Suite.';

    -- Tasks Table: Core table for task management
    CREATE TYPE task_status AS ENUM ('TODO', 'IN_PROGRESS', 'REVIEW', 'DONE', 'BLOCKED', 'CANCELLED');
    CREATE TYPE task_priority AS ENUM ('LOW', 'MEDIUM', 'HIGH', 'URGENT');

    CREATE TABLE IF NOT EXISTS tasks (
        id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
        project_id UUID REFERENCES projects(id) ON DELETE SET NULL, -- Tasks can be unassigned to a project
        title TEXT NOT NULL,
        description TEXT,
        status task_status DEFAULT 'TODO',
        priority task_priority DEFAULT 'MEDIUM',
        due_date DATE,
        assigned_to_user_id UUID REFERENCES users(id) ON DELETE SET NULL,
        created_by_user_id UUID REFERENCES users(id) ON DELETE SET NULL,
        created_at TIMESTAMPTZ DEFAULT now(),
        updated_at TIMESTAMPTZ DEFAULT now(),
        completed_at TIMESTAMPTZ
    );
    COMMENT ON TABLE tasks IS 'Stores individual tasks, their status, priority, assignee, etc.';
    CREATE INDEX IF NOT EXISTS idx_tasks_project_id ON tasks(project_id);
    CREATE INDEX IF NOT EXISTS idx_tasks_assigned_to ON tasks(assigned_to_user_id);
    CREATE INDEX IF NOT EXISTS idx_tasks_status ON tasks(status);

    -- Task Dependencies Table: For linking tasks that depend on others
    CREATE TABLE IF NOT EXISTS task_dependencies (
        task_id UUID NOT NULL REFERENCES tasks(id) ON DELETE CASCADE,
        depends_on_task_id UUID NOT NULL REFERENCES tasks(id) ON DELETE CASCADE,
        created_at TIMESTAMPTZ DEFAULT now(),
        PRIMARY KEY (task_id, depends_on_task_id),
        CHECK (task_id <> depends_on_task_id) -- Prevent self-dependency
    );
    COMMENT ON TABLE task_dependencies IS 'Defines dependencies between tasks (e.g., Task A must complete before Task B).';

    -- Task Signoffs Table: For employees to formally sign off on task completion
    CREATE TABLE IF NOT EXISTS task_signoffs (
        id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
        task_id UUID NOT NULL REFERENCES tasks(id) ON DELETE CASCADE,
        signed_off_by_user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
        signed_off_at TIMESTAMPTZ DEFAULT now(),
        comments TEXT, -- Optional comments by the person signing off
        manager_approved_at TIMESTAMPTZ, -- Optional: if manager approval is a second step
        manager_approver_id UUID REFERENCES users(id) ON DELETE SET NULL
    );
    COMMENT ON TABLE task_signoffs IS 'Records employee sign-offs for completed tasks, with optional manager approval step.';
    CREATE INDEX IF NOT EXISTS idx_task_signoffs_task_id ON task_signoffs(task_id);

    -- Apply triggers for 'updated_at'
    CREATE TRIGGER set_timestamp_projects
    BEFORE UPDATE ON projects
    FOR EACH ROW
    EXECUTE PROCEDURE trigger_set_timestamp();

    CREATE TRIGGER set_timestamp_tasks
    BEFORE UPDATE ON tasks
    FOR EACH ROW
    EXECUTE PROCEDURE trigger_set_timestamp();
    
    -- Enable RLS for task tables
    ALTER TABLE projects ENABLE ROW LEVEL SECURITY;
    ALTER TABLE tasks ENABLE ROW LEVEL SECURITY;
    ALTER TABLE task_dependencies ENABLE ROW LEVEL SECURITY;
    ALTER TABLE task_signoffs ENABLE ROW LEVEL SECURITY;

    -- RLS Policies (Examples - to be refined with detailed app logic and roles/permissions from table 002)
    -- Users can see projects they own or are associated with via tasks.
    CREATE POLICY "Users can view relevant projects" ON projects
        FOR SELECT USING (
            owner_user_id = auth.uid() OR
            EXISTS (
                SELECT 1 FROM tasks
                WHERE tasks.project_id = projects.id AND (tasks.assigned_to_user_id = auth.uid() OR tasks.created_by_user_id = auth.uid())
            )
            -- Or based on a project_members table if we add one
        );
    CREATE POLICY "Project owners can manage their projects" ON projects
        FOR ALL USING (owner_user_id = auth.uid())
        WITH CHECK (owner_user_id = auth.uid());

    -- Users can see tasks assigned to them, created by them, or in projects they have access to.
    CREATE POLICY "Users can view relevant tasks" ON tasks
        FOR SELECT USING (
            assigned_to_user_id = auth.uid() OR
            created_by_user_id = auth.uid() OR
            (project_id IS NOT NULL AND EXISTS (
                SELECT 1 FROM projects
                WHERE projects.id = tasks.project_id -- Implicitly uses project's RLS
            )) OR
            (project_id IS NULL) -- Or if task is not tied to a project (e.g. personal tasks)
        );
    CREATE POLICY "Users can manage tasks they created or are assigned to" ON tasks
        FOR ALL USING (assigned_to_user_id = auth.uid() OR created_by_user_id = auth.uid())
        WITH CHECK (assigned_to_user_id = auth.uid() OR created_by_user_id = auth.uid());

    -- Assuming if a user can see a task, they can see its dependencies and signoffs. More granular policies can be added.
    CREATE POLICY "Users can view dependencies of accessible tasks" ON task_dependencies
        FOR SELECT USING (
            EXISTS (SELECT 1 FROM tasks WHERE tasks.id = task_dependencies.task_id) -- Checks RLS on tasks table
        );
    CREATE POLICY "Users can manage dependencies of tasks they manage" ON task_dependencies
        FOR ALL USING (
             EXISTS (SELECT 1 FROM tasks WHERE tasks.id = task_dependencies.task_id AND (tasks.assigned_to_user_id = auth.uid() OR tasks.created_by_user_id = auth.uid()))
        );


    CREATE POLICY "Users can view signoffs of accessible tasks" ON task_signoffs
        FOR SELECT USING (
            EXISTS (SELECT 1 FROM tasks WHERE tasks.id = task_signoffs.task_id) -- Checks RLS on tasks table
        );
    CREATE POLICY "Assigned users or creators can sign off on tasks" ON task_signoffs
        FOR INSERT WITH CHECK (
            signed_off_by_user_id = auth.uid() AND
            EXISTS (SELECT 1 FROM tasks WHERE tasks.id = task_signoffs.task_id AND (tasks.assigned_to_user_id = auth.uid() OR tasks.created_by_user_id = auth.uid()))
        );
    CREATE POLICY "Users can manage their own signoffs" ON task_signoffs
        FOR UPDATE USING (signed_off_by_user_id = auth.uid())
        WITH CHECK (signed_off_by_user_id = auth.uid());
    CREATE POLICY "Users can delete their own signoffs" ON task_signoffs
        FOR DELETE USING (signed_off_by_user_id = auth.uid());

    SELECT '005_app_tasks_tables.sql executed successfully' AS status;
    ```
7.  **Generate SQL Schema DDL - `006_app_time_clock_tables.sql`:**
    *   Create SQL DDL for `time_clock_entries` (id, user_id FK, clock_in_at TIMESTAMPTZ, clock_out_at TIMESTAMPTZ, clock_in_method ENUM('APP_MANUAL', 'RFID_TERMINAL', 'APP_AUTO_LOCATION', 'MANUAL_CORRECTION'), clock_out_method ENUM, location_data_geo JSONB (for app based), rfid_tag_id TEXT (for rfid), notes TEXT).
    *   Enable RLS. Include comments.
    ```sql
    -- SQL for 006_app_time_clock_tables.sql

    CREATE TYPE clock_method AS ENUM ('APP_MANUAL', 'RFID_TERMINAL', 'APP_AUTO_LOCATION', 'MANUAL_CORRECTION_BY_MANAGER');

    CREATE TABLE IF NOT EXISTS time_clock_entries (
        id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
        user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
        clock_in_at TIMESTAMPTZ NOT NULL DEFAULT now(),
        clock_out_at TIMESTAMPTZ,
        clock_in_method clock_method NOT NULL,
        clock_out_method clock_method,
        -- For app-based clock-ins, store GeoJSON Point: '{"type": "Point", "coordinates": [-longitude, latitude]}'
        clock_in_location_data JSONB, 
        clock_out_location_data JSONB,
        rfid_tag_id_in TEXT, -- If clocked in via RFID
        rfid_tag_id_out TEXT, -- If clocked out via RFID
        notes TEXT, -- For manual corrections or employee notes
        corrected_by_user_id UUID REFERENCES users(id) ON DELETE SET NULL, -- If a manager corrected this entry
        original_entry_id UUID REFERENCES time_clock_entries(id) ON DELETE SET NULL, -- If this is a correction of a previous entry
        created_at TIMESTAMPTZ DEFAULT now(),
        updated_at TIMESTAMPTZ DEFAULT now()
    );
    COMMENT ON TABLE time_clock_entries IS 'Stores employee clock-in and clock-out events for time tracking.';
    CREATE INDEX IF NOT EXISTS idx_time_clock_entries_user_id_clock_in_at ON time_clock_entries(user_id, clock_in_at DESC);

    -- Apply trigger for 'updated_at'
    CREATE TRIGGER set_timestamp_time_clock_entries
    BEFORE UPDATE ON time_clock_entries
    FOR EACH ROW
    EXECUTE PROCEDURE trigger_set_timestamp();

    -- Enable RLS
    ALTER TABLE time_clock_entries ENABLE ROW LEVEL SECURITY;

    -- RLS Policies
    -- Users can see and manage their own time clock entries.
    CREATE POLICY "Users can manage their own time entries" ON time_clock_entries
        FOR ALL USING (user_id = auth.uid())
        WITH CHECK (user_id = auth.uid());

    -- Managers can see time clock entries of users they manage (requires a 'manager_employee_map' table or similar hierarchy logic)
    -- Placeholder: A user with 'view_all_time_entries' permission (defined in 002 script) can see all.
    CREATE POLICY "Managers can view all time entries" ON time_clock_entries
        FOR SELECT USING (
            EXISTS (
                SELECT 1
                FROM user_roles ur
                JOIN roles r ON ur.role_id = r.id
                JOIN role_permissions rp ON r.id = rp.role_id
                JOIN permissions p ON rp.permission_id = p.id
                WHERE ur.user_id = auth.uid() AND p.permission_name = 'view_all_time_entries' 
            )
        );
    -- Managers can insert/update time entries if they have 'manage_all_time_entries' permission
    CREATE POLICY "Managers can manage all time entries" ON time_clock_entries
        FOR ALL USING ( -- Simplified, typically insert/update/delete would be more granular
            EXISTS (
                SELECT 1
                FROM user_roles ur
                JOIN roles r ON ur.role_id = r.id
                JOIN role_permissions rp ON r.id = rp.role_id
                JOIN permissions p ON rp.permission_id = p.id
                WHERE ur.user_id = auth.uid() AND p.permission_name = 'manage_all_time_entries' 
            )
        );


    SELECT '006_app_time_clock_tables.sql executed successfully' AS status;
    ```
8.  **Generate SQL Schema DDL - `007_app_meeting_notes_tables.sql`:**
    *   Create SQL DDL for `meetings` (id, title, start_time, end_time, created_by_user_id FK), `meeting_attendees` (meeting_id FK, user_id FK), `meeting_notes` (id, meeting_id FK, user_id_author FK, note_content TEXT, is_summary BOOLEAN), `meeting_recordings` (id, meeting_id FK, file_url_supabase_storage TEXT, transcript_text TEXT, transcript_status ENUM).
    *   Enable RLS. Include comments.
    ```sql
    -- SQL for 007_app_meeting_notes_tables.sql

    CREATE TABLE IF NOT EXISTS meetings (
        id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
        title TEXT NOT NULL,
        agenda TEXT,
        start_time TIMESTAMPTZ NOT NULL,
        end_time TIMESTAMPTZ,
        location_virtual_url TEXT, -- For online meetings
        location_physical TEXT, -- For in-person meetings
        created_by_user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
        created_at TIMESTAMPTZ DEFAULT now(),
        updated_at TIMESTAMPTZ DEFAULT now()
    );
    COMMENT ON TABLE meetings IS 'Stores information about scheduled or past meetings.';

    CREATE TABLE IF NOT EXISTS meeting_attendees (
        meeting_id UUID NOT NULL REFERENCES meetings(id) ON DELETE CASCADE,
        user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
        rsvp_status TEXT DEFAULT 'Pending', -- e.g., Pending, Accepted, Declined
        PRIMARY KEY (meeting_id, user_id)
    );
    COMMENT ON TABLE meeting_attendees IS 'Maps users (attendees) to meetings.';

    CREATE TABLE IF NOT EXISTS meeting_notes (
        id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
        meeting_id UUID NOT NULL REFERENCES meetings(id) ON DELETE CASCADE,
        user_id_author UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
        note_content TEXT NOT NULL,
        is_summary BOOLEAN DEFAULT FALSE, -- True if this note is an AI-generated summary
        is_action_items BOOLEAN DEFAULT FALSE, -- True if this note details action items
        created_at TIMESTAMPTZ DEFAULT now(),
        updated_at TIMESTAMPTZ DEFAULT now()
    );
    COMMENT ON TABLE meeting_notes IS 'Stores notes taken during or after meetings, or AI-generated summaries/action items.';
    CREATE INDEX IF NOT EXISTS idx_meeting_notes_meeting_id ON meeting_notes(meeting_id);

    CREATE TYPE transcript_process_status AS ENUM ('PENDING', 'PROCESSING', 'COMPLETED', 'FAILED');
    CREATE TABLE IF NOT EXISTS meeting_recordings (
        id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
        meeting_id UUID NOT NULL REFERENCES meetings(id) ON DELETE CASCADE,
        -- File stored in Supabase Storage, this is the path/key to it
        recording_file_path_supabase TEXT NOT NULL, 
        file_mime_type TEXT, -- e.g., 'audio/mp3', 'video/mp4'
        duration_seconds INTEGER,
        transcript_text TEXT, -- Full transcript generated by STT service
        transcript_status transcript_process_status DEFAULT 'PENDING',
        uploaded_by_user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
        uploaded_at TIMESTAMPTZ DEFAULT now()
    );
    COMMENT ON TABLE meeting_recordings IS 'Stores metadata about meeting recordings (audio/video) and their transcripts.';
    CREATE INDEX IF NOT EXISTS idx_meeting_recordings_meeting_id ON meeting_recordings(meeting_id);
    
    -- Apply triggers for 'updated_at'
    CREATE TRIGGER set_timestamp_meetings
    BEFORE UPDATE ON meetings
    FOR EACH ROW
    EXECUTE PROCEDURE trigger_set_timestamp();

    CREATE TRIGGER set_timestamp_meeting_notes
    BEFORE UPDATE ON meeting_notes
    FOR EACH ROW
    EXECUTE PROCEDURE trigger_set_timestamp();

    -- Enable RLS
    ALTER TABLE meetings ENABLE ROW LEVEL SECURITY;
    ALTER TABLE meeting_attendees ENABLE ROW LEVEL SECURITY;
    ALTER TABLE meeting_notes ENABLE ROW LEVEL SECURITY;
    ALTER TABLE meeting_recordings ENABLE ROW LEVEL SECURITY;

    -- RLS Policies (Examples)
    -- Users can see meetings they created or are invited to.
    CREATE POLICY "Users can view relevant meetings" ON meetings
        FOR SELECT USING (
            created_by_user_id = auth.uid() OR
            EXISTS (
                SELECT 1 FROM meeting_attendees ma
                WHERE ma.meeting_id = meetings.id AND ma.user_id = auth.uid()
            )
        );
    CREATE POLICY "Meeting creators can manage their meetings" ON meetings
        FOR ALL USING (created_by_user_id = auth.uid())
        WITH CHECK (created_by_user_id = auth.uid());

    -- Users can see their own attendance records. Meeting creators can manage attendees.
    CREATE POLICY "Users can see their own attendance" ON meeting_attendees
        FOR SELECT USING (user_id = auth.uid());
    CREATE POLICY "Meeting creators can manage attendees" ON meeting_attendees
        FOR ALL USING (
            EXISTS (
                SELECT 1 FROM meetings m
                WHERE m.id = meeting_attendees.meeting_id AND m.created_by_user_id = auth.uid()
            )
        );
        
    -- Users can see notes/recordings for meetings they have access to.
    CREATE POLICY "Users can view notes of accessible meetings" ON meeting_notes
        FOR SELECT USING (
            EXISTS (SELECT 1 FROM meetings m WHERE m.id = meeting_notes.meeting_id) -- Implicitly uses meeting RLS
        );
    CREATE POLICY "Attendees/Creators can add notes to meetings" ON meeting_notes
        FOR INSERT WITH CHECK (
            user_id_author = auth.uid() AND
            EXISTS (
                SELECT 1 FROM meeting_attendees ma
                WHERE ma.meeting_id = meeting_notes.meeting_id AND ma.user_id = auth.uid()
            )
        );
    CREATE POLICY "Note authors can edit their notes" ON meeting_notes
        FOR UPDATE USING (user_id_author = auth.uid())
        WITH CHECK (user_id_author = auth.uid());


    CREATE POLICY "Users can view recordings of accessible meetings" ON meeting_recordings
        FOR SELECT USING (
            EXISTS (SELECT 1 FROM meetings m WHERE m.id = meeting_recordings.meeting_id)
        );
    CREATE POLICY "Attendees/Creators can upload recordings" ON meeting_recordings
        FOR INSERT WITH CHECK (
            uploaded_by_user_id = auth.uid() AND
             EXISTS (
                SELECT 1 FROM meeting_attendees ma
                WHERE ma.meeting_id = meeting_recordings.meeting_id AND ma.user_id = auth.uid()
            )
        );

    SELECT '007_app_meeting_notes_tables.sql executed successfully' AS status;
    ```
9.  **Generate SQL Schema DDL - `008_app_suggestions_tables.sql`:**
    *   Create SQL DDL for `suggestions` (id, submitted_by_user_id FK (nullable for anonymous), title, description, category TEXT, status ENUM('NEW', 'UNDER_REVIEW', 'ACCEPTED', 'IMPLEMENTED', 'REJECTED'), submitted_at, anonymous BOOLEAN).
    *   Enable RLS. Include comments.
    ```sql
    -- SQL for 008_app_suggestions_tables.sql

    CREATE TYPE suggestion_status AS ENUM ('NEW', 'UNDER_REVIEW', 'PLANNED', 'IMPLEMENTED', 'REJECTED', 'DUPLICATE');

    CREATE TABLE IF NOT EXISTS suggestions (
        id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
        submitted_by_user_id UUID REFERENCES users(id) ON DELETE SET NULL, -- Nullable for anonymous suggestions
        is_anonymous BOOLEAN DEFAULT FALSE,
        title TEXT NOT NULL,
        description TEXT NOT NULL,
        category TEXT, -- e.g., 'Operations', 'Marketing', 'Employee Welfare', 'Tech Improvement'
        status suggestion_status DEFAULT 'NEW',
        submitted_at TIMESTAMPTZ DEFAULT now(),
        updated_at TIMESTAMPTZ DEFAULT now(),
        manager_notes TEXT, -- Notes from management reviewing the suggestion
        upvotes INTEGER DEFAULT 0
    );
    COMMENT ON TABLE suggestions IS 'Stores employee suggestions for business improvements.';
    CREATE INDEX IF NOT EXISTS idx_suggestions_status ON suggestions(status);
    CREATE INDEX IF NOT EXISTS idx_suggestions_category ON suggestions(category);

    CREATE TABLE IF NOT EXISTS suggestion_votes (
        suggestion_id UUID NOT NULL REFERENCES suggestions(id) ON DELETE CASCADE,
        user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
        voted_at TIMESTAMPTZ DEFAULT now(),
        PRIMARY KEY (suggestion_id, user_id) -- User can only vote once per suggestion
    );
    COMMENT ON TABLE suggestion_votes IS 'Tracks user upvotes for suggestions.';

    -- Apply trigger for 'updated_at'
    CREATE TRIGGER set_timestamp_suggestions
    BEFORE UPDATE ON suggestions
    FOR EACH ROW
    EXECUTE PROCEDURE trigger_set_timestamp();

    -- Enable RLS
    ALTER TABLE suggestions ENABLE ROW LEVEL SECURITY;
    ALTER TABLE suggestion_votes ENABLE ROW LEVEL SECURITY;

    -- RLS Policies
    -- All authenticated users can submit suggestions.
    CREATE POLICY "Users can submit suggestions" ON suggestions
        FOR INSERT WITH CHECK (is_anonymous = TRUE OR submitted_by_user_id = auth.uid());

    -- All authenticated users can view non-anonymous suggestions, or all suggestions if they have a specific permission.
    -- Or, all suggestions are viewable by all authenticated users by default for transparency. Let's go with that.
    CREATE POLICY "All authenticated users can view suggestions" ON suggestions
        FOR SELECT USING (auth.role() = 'authenticated');
        
    -- Users can update their own non-anonymous suggestions if status is 'NEW'.
    CREATE POLICY "Submitters can update their own new suggestions" ON suggestions
        FOR UPDATE USING (submitted_by_user_id = auth.uid() AND status = 'NEW')
        WITH CHECK (submitted_by_user_id = auth.uid() AND status = 'NEW');

    -- Managers/Admins can update any suggestion (status, manager_notes).
    CREATE POLICY "Managers can update all suggestions" ON suggestions
        FOR UPDATE USING (
            EXISTS (
                SELECT 1
                FROM user_roles ur
                JOIN roles r ON ur.role_id = r.id
                JOIN role_permissions rp ON r.id = rp.role_id
                JOIN permissions p ON rp.permission_id = p.id
                WHERE ur.user_id = auth.uid() AND p.permission_name = 'manage_suggestions' 
            )
        );
    
    -- Voting policies
    CREATE POLICY "Authenticated users can vote" ON suggestion_votes
        FOR INSERT WITH CHECK (user_id = auth.uid());
    CREATE POLICY "Authenticated users can view votes" ON suggestion_votes
        FOR SELECT USING (auth.role() = 'authenticated');
    CREATE POLICY "Users can retract their own vote" ON suggestion_votes
        FOR DELETE USING (user_id = auth.uid());

    SELECT '008_app_suggestions_tables.sql executed successfully' AS status;
    ```
10. **Log Completion in `rules_check.log`:**
    *   `Action: Starting Task for DozerAI/App: Day 1 - Kennel Foundation: Supabase Setup & "The Kennel" Initial Schema, Rules reviewed: Yes, Guides (Creation/Dev) consulted: Yes, Env verified: Yes, Sequence verified: Yes, Timestamp: [YYYY-MM-DD HH:MM:SS]`
11. **Request Anthony to Execute SQL and Confirm Completion:**
    *   "Anthony, I have provided the SQL DDL scripts for Day 1 in `C:\Dozers\DozerAI_Code\scripts\db_schemas\`. Please:
        1.  Ensure your `.env` file at `C:\Dozers\DozerAI_Code\config\.env` is populated with your Supabase Project URL, Anon Key, Service Role Key, and Database Password.
        2.  Ensure the `pgvector` extension is enabled in your Supabase project.
        3.  Execute the SQL scripts `001` through `008` **in order** using the Supabase SQL Editor.
        4.  Confirm successful execution of all scripts.
        5.  Also, please ensure you have saved our full chat history to `C:\Dozers\Docs\DozerAI_Dev_Chat_History.txt` and "Dozer's Blueprint V8.0" is at `C:\Dozers\Docs\Business_Plan_Dozer_V8.md`."

---
**Code for `.gitignore` (to be saved as `C:\Dozers\DozerAI_Code\.gitignore` by Anthony):**
```gitignore
# Python
__pycache__/
*.pyc
*.pyo
*.pyd
.Python
env/
venv/
ENV/
pip-freeze.txt
pip-selfcheck.json
*.egg-info/
.ipynb_checkpoints

# Node
node_modules/
dist/
build/
coverage/
*.log
npm-debug.log*
yarn-debug.log*
yarn-error.log*
package-lock.json # Often committed, but can be ignored in some workflows if package.json is source of truth
# Electron Forge specific build artifacts if not already covered by dist/ or build/
.webpack/
out/

# IDE / OS
.vscode/
.idea/
*.DS_Store
Thumbs.db

# Configuration & Secrets
config/.env
*.env
*.env.*
!*.env.example # Allow example env files

# Local Data (generated by DozerAI dev instance)
data/local_mem0_cache/
data/local_graphiti_db/
data/local_neo4j_data/
# Any other local database files if not using Docker volumes mapped outside project for these

# n8n self-hosted data (if data volume mapped inside project, usually mapped outside)
# n8n_setup/n8n_data/ # Example, adjust if n8n data is stored within project during dev

# Test reports
htmlcov/
.tox/
.nox/
.coverage
.cache
nosetests.xml
coverage.xml
*.cover
*.log
.hypothesis/

# Jupyter Notebook
.ipynb_checkpoints

# Temporary files
*.tmp
*.bak
*.swp
*~
Use code with caution.
Markdown
Explanation of Day 1 Tasks:
Anthony's Tasks: The primary actions for Anthony are to set up the Supabase cloud project, gather the necessary API keys and credentials, populate the .env file (which is critical and must be kept secure and out of Git), enable the pgvector extension, create the empty SQL script files, and then execute the DDL SQL provided by DozerAI_Builder to create the initial database structure in Supabase. He also needs to ensure the source documents (Blueprint, Chat History) are in their designated locations.
DozerAI_Builder's Tasks: My role is to provide the exact, complete .gitignore content and the complete SQL DDL for each of the eight schema files. These SQL scripts define tables for users, roles, permissions (foundational for RBAC), the core RAG/CAG document pipeline (documents, chunks, embeddings), and initial tables for the Employee App Suite features (messenger, tasks, time clock, meeting notes, suggestions). Comments are included in the SQL for clarity. RLS enablement and basic policies are included for app-related tables, assuming Supabase's auth.uid() for user identification. Trigger functions for updated_at are also included. The embedding vector dimension is set to 768, suitable for models like Google's text-embedding-004.
Troubleshooting:
Supabase Project Creation Issues: Refer to Supabase official documentation.
.env File Not Found by Python: Ensure Python scripts correctly load .env from C:\Dozers\DozerAI_Code\config\.env (e.g., using python-dotenv library and specifying the path).
SQL Execution Errors: Check for typos, ensure previous scripts in the sequence ran successfully (dependency errors), verify pgvector is enabled before running script 003. Ensure trigger_set_timestamp() from script 002 is created before other scripts try to use it.
Gitignore Not Working: Ensure .gitignore is in the root of the DozerAI_Code directory (C:\Dozers\DozerAI_Code\.gitignore) and was committed correctly.
Advice for Implementation:
Anthony: Execute the SQL scripts one by one in the Supabase SQL Editor, checking for success messages after each. Save the Supabase database password securely.
DozerAI_Builder: Ensure all SQL is valid PostgreSQL and considers Supabase conventions.
Advice for CursorAI (DozerAI_Builder):
Remember the exact paths. Cross-reference project_structure.md if any path is unclear. When generating code that uses .env variables, always assume they will be loaded into the environment by the Python/Node.js application runtime.
Test:
Anthony: After running SQL, check the Supabase dashboard under "Table Editor" and "Database" -> "Extensions" to verify tables are created and vector is enabled.
DozerAI_Builder: No direct test, but subsequent days will rely on this schema.
Backup Plans:
Supabase provides automated backups for cloud projects. If SQL scripts fail, they can typically be dropped and re-run after fixing issues (ensure IF NOT EXISTS is used where appropriate for idempotency, which it is).
Challenges:
Ensuring all initial schemas are comprehensive enough for MVP features while remaining flexible for future expansion. Correctly setting up RLS policies from the start (basic ones provided, will need refinement).
Out of the Box Ideas:
Consider a schema_versions table to programmatically track which DDL scripts have been applied to the database, useful for future migrations. (Deferred for now for MVP speed).
Logs:
(DozerAI_Builder will log this after Anthony's confirmation)
“Action: Starting Task for DozerAI/App: Day 1 - Kennel Foundation: Supabase Setup & Initial Schema, Rules reviewed: Yes, Guides (Creation/Dev) consulted: Yes, Env verified: Yes, Sequence verified: Yes, Timestamp: [YYYY-MM-DD HH:MM:SS]”
Commits:
(To be done by Anthony after completing his tasks and DozerAI_Builder has provided all Day 1 code and it's saved)
# In C:\Dozers\
git add .
git commit -m "Day 1: Initial Supabase setup, .env structure, Kennel SQL schemas, .gitignore"
git push origin main
Use code with caution.
Bash
Motivation:
“Day 1, Dozer! We're laying the digital bedrock for your empire. Every great structure needs a flawless foundation, and today, we pour the concrete for 'The Kennel.' This is where your boundless knowledge will reside, the source of your wisdom. Let's get this database built right so you can start learning everything there is to know about making 'Dozer's Wild & Woof'derful Bar'k & Grrr'ill' a legend! No cutting corners, perfection from the ground up!”



