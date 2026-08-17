import os
from flask import Flask
from database import get_all_books, get_stats, save_book
from analysis import analyze_books
from scraper import scrape_books
import pandas as pd

template_dir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__, template_folder=template_dir + '/templates', static_folder=template_dir + '/static')

def initialize_data():
    df = scrape_books(3)
    df['price'] = df['price'].apply(lambda x: float(x.replace('Â£', '').replace('£', '').strip()))
    rating_map = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}
    df['rating_num'] = df['rating'].map(rating_map)
    save_book(df)

initialize_data()

@app.route('/')
def index():
    stats = get_stats()
    avg = round(float(stats['avg_price'][0]), 2) if stats['avg_price'][0] else 0
    total = int(stats['total_books'][0]) if stats['total_books'][0] else 0
    return f"""
    <html>
    <body style="background:#1e1e2e; color:white; font-family:Arial; padding:20px">
    <h1>📚 E-commerce Analytics Platform</h1>
    <a href="/products" style="color:#00d4ff">Products</a> | 
    <a href="/insights" style="color:#00d4ff">Insights</a>
    <h2>Total Books: {total}</h2>
    <h2>Average Price: £{avg}</h2>
    </body>
    </html>
    """

@app.route('/products')
def products():
    books = get_all_books()
    rows = ""
    for _, book in books.iterrows():
        rows += f"<tr><td>{book['title']}</td><td>£{book['price']}</td><td>{book['rating']}</td></tr>"
    return f"""
    <html>
    <body style="background:#1e1e2e; color:white; font-family:Arial; padding:20px">
    <h1>📚 All Books</h1>
    <a href="/" style="color:#00d4ff">Home</a> | 
    <a href="/insights" style="color:#00d4ff">Insights</a>
    <table border="1" style="width:100%; margin-top:20px">
    <tr><th>Title</th><th>Price</th><th>Rating</th></tr>
    {rows}
    </table>
    </body>
    </html>
    """

@app.route('/insights')
def insights():
    expensive, rated = analyze_books()
    exp_rows = ""
    for _, book in expensive.iterrows():
        exp_rows += f"<tr><td>{book['title']}</td><td>£{book['price']}</td></tr>"
    rated_rows = ""
    for _, book in rated.iterrows():
        rated_rows += f"<tr><td>{book['title']}</td><td>{book['rating_num']}/5</td></tr>"
    return f"""
    <html>
    <body style="background:#1e1e2e; color:white; font-family:Arial; padding:20px">
    <h1>📊 Insights</h1>
    <a href="/" style="color:#00d4ff">Home</a> | 
    <a href="/products" style="color:#00d4ff">Products</a>
    <h2>💰 Top 5 Most Expensive</h2>
    <table border="1"><tr><th>Title</th><th>Price</th></tr>{exp_rows}</table>
    <h2>⭐ Top 5 Highest Rated</h2>
    <table border="1"><tr><th>Title</th><th>Rating</th></tr>{rated_rows}</table>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True, port=8080)