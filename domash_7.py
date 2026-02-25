import sqlite3

def create_connection(db_file):
    connection = None
    try:
        connection = sqlite3.connect(db_file)
        print(f"Connection to {db_file} is successful")
    except sqlite3.Error as e:
        print(e)
    return connection

def create_table(connection, sql):
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
        print("Таблица создана успешно")
    except sqlite3.Error as e:
        print(f"Ошибка создания таблицы: {e}")

# def insert_books(connection):
#     books = [
#         ("War and Peace", "Leo Tolstoy", 1869, "Novel", 1225, 5),
#         ("1984", "George Orwell", 1949, "Dystopian", 328, 8),
#         ("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Novel", 180, 6),
#          ]
#
#     sql = """
#     INSERT INTO books (name, author, publication_year, genre, number_of_pages, number_of_copies)
#     VALUES (?, ?, ?, ?, ?, ?)
#     """

    # cursor = connection.cursor()
    # cursor.executemany(sql, books)
    # connection.commit()  # <- обязательно, чтобы данные сохранились
    # print("Книги добавлены успешно")
#
# if __name__ == "__main__":
#     connection = create_connection("books.db")

sql_create_books_table = """
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            author TEXT,
            publication_year INTEGER,
            genre TEXT,
            number_of_pages INTEGER,
            number_of_copies INTEGER
        )
        """

connection = create_connection("books.db")
create_table(connection, sql_create_books_table)

connection.close()
print("Соединение закрыто")




