import sqlite3

def create_connection(db_file):
    return sqlite3.connect(db_file)


def create_table(connection):
    sql = """
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY,
        name TEXT,
        author TEXT,
        publication_year INTEGER,
        genre TEXT,
        number_of_pages INTEGER,
        number_of_copies INTEGER
    )
    """
    cursor = connection.cursor()
    cursor.execute(sql)
    connection.commit()
    print("Таблица создана успешно")


def insert_books(connection):
    books = [
        ("War and Peace", "Leo Tolstoy", 1869, "Novel", 1225, 5),
        ("1984", "George Orwell", 1949, "Dystopian", 328, 8),
        ("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Novel", 180, 6),
     ]

    sql = """
    INSERT INTO books (name, author, publication_year, genre, number_of_pages, number_of_copies)
    VALUES (?, ?, ?, ?, ?, ?)
    """

    cursor = connection.cursor()
    cursor.executemany(sql, books)
    connection.commit()
    print("Книги добавлены успешно")


if __name__ == "__main__":
    connection = create_connection("books.db")

    create_table(connection)
    insert_books(connection)

    connection.close()
    print("Соединение закрыто")