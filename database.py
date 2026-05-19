import sqlite3
from datetime import datetime

DB_NAME = "candidates.db"


def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS candidates (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        score TEXT,
        created_at TEXT
    )
    """)

    conn.commit()
    conn.close()


def save_candidate(name, score):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute("""
    INSERT INTO candidates (name, score, created_at)
    VALUES (?, ?, ?)
    """, (name, score, str(datetime.now())))

    conn.commit()
    conn.close()


def search_candidates(keyword):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute("""
    SELECT * FROM candidates
    WHERE name LIKE ?
    """, ('%' + keyword + '%',))

    results = c.fetchall()
    conn.close()

    return results