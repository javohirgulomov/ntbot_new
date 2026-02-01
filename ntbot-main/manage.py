from core.db_settings import execute_query

# Drop users table
execute_query("DROP TABLE IF EXISTS users CASCADE;")
print("✅ Users table dropped!")

# Recreate table
create_query = """
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    chat_id BIGINT UNIQUE NOT NULL,
    username VARCHAR(255),
    language VARCHAR(10),
    full_name VARCHAR(255),
    phone_number VARCHAR(20),
    longitude FLOAT,
    latitude FLOAT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""
execute_query(create_query)
print("✅ Table recreated!")

exit()