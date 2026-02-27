import sqlite3


def create_connection(db_file):
    return sqlite3.connect(db_file)


def get_books_by_author(connection, author):
    cursor = connection.cursor()
    sql = """
        SELECT name
        FROM books
        WHERE author = ?
        ORDER BY name ASC
    """
    cursor.execute(sql, (author,))
    results = cursor.fetchall()


    books = [row[0] for row in results]
    return books


if __name__ == "__main__":
   connection = create_connection("books.db")

    # Пример: получаем книги Leo Tolstoy
    author_name = "Leo Tolstoy"
    books_by_author = get_books_by_author(connection, author_name)

    print(f"Книги автора {author_name}:")
    for book in books_by_author:
        print("-", book)

    # Закрываем соединение
    connection.close()
    print("Соединение закрыто")