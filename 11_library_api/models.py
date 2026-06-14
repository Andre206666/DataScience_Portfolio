import sqlite3

class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre
        self.available = True

    def borrow(self):
        self.available = False
        return self

    def return_book(self):
        self.avaiable = True
        return self

    def __str__(self):
        return f"title {self.title}, author {self.author}, genre {self.genre} avaible {self.available}"

class Member:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.borrowed_books = []

    def borrow_book(self, book):
        book.borrow()
        self.borrowed_books.append(book)

    def return_book(self, book):
        book.return_book()
        self.borrowed_books.remove(book)

    def __str__(self):
        return f"Name: {self.name}, Email: {self.email}"

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def borrow_book(self, member, book):
        member.borrow_book(book)

    def return_book(self, member, book):
        member.return_book(book)

    def __str__(self):
        return f"Library | Books: {len(self.books)} | Members: {len(self.members)}"

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

