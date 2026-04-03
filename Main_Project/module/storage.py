# ======================================================
# module/storage.py
# ======================================================
import sqlite3
import streamlit as st
import pandas as pd


@st.cache_resource
def get_db_connection():
    conn = sqlite3.connect("sentiment_results.db", check_same_thread=False)
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA synchronous=NORMAL")
    conn.execute("PRAGMA cache_size=100000")
    conn.execute("PRAGMA temp_store=MEMORY")
    conn.execute("""
        CREATE TABLE IF NOT EXISTS sentiment_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text TEXT,
            score REAL,
            sentiment TEXT
        )
    """)

    conn.commit()
    return conn
def bulk_insert(conn, rows):
    conn.executemany(
        "INSERT INTO sentiment_data (text, score, sentiment) VALUES (?,?,?)",
        rows
    )
    conn.commit()


def query_all(conn):
    cursor = conn.execute("SELECT text, score, sentiment FROM sentiment_data")
    return cursor.fetchall()


def bulk_insert(conn, rows):
    conn.executemany(
        "INSERT INTO sentiment_data (text, score, sentiment) VALUES (?,?,?)",
        rows
    )
    conn.commit()
    
def query_all(conn):
    cursor = conn.execute("SELECT text, score, sentiment FROM sentiment_data")
    return cursor.fetchall()


def export_summary_excel(df):
    summary = df["Sentiment"].value_counts().reset_index()
    summary.columns = ["Sentiment", "Count"]

    score_stats = pd.DataFrame({
        "Metric": ["Average Score", "Max Score", "Min Score"],
        "Value": [df["Score"].mean(), df["Score"].max(), df["Score"].min()]
    })

    file_name = "sentiment_summary.xlsx"
def export_summary_excel(df):
    summary = df["Sentiment"].value_counts().reset_index()
    summary.columns = ["Sentiment", "Count"]

    score_stats = pd.DataFrame({
        "Metric": ["Average Score", "Max Score", "Min Score"],
        "Value": [df["Score"].mean(), df["Score"].max(), df["Score"].min()]
    })

    file_name = "sentiment_summary.xlsx"

    with pd.ExcelWriter(file_name) as writer:
        df.to_excel(writer, sheet_name="All Data", index=False)
        summary.to_excel(writer, sheet_name="Summary", index=False)
        score_stats.to_excel(writer, sheet_name="Score Stats", index=False)

    return file_name