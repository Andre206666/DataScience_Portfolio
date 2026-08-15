import os
from flask import Flask, render_template
import pandas as pd
from database import get_all_books, get_stats
from analysis import analyze_books

template_dir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__, template_folder=template_dir + '/templates', static_folder=template_dir + '/static')

@app.route('/')
def index():
    stats = get_stats()
    return f"""
    <html>
    <body style="background:#1e1e2e; color:white; font-family:Arial; padding:20px">
    <h1>📚 E-commerce Analytics Platform</h1>
    <a href="/products" style="color:#00d4ff">Products</a> | 
    <a href="/insights" style="color:#00d4ff">Insights</a>
    <h2>Total Books: {stats['total_books'][0]}</h2>
    <h2>Average Price: £{round(stats['avg_price'][0], 2)}</h2>
    </body>
    </html>
    """

@app.route('/products')
def products():
    books = get_all_books()
    return render_template('products.html', books=books)

@app.route('/insights')
def insights():
    expensive, rated = analyze_books()
    return render_template('insights.html', expensive=expensive, rated=rated)

if __name__ == "__main__":
    app.run(debug=True, port=8080)