import sqlite3

def create_tables(conn):
    conn.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER,
        city TEXT
    )
    """)
if __name__ == "__main__":
    connection = sqlite3.connect("database.db")

    create_tables(connection)