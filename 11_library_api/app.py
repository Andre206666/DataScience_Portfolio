from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

def get_db():
    conn = sqlite3.connect("library.db")
    return conn

@app.route('/books')
def get_books():
    conn = get_db()
    c = conn.cursor()
    c.execute("SELECT * FROM books")
    books = c.fetchall()
    return jsonify(books)

@app.route('/members')
def get_members():
    conn = get_db()
    c = conn.cursor()
    c.execute("SELECT * FROM members")
    members = c.fetchall()
    return jsonify(members)

if __name__ == '__main__':
    app.run(debug=True, port=8080)