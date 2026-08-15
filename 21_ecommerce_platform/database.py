import sqlite3
import pandas as pd

conn = sqlite3.connect("ecommerce.db", check_same_thread=False)
c = conn.cursor()

c.execute("""
    CREATE TABLE IF NOT EXISTS books(
        id INTEGER PRIMARY KEY,
        title TEXT,
        price REAL,
        rating TEXT,
        rating_num INTEGER
    )
""")
conn.commit()
print("Table created successfully")

def save_book(df):
    df.to_sql("books", conn, if_exists="replace", index=False)
    print("Books saved!")

def get_all_books():
    return pd.read_sql("SELECT * FROM books", conn)

def get_stats():
    return pd.read_sql("""
       SELECT AVG(price) as avg_price,
             COUNT(*) as total_books
        FROM books""",
                       conn)

if __name__ == "__main__":
    from scraper import scrape_books
    df = scrape_books(2)
    df["price"] = df["price"].apply(lambda x: float(x.replace('Â£', '').replace('£', '').strip()))
    rating_map = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
    df["rating_num"] = df["rating"].map(rating_map)
    save_book(df)
    print(get_all_books())
    print(get_stats())

