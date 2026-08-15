from flask import Flask, render_template
import pandas as pd
from scraper import scrape_books
from database import save_book, get_all_books, get_stats
from analysis import analyze_books

app = Flask(__name__)

@app.route('/')
def index():
    stats = get_stats()
    return render_template("index.html", stats=stats)

@app.route('/products')
def products():
    books = get_all_books()
    return render_template('products.html', books=books)

@app.route('/insights')
def insights():
    expensive, rated = analyze_books()
    return render_template('insights.html',
                         expensive=expensive,
                         rated=rated)

if __name__ == "__main__":
    app.run(debug=True, port=8080)

