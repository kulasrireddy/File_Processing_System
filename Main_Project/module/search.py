from database.database import get_connection

def search_keyword(keyword):
    conn = get_connection()
    cursor = conn.cursor()

    query = "SELECT * FROM reviews WHERE text LIKE ?"
    cursor.execute(query, ('%' + keyword + '%',))

    results = cursor.fetchall()
    conn.close()
    return results