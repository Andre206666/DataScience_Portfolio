import sqlite3

conn = sqlite3.connect('sales.db')
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY,
        name TEXT UNIQUE,
        price REAL,
        category TEXT
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS sales (
        id INTEGER PRIMARY KEY,
        product_name TEXT,
        quantity INTEGER,
        total REAL,
        date TEXT
    )
""")

conn.commit()
print("Database created!")

def save_product(product):
    cursor.execute("""
        INSERT OR IGNORE INTO products (name, price, category)
        VALUES (?, ?, ?)
    """, (product.name, product.price, product.category))
    conn.commit()

def save_sale(sales):
    cursor.execute("""
    INSERT INTO sales (product_name, quantity, total, date)
    VALUES (?, ?, ?, ?)
    """, (sales.product.name, sales.quantity, sales.total, sales.date))
    conn.commit()

def get_all_products():
    cursor.execute("SELECT * FROM products")
    return cursor.fetchall()

def get_all_sales():
    cursor.execute("SELECT * FROM sales")
    return cursor.fetchall()