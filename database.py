import sqlite3

DB_NAME = "candidates.db"


def get_all_candidates():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute("SELECT * FROM candidates")
    data = c.fetchall()

    conn.close()
    return data


def get_candidates_count():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute("SELECT COUNT(*) FROM candidates")
    count = c.fetchone()[0]

    conn.close()
    return count


def get_best_candidates(limit=5):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute("""
    SELECT * FROM candidates
    ORDER BY score DESC
    LIMIT ?
    """, (limit,))

    data = c.fetchall()
    conn.close()
    return data