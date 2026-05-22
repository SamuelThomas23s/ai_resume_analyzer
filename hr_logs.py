import sqlite3
from datetime import datetime

DB_NAME = "hr_logs.db"


def init_logs():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS decisions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        candidate TEXT,
        job TEXT,
        decision TEXT,
        reason TEXT,
        created_at TEXT
    )
    """)

    conn.commit()
    conn.close()


def save_decision(candidate, job, decision, reason):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute("""
    INSERT INTO decisions (candidate, job, decision, reason, created_at)
    VALUES (?, ?, ?, ?, ?)
    """, (candidate, job, decision, reason, str(datetime.now())))

    conn.commit()
    conn.close()


def get_logs():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute("SELECT * FROM decisions")
    data = c.fetchall()

    conn.close()
    return data