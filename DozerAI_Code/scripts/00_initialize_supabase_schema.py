# C:\Dozers\DozerAI_Code\scripts\00_initialize_supabase_schema.py
import os
import sys
import logging
import time
from dotenv import load_dotenv
from psycopg2 import sql, OperationalError, ProgrammingError

# --- Setup Logging ---
SCRIPT_DIR_FOR_LOG = os.path.dirname(os.path.abspath(__file__))
LOG_FILE_PATH = os.path.join(SCRIPT_DIR_FOR_LOG, 'schema_init.log')

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(LOG_FILE_PATH, mode='w'), # Overwrite log file each run
    ]
)
logger = logging.getLogger(__name__)

# --- Early check for psycopg2 ---
try:
    import psycopg2
except ImportError as e:
    logger.critical(f"Failed to import psycopg2. Message: {e}")
    logger.critical(f"Python executable: {sys.executable}")
    logger.critical(f"Python sys.path: {sys.path}")
    sys.exit(1)
# --- End early check ---

# --- Configuration & Constants ---
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR_FOR_LOG)
CONFIG_DIR = os.path.join(PROJECT_ROOT, 'config')
DOTENV_PATH = os.path.join(CONFIG_DIR, '.env')

# Load environment variables from .env file
dotenv_path = os.path.join(os.path.dirname(__file__), '..', 'config', '.env')
if os.path.exists(dotenv_path):
    logger.info(f"Attempting to load .env file from: {dotenv_path}")
    load_dotenv(dotenv_path)
    logger.info(".env file loaded.")
else:
    logger.warning(f".env file not found at {dotenv_path}. Script may rely on environment variables set externally.")

# DEBUG: Print raw values directly after attempting to load .env
print(f"DEBUG: Raw SUPABASE_POOLER_ENABLED from env: '{os.getenv('SUPABASE_POOLER_ENABLED')}'")
print(f"DEBUG: Raw SUPABASE_POOL_HOST from env: '{os.getenv('SUPABASE_POOL_HOST')}'")
print(f"DEBUG: Raw SUPABASE_POOL_PORT from env: '{os.getenv('SUPABASE_POOL_PORT')}'")
print(f"DEBUG: Raw SUPABASE_POOLER_DB_USER from env: '{os.getenv('SUPABASE_POOLER_DB_USER')}'")

# --- Supabase Connection Details ---
POOLER_ENABLED = os.getenv("SUPABASE_POOLER_ENABLED", "false").lower() == "true"
POOLER_USER = os.getenv("SUPABASE_POOLER_DB_USER")
POOLER_PASSWORD = os.getenv("SUPABASE_POOLER_DB_PASSWORD")
POOLER_HOST = os.getenv("SUPABASE_POOL_HOST")
POOLER_PORT = os.getenv("SUPABASE_POOL_PORT", "6543")
POOLER_DB_NAME = os.getenv("SUPABASE_POOLER_DB_NAME", "postgres")

DB_USER = os.getenv("SUPABASE_DB_USER")
DB_PASSWORD = os.getenv("SUPABASE_DB_PASSWORD")
DB_HOST = os.getenv("SUPABASE_DB_HOST")
DB_PORT = os.getenv("SUPABASE_DB_PORT", "5432")
DB_NAME = os.getenv("SUPABASE_DB_NAME", "postgres")

pooler_config_complete = POOLER_ENABLED and all([POOLER_USER, POOLER_PASSWORD, POOLER_HOST, POOLER_PORT, POOLER_DB_NAME])
direct_db_config_complete = all([DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME])

if not (pooler_config_complete or direct_db_config_complete):
    logger.error("CRITICAL ERROR: Insufficient Supabase connection details in .env.")
    sys.exit(1)

conn = None
MAX_RETRIES = 3
RETRY_DELAY = 5 # seconds

# --- SQL Schema Definitions ---

# Part 1: Core definitions, tables, and functions needed by RLS policies
SQL_DEFINITIONS_PART_1 = """
-- Enable pgvector extension if not already enabled
CREATE EXTENSION IF NOT EXISTS vector WITH SCHEMA extensions;

-- Create a schema for private user data if it doesn't exist
CREATE SCHEMA IF NOT EXISTS private;

-- Helper function to drop RLS policies safely
CREATE OR REPLACE FUNCTION drop_rls_policy_if_exists(
    table_name_text TEXT,
    policy_name_text TEXT
)
RETURNS VOID AS $$
BEGIN
    IF EXISTS (
        SELECT 1
        FROM pg_policies
        WHERE schemaname = 'public' -- Assuming tables are in public schema
        AND tablename = table_name_text
        AND policyname = policy_name_text
    ) THEN
        EXECUTE 'DROP POLICY ' || quote_ident(policy_name_text) || ' ON public.' || quote_ident(table_name_text);
        RAISE NOTICE 'Dropped RLS policy % on table %', policy_name_text, table_name_text;
    ELSE
        RAISE NOTICE 'RLS policy % on table % does not exist, skipping drop.', policy_name_text, table_name_text;
    END IF;
END;
$$ LANGUAGE plpgsql;

-- Core Application Settings Table (without RLS yet)
CREATE TABLE IF NOT EXISTS app_settings (
    setting_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    setting_name TEXT NOT NULL UNIQUE,
    setting_value TEXT,
    description TEXT,
    last_updated_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);
COMMENT ON TABLE app_settings IS 'Stores core application-wide settings and configurations.';

-- Users, Roles, and Permissions Tables (without RLS yet)
CREATE TABLE IF NOT EXISTS user_roles (
    role_id SERIAL PRIMARY KEY,
    role_name TEXT NOT NULL UNIQUE,
    description TEXT,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);
COMMENT ON TABLE user_roles IS 'Defines different user roles within the application.';

INSERT INTO user_roles (role_name, description) VALUES
    ('admin', 'Administrator with full system access'),
    ('manager', 'Managerial role with oversight capabilities'),
    ('employee', 'Standard employee user'),
    ('guest', 'Limited access guest user')
ON CONFLICT (role_name) DO NOTHING;

CREATE TABLE IF NOT EXISTS user_profiles (
    user_id UUID PRIMARY KEY REFERENCES auth.users(id) ON DELETE CASCADE,
    role_id INTEGER REFERENCES user_roles(role_id) NOT NULL,
    full_name TEXT,
    avatar_url TEXT,
    updated_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);
COMMENT ON TABLE user_profiles IS 'Stores public profile information for users, linking to auth.users and user_roles.';

-- Function to get user_id from email
CREATE OR REPLACE FUNCTION get_user_id_by_email(email_text TEXT)
RETURNS UUID AS $$
DECLARE
    user_id_result UUID;
BEGIN
    SELECT id INTO user_id_result FROM auth.users WHERE email = email_text;
    RETURN user_id_result;
END;
$$ LANGUAGE plpgsql;

-- Function to assign a role to a user
CREATE OR REPLACE FUNCTION assign_user_role(p_user_id UUID, p_role_name TEXT)
RETURNS VOID AS $$
DECLARE
    v_role_id INTEGER;
BEGIN
    SELECT role_id INTO v_role_id FROM user_roles WHERE role_name = p_role_name;
    IF v_role_id IS NULL THEN
        RAISE EXCEPTION 'Role % not found', p_role_name;
    END IF;
    INSERT INTO user_profiles (user_id, role_id, full_name)
    VALUES (p_user_id, v_role_id, (SELECT raw_user_meta_data->>'full_name' FROM auth.users WHERE id = p_user_id))
    ON CONFLICT (user_id) DO UPDATE SET role_id = v_role_id;
END;
$$ LANGUAGE plpgsql;

-- Function to get a user's role name (CRITICAL FOR RLS)
CREATE OR REPLACE FUNCTION public.get_user_role(p_user_id UUID)
RETURNS TEXT AS $$
DECLARE
    v_role_name TEXT;
BEGIN
    SELECT ur.role_name INTO v_role_name
    FROM public.user_profiles up
    JOIN public.user_roles ur ON up.role_id = ur.role_id
    WHERE up.user_id = p_user_id;
    RETURN v_role_name;
END;
$$ LANGUAGE plpgsql SECURITY DEFINER;
"""

# Part 2: RLS policies and the rest of the schema
SQL_RLS_AND_REMAINDER_PART_2 = """
-- Enable RLS for app_settings
SELECT drop_rls_policy_if_exists('app_settings', 'Allow admin full access to app_settings');
ALTER TABLE app_settings ENABLE ROW LEVEL SECURITY;
CREATE POLICY "Allow admin full access to app_settings"
    ON app_settings
    FOR ALL
    USING (auth.jwt() ->> 'role' = 'service_role' OR public.get_user_role(auth.uid()::UUID) = 'admin')
    WITH CHECK (auth.jwt() ->> 'role' = 'service_role' OR public.get_user_role(auth.uid()::UUID) = 'admin');

-- RLS for user_profiles
SELECT drop_rls_policy_if_exists('user_profiles', 'Allow users to see their own profile');
SELECT drop_rls_policy_if_exists('user_profiles', 'Allow admins to see all profiles');
SELECT drop_rls_policy_if_exists('user_profiles', 'Allow users to update their own profile');
SELECT drop_rls_policy_if_exists('user_profiles', 'Allow admins to update any profile');
ALTER TABLE user_profiles ENABLE ROW LEVEL SECURITY;
CREATE POLICY "Allow users to see their own profile"
    ON user_profiles FOR SELECT
    USING (auth.uid() = user_id);
CREATE POLICY "Allow admins to see all profiles"
    ON user_profiles FOR SELECT
    USING (public.get_user_role(auth.uid()::UUID) = 'admin');
CREATE POLICY "Allow users to update their own profile"
    ON user_profiles FOR UPDATE
    USING (auth.uid() = user_id)
    WITH CHECK (auth.uid() = user_id);
CREATE POLICY "Allow admins to update any profile"
    ON user_profiles FOR UPDATE
    USING (public.get_user_role(auth.uid()::UUID) = 'admin')
    WITH CHECK (public.get_user_role(auth.uid()::UUID) = 'admin');

-- RLS for user_roles
SELECT drop_rls_policy_if_exists('user_roles', 'Allow authenticated users to read roles');
SELECT drop_rls_policy_if_exists('user_roles', 'Allow admin to manage roles');
ALTER TABLE user_roles ENABLE ROW LEVEL SECURITY;
CREATE POLICY "Allow authenticated users to read roles"
    ON user_roles FOR SELECT
    USING (auth.role() = 'authenticated');
CREATE POLICY "Allow admin to manage roles"
    ON user_roles FOR ALL
    USING (public.get_user_role(auth.uid()::UUID) = 'admin')
    WITH CHECK (public.get_user_role(auth.uid()::UUID) = 'admin');

-- 3. Documents, Chunks, and Embeddings Tables ("The Kennel" RAG System)
CREATE TABLE IF NOT EXISTS documents (
    document_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    title TEXT NOT NULL,
    source_uri TEXT UNIQUE,
    document_type TEXT,
    metadata JSONB,
    content_hash TEXT,
    last_processed_at TIMESTAMPTZ,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);
COMMENT ON TABLE documents IS 'Stores metadata about ingested documents for the RAG system.';

CREATE TABLE IF NOT EXISTS document_chunks (
    chunk_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    document_id UUID NOT NULL REFERENCES documents(document_id) ON DELETE CASCADE,
    chunk_text TEXT NOT NULL,
    chunk_order INTEGER NOT NULL,
    metadata JSONB,
    embedding extensions.vector(1536),
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);
COMMENT ON TABLE document_chunks IS 'Stores individual text chunks from documents and their vector embeddings.';
CREATE INDEX IF NOT EXISTS idx_document_chunks_document_id ON document_chunks(document_id);
CREATE INDEX IF NOT EXISTS idx_hnsw_document_chunks_embedding ON document_chunks USING hnsw (embedding extensions.vector_l2_ops);

-- 4. App Messenger Tables
CREATE TABLE IF NOT EXISTS message_channels (
    channel_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    channel_name TEXT NOT NULL UNIQUE,
    description TEXT,
    created_by UUID REFERENCES auth.users(id),
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    channel_type TEXT DEFAULT 'public'
);
CREATE TABLE IF NOT EXISTS channel_members (
    channel_id UUID NOT NULL REFERENCES message_channels(channel_id) ON DELETE CASCADE,
    user_id UUID NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE,
    joined_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    last_read_at TIMESTAMPTZ,
    PRIMARY KEY (channel_id, user_id)
);
CREATE TABLE IF NOT EXISTS messages (
    message_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    channel_id UUID NOT NULL REFERENCES message_channels(channel_id) ON DELETE CASCADE,
    sender_id UUID NOT NULL REFERENCES auth.users(id),
    content TEXT NOT NULL,
    metadata JSONB,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMPTZ
);
CREATE INDEX IF NOT EXISTS idx_messages_channel_id_created_at ON messages(channel_id, created_at DESC);

-- 5. App Tasks Tables
CREATE TABLE IF NOT EXISTS tasks (
    task_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    title TEXT NOT NULL,
    description TEXT,
    status TEXT DEFAULT 'pending',
    priority TEXT DEFAULT 'medium',
    due_date DATE,
    assigned_to UUID REFERENCES auth.users(id),
    created_by UUID REFERENCES auth.users(id),
    completed_at TIMESTAMPTZ,
    requires_sign_off BOOLEAN DEFAULT FALSE,
    signed_off_by UUID REFERENCES auth.users(id),
    signed_off_at TIMESTAMPTZ,
    project_id UUID,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX IF NOT EXISTS idx_tasks_assigned_to_status ON tasks(assigned_to, status);
CREATE INDEX IF NOT EXISTS idx_tasks_due_date ON tasks(due_date);

-- Function to calculate total_hours on clock_out (should already be created in PART 1 if needed by trigger)
-- If it's only used by the trigger below, it's fine here too, but good practice to define functions early.
-- For safety, ensure it's defined in SQL_DEFINITIONS_PART_1 if it isn't already.
CREATE OR REPLACE FUNCTION calculate_total_hours()
RETURNS TRIGGER AS $$
BEGIN
  IF NEW.clock_out_time IS NOT NULL AND NEW.clock_in_time IS NOT NULL THEN
    NEW.total_hours = EXTRACT(EPOCH FROM (NEW.clock_out_time - NEW.clock_in_time)) / 3600.0;
    NEW.status = 'closed';
  END IF;
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- 6. App Time Clock Tables
CREATE TABLE IF NOT EXISTS time_entries (
    entry_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL REFERENCES auth.users(id),
    clock_in_time TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    clock_out_time TIMESTAMPTZ,
    notes TEXT,
    total_hours DECIMAL(5,2),
    status TEXT DEFAULT 'open',
    approved_by UUID REFERENCES auth.users(id),
    approved_at TIMESTAMPTZ,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);

DO $$
BEGIN
    DROP TRIGGER IF EXISTS calculate_total_hours_trigger ON time_entries;
    CREATE TRIGGER calculate_total_hours_trigger
    BEFORE INSERT OR UPDATE ON time_entries
    FOR EACH ROW
    EXECUTE FUNCTION calculate_total_hours();
END $$;
CREATE INDEX IF NOT EXISTS idx_time_entries_user_id_clock_in_time ON time_entries(user_id, clock_in_time DESC);

-- 7. App Meeting Notes Tables
CREATE TABLE IF NOT EXISTS meetings (
    meeting_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    title TEXT NOT NULL,
    meeting_date DATE NOT NULL,
    start_time TIME,
    end_time TIME,
    location TEXT,
    created_by UUID REFERENCES auth.users(id),
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS meeting_attendees (
    meeting_id UUID NOT NULL REFERENCES meetings(meeting_id) ON DELETE CASCADE,
    user_id UUID NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE,
    status TEXT DEFAULT 'accepted',
    PRIMARY KEY (meeting_id, user_id)
);
CREATE TABLE IF NOT EXISTS meeting_notes (
    note_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    meeting_id UUID NOT NULL REFERENCES meetings(meeting_id) ON DELETE CASCADE,
    content TEXT NOT NULL,
    created_by UUID REFERENCES auth.users(id),
    last_modified_by UUID REFERENCES auth.users(id),
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS action_items (
    action_item_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    meeting_id UUID REFERENCES meetings(meeting_id) ON DELETE CASCADE,
    note_id UUID REFERENCES meeting_notes(note_id) ON DELETE CASCADE,
    description TEXT NOT NULL,
    assigned_to UUID REFERENCES auth.users(id),
    due_date DATE,
    status TEXT DEFAULT 'open',
    created_by UUID REFERENCES auth.users(id),
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);

-- 8. App Suggestions/Feedback Table
CREATE TABLE IF NOT EXISTS suggestions (
    suggestion_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES auth.users(id),
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    category TEXT,
    status TEXT DEFAULT 'new',
    votes INTEGER DEFAULT 0,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX IF NOT EXISTS idx_suggestions_status_category ON suggestions(status, category);

-- Remaining RLS policies
SELECT drop_rls_policy_if_exists('documents', 'Allow admins full access to documents');
ALTER TABLE documents ENABLE ROW LEVEL SECURITY;
CREATE POLICY "Allow admins full access to documents"
    ON documents FOR ALL
    USING (public.get_user_role(auth.uid()::UUID) = 'admin')
    WITH CHECK (public.get_user_role(auth.uid()::UUID) = 'admin');

SELECT drop_rls_policy_if_exists('document_chunks', 'Allow admins full access to chunks');
ALTER TABLE document_chunks ENABLE ROW LEVEL SECURITY;
CREATE POLICY "Allow admins full access to chunks"
    ON document_chunks FOR ALL
    USING (public.get_user_role(auth.uid()::UUID) = 'admin')
    WITH CHECK (public.get_user_role(auth.uid()::UUID) = 'admin');

SELECT drop_rls_policy_if_exists('message_channels', 'Base RLS for message_channels');
ALTER TABLE message_channels ENABLE ROW LEVEL SECURITY;
CREATE POLICY "Base RLS for message_channels" ON message_channels FOR SELECT USING (true);

SELECT drop_rls_policy_if_exists('channel_members', 'Base RLS for channel_members');
ALTER TABLE channel_members ENABLE ROW LEVEL SECURITY;
CREATE POLICY "Base RLS for channel_members" ON channel_members FOR SELECT USING (true);

SELECT drop_rls_policy_if_exists('messages', 'Base RLS for messages');
ALTER TABLE messages ENABLE ROW LEVEL SECURITY;
CREATE POLICY "Base RLS for messages" ON messages FOR SELECT USING (true);

SELECT drop_rls_policy_if_exists('tasks', 'Base RLS for tasks');
ALTER TABLE tasks ENABLE ROW LEVEL SECURITY;
CREATE POLICY "Base RLS for tasks" ON tasks FOR SELECT USING (true);

SELECT drop_rls_policy_if_exists('time_entries', 'Base RLS for time_entries');
ALTER TABLE time_entries ENABLE ROW LEVEL SECURITY;
CREATE POLICY "Base RLS for time_entries" ON time_entries FOR SELECT USING (true);

SELECT drop_rls_policy_if_exists('meetings', 'Base RLS for meetings');
ALTER TABLE meetings ENABLE ROW LEVEL SECURITY;
CREATE POLICY "Base RLS for meetings" ON meetings FOR SELECT USING (true);

SELECT drop_rls_policy_if_exists('meeting_attendees', 'Base RLS for meeting_attendees');
ALTER TABLE meeting_attendees ENABLE ROW LEVEL SECURITY;
CREATE POLICY "Base RLS for meeting_attendees" ON meeting_attendees FOR SELECT USING (true);

SELECT drop_rls_policy_if_exists('meeting_notes', 'Base RLS for meeting_notes');
ALTER TABLE meeting_notes ENABLE ROW LEVEL SECURITY;
CREATE POLICY "Base RLS for meeting_notes" ON meeting_notes FOR SELECT USING (true);

SELECT drop_rls_policy_if_exists('action_items', 'Base RLS for action_items');
ALTER TABLE action_items ENABLE ROW LEVEL SECURITY;
CREATE POLICY "Base RLS for action_items" ON action_items FOR SELECT USING (true);

SELECT drop_rls_policy_if_exists('suggestions', 'Base RLS for suggestions');
ALTER TABLE suggestions ENABLE ROW LEVEL SECURITY;
CREATE POLICY "Base RLS for suggestions" ON suggestions FOR SELECT USING (true);

-- Final check message
SELECT 'DozerAI Kennel Base Schema Initialized Successfully (v1.0)';
"""

def initialize_schema():
    global conn # Keep conn global for potential reuse if script evolves
    connection_successful = False
    conn_details_to_use = {}
    connection_type = ""
    cur = None # Cursor should be local to each connection attempt block

    # Determine connection method (Pooler preferred)
    use_pooler = POOLER_ENABLED and pooler_config_complete
    if use_pooler:
        logger.info("Attempting to connect using Supabase Connection Pooler...")
        connection_type = "Pooler"
        conn_details_to_use = {
            "user": POOLER_USER, "password": POOLER_PASSWORD, "host": POOLER_HOST,
            "port": POOLER_PORT, "database": POOLER_DB_NAME, "connect_timeout": 10
        }
    elif direct_db_config_complete:
        logger.info("Pooler not enabled or configured, attempting Direct Database Connection...")
        connection_type = "Direct DB"
        conn_details_to_use = {
            "user": DB_USER, "password": DB_PASSWORD, "host": DB_HOST,
            "port": DB_PORT, "database": DB_NAME, "connect_timeout": 10
        }
    else:
        logger.error("CRITICAL ERROR: No valid Supabase connection method configured.")
        return # Exit if no connection method is viable

    # Connection attempt loop
    for attempt in range(MAX_RETRIES):
        try:
            conn = psycopg2.connect(**conn_details_to_use)
            # conn.autocommit = False # Ensure we control transactions explicitly
            logger.info(f"Successfully connected to Supabase PostgreSQL using {connection_type} on attempt {attempt + 1}.")
            connection_successful = True
            break
        except Exception as e:
            logger.error(f"Attempt {attempt + 1} of {MAX_RETRIES} failed to connect using {connection_type}: {e}")
            if attempt < MAX_RETRIES - 1:
                time.sleep(RETRY_DELAY)
            else:
                logger.error(f"All {MAX_RETRIES} connection attempts using {connection_type} failed.")
                break
    
    if not connection_successful:
        logger.error("CRITICAL DATABASE CONNECTION FAILED. Cannot proceed with schema initialization.")
        if conn: # Close if partially opened
             try: conn.close()
             except: pass
        return

    try:
        # --- Execute Part 1: Definitions ---
        with conn.cursor() as cur_part1:
            logger.info("Starting PART 1: Definitions and core functions...")
            cur_part1.execute(SQL_DEFINITIONS_PART_1)
            logger.info("PART 1 SQL block execution attempted.")
        conn.commit() # Commit after Part 1
        logger.info("PART 1: Definitions and core functions committed successfully.")

        # --- Execute Part 2: RLS Policies and Remainder ---
        with conn.cursor() as cur_part2:
            logger.info("Starting PART 2: RLS Policies and remaining schema...")
            cur_part2.execute(SQL_RLS_AND_REMAINDER_PART_2)
            logger.info("PART 2 SQL block execution attempted.")
        conn.commit() # Commit after Part 2
        logger.info("PART 2: RLS Policies and remaining schema committed successfully.")
        
        # --- Verification (after both parts are committed) ---
        with conn.cursor() as cur_verify:
            logger.info("Verifying critical tables existence post-commit...")
            # Updated critical_tables list to reflect actual RLS-dependent tables first
            critical_tables = ["app_settings", "user_profiles", "user_roles", "documents", "document_chunks", "time_entries"]
            all_verified = True
            for table_name in critical_tables:
                cur_verify.execute(f"SELECT EXISTS (SELECT FROM information_schema.tables WHERE table_name = '{table_name}' AND table_schema = 'public');")
                table_exists_result = cur_verify.fetchone()
                if table_exists_result and table_exists_result[0]:
                    logger.info(f"VERIFICATION SUCCESS: '{table_name}' table exists.")
                else:
                    logger.error(f"VERIFICATION FAILURE: '{table_name}' table does NOT exist. Result: {table_exists_result}")
                    all_verified = False
            
            if all_verified:
                logger.info("All critical tables verified successfully after FULL schema commit.")
            else:
                logger.error("One or more critical tables FAILED verification after FULL schema commit.")
        
        logger.info("FULL schema initialization process completed successfully.")

    except ProgrammingError as pe: # Catch SQL syntax or logical errors
        logger.error(f"Database Programming Error (likely SQL syntax) during schema initialization: {pe}")
        if conn:
            try: conn.rollback(); logger.info("Transaction rolled back due to ProgrammingError.")
            except Exception as re: logger.error(f"Error during rollback for ProgrammingError: {re}")
    except OperationalError as oe: # Catch connection or DB operation issues
        logger.error(f"Database Operational Error during schema initialization: {oe}")
        if conn:
            try: conn.rollback(); logger.info("Transaction rolled back due to OperationalError.")
            except Exception as re: logger.error(f"Error during rollback for OperationalError: {re}")
    except Exception as e: # Catch any other errors
        logger.error(f"An unexpected error occurred during schema initialization: {e}")
        if conn:
            try: conn.rollback(); logger.info("Transaction rolled back due to unexpected error.")
            except Exception as re: logger.error(f"Error during rollback for unexpected error: {re}")
    finally:
        if conn and not conn.closed: # Ensure connection is closed
            try:
                # No need to close cursors explicitly if using `with conn.cursor() as cur:`
                conn.close()
                logger.info("Database connection closed.")
            except Exception as ce:
                logger.error(f"Error closing connection: {ce}")

if __name__ == "__main__":
    logger.info("Starting DozerAI Supabase Schema Initializer (Split Execution)...")
    initialize_schema()