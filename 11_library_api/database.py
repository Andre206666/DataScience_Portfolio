import sqlite3
from models import Book

conn = sqlite3.connect("library.db")
c = conn.cursor()

c.execute("""
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY,
        title TEXT UNIQUE,
        author TEXT,
        genre TEXT
    )
""")

c.execute("""
    CREATE TABLE IF NOT EXISTS members (
        id INTEGER PRIMARY KEY,
        name TEXT UNIQUE,
        email TEXT
    )
""")

conn.commit()
print("Database created!")

def save_book(book):
    c.execute("INSERT OR IGNORE INTO books (title, author, genre) VALUES (?, ?, ?)",
              (book.title, book.author, book.genre))
    conn.commit()

b1 = Book("1984", "George Orwell", "Dystopia")
b2 = Book("Harry Potter", "J.K. Rowling", "Fantasy")
save_book(b1)
save_book(b2)
print("Books saved!")