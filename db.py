import sqlite3
from datetime import datetime

def get_db_connection():
    """Create a connection to the SQLite database."""
    conn = sqlite3.connect('cache.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Initialize the database with required tables."""
    conn = get_db_connection()
    c = conn.cursor()
    
    # Create cache table if it doesn't exist
    c.execute('''
        CREATE TABLE IF NOT EXISTS cache (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            prompt TEXT NOT NULL,
            response TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    conn.commit()
    conn.close()

def add_to_cache(prompt, response):
    """Add a new entry to the cache."""
    conn = get_db_connection()
    c = conn.cursor()
    
    c.execute('''
        INSERT INTO cache (prompt, response, timestamp)
        VALUES (?, ?, ?)
    ''', (prompt, response, datetime.now()))
    
    conn.commit()
    conn.close()

def get_cache_entries():
    """Retrieve all cache entries."""
    conn = get_db_connection()
    c = conn.cursor()
    
    c.execute('SELECT * FROM cache ORDER BY timestamp DESC')
    entries = c.fetchall()
    
    conn.close()
    return entries

def search_cache_for_context(prompt):
    """Search cache for relevant entries based on prompt keywords."""
    conn = get_db_connection()
    c = conn.cursor()
    
    # Simple keyword-based search
    keywords = prompt.lower().split()
    query = ' OR '.join([f'prompt LIKE ?' for _ in keywords])
    params = [f'%{keyword}%' for keyword in keywords]
    
    c.execute(f'''
        SELECT * FROM cache 
        WHERE {query}
        ORDER BY timestamp DESC
        LIMIT 5
    ''', params)
    
    entries = c.fetchall()
    conn.close()
    return entries 