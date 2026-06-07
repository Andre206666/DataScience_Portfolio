from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

def get_db():
    conn = sqlite3.connect('../06_sales_anayltic_system/sales.db')
    return conn

@app.route('/')
def home():
    return "Welcome to sales API"

@app.route('/products')
def products():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    data = cursor.fetchall()
    return jsonify(data)

@app.route('/sales')
def sales():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM sales")
    data = cursor.fetchall()
    return jsonify(data)

@app.route('/analysis')
def analysis():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT SUM(total), COUNT(*), AVG(total) FROM sales")
    data = cursor.fetchone()  # gets one row instead of list of rows
    return jsonify({
        "total_revenue": data[0],
        "total_sales": data[1],
        "average_sale": data[2]
    })



if __name__ == '__main__':
    app.run(debug=True, port=8080)