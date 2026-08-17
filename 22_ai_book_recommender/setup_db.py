import sqlite3

def create_and_seed_db():
    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            genre TEXT NOT NULL,
            description TEXT NOT NULL
        )
    ''')

    cursor.execute('DELETE FROM books')

    sample_books = [
        ("The Martian", "Andy Weir", "Science Fiction", "An astronaut is stranded on Mars and must use his science skills to survive."),
        ("Dune", "Frank Herbert", "Science Fiction", "A young nobleman becomes entangled in a planetary struggle over the universe's most valuable resource."),
        ("The Hobbit", "J.R.R. Tolkien", "Fantasy", "A home-loving hobbit goes on an epic quest to help a group of dwarves reclaim their mountain home from a dragon."),
        ("Gone Girl", "Gillian Flynn", "Thriller", "A woman disappears on her fifth wedding anniversary, and all evidence points to her husband."),
        ("Steve Jobs", "Walter Isaacson", "Biography", "The definitive biography of the visionary Apple co-founder based on exclusive interviews."),
        ("Project Hail Mary", "Andy Weir", "Science Fiction", "A lone astronaut must save the Earth from disaster in a desperate mission to deep space.")
    ]

    cursor.executemany('''
        INSERT INTO books (title, author, genre, description)
        VALUES (?, ?, ?, ?)
    ''', sample_books)

    conn.commit()
    conn.close()
    print("Database 'books.db' created successfully with 6 sample books!")

if __name__ == "__main__":
    create_and_seed_db()