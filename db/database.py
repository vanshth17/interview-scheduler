import sqlite3
from config.settings import settings

def get_connection():
    return sqlite3.connect(settings.DB_PATH)


def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS interviews (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        time TEXT,
        status TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS memory (
        thread_id TEXT PRIMARY KEY,
        name TEXT,
        time TEXT
    )
    """)

    conn.commit()
    conn.close()