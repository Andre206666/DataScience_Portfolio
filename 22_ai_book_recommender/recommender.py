import os
import json
import sqlite3
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from google import genai
from google.genai import types

current_folder = os.path.dirname(os.path.abspath(__file__))
env_path = os.path.join(current_folder, ".env")
load_dotenv(env_path)


class Book(BaseModel):
    title: str = Field(description="The title of the book")
    author: str = Field(description="The author of the book")
    genre: str = Field(description="The main genre of the book")
    summary: str = Field(description="A short 2-sentence summary of the plot")
    reason: str = Field(description="Why this book matches the user's request")


class BookList(BaseModel):
    recommendations: list[Book]


def get_inventory_from_db():
    """Reads all books from the SQLite database and returns them as a single string."""
    try:
        conn = sqlite3.connect('books.db')
        cursor = conn.cursor()
        cursor.execute("SELECT title, author, genre, description FROM books")
        rows = cursor.fetchall()
        conn.close()

        inventory_text = ""
        for row in rows:
            inventory_text += f"- Title: {row[0]}, Author: {row[1]}, Genre: {row[2]}, Plot: {row[3]}\n"
        return inventory_text
    except Exception as e:
        print(f"Database error: {e}")
        return ""


def get_book_recommendations(user_query):
    api_key = os.getenv("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    database_inventory = get_inventory_from_db()

    prompt = f"""
    You are an expert librarian recommending books from a specific store inventory.

    The user is asking for: "{user_query}"

    Here is our current store database inventory:
    {database_inventory}

    INSTRUCTIONS:
    1. Recommend up to 3 books that best fit the user's request.
    2. You MUST ONLY recommend books from the database inventory provided above. Do not invent books or recommend books not on the list.
    3. If none of the books fit well, recommend the closest match and explain why.
    """

    print("Asking Gemini to search the local database...")

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=BookList,
            temperature=0.3,
        ),
    )

    data = json.loads(response.text)
    return data.get("recommendations", [])

if __name__ == "__main__":
    books = get_book_recommendations("A book about being stranded in space")
    for book in books:
        print(f"\nTitle: {book['title']}")
        print(f"Author: {book['author']}")
        print(f"Summary: {book['summary']}")