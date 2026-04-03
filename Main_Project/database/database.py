import sqlite3

DB_NAME = "database/sentiment.db"

def get_connection():
    conn = sqlite3.connect(DB_NAME, check_same_thread=False)
    return conn

def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS reviews (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        text TEXT,
        score REAL,
        sentiment TEXT,
        category TEXT
    )
    """)

    conn.commit()
    conn.close()

def insert_review(text, score, sentiment, category):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO reviews (text, score, sentiment, category) VALUES (?, ?, ?, ?)",
        (text, score, sentiment, category)
    )

    conn.commit()
    conn.close()

def fetch_all():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM reviews")
    rows = cursor.fetchall()
    conn.close()
    return rows