import os
from flask import Flask, request, render_template
from recommender import get_book_recommendations

app = Flask(__name__)
app.secret_key = "my_secret_key_for_flask"

@app.route("/", methods=["GET", "POST"])
def home():
    books = []
    user_query = ""

    if request.method == "POST":
        user_query = request.form.get("query")
        if user_query:
            books = get_book_recommendations(user_query)
    return render_template("index.html", books=books, query=user_query)

if __name__ == "__main__":
    app.run(debug=True)