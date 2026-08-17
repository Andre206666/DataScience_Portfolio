# 📚 AI Book Recommender (RAG System)

A full-stack web application that uses Google's Gemini AI to act as a smart librarian. Instead of relying on general internet knowledge, the application uses **Retrieval-Augmented Generation (RAG)** to recommend books strictly from a local SQLite database inventory based on the user's natural language queries.

## 🚀 Key Features

* **RAG Architecture:** The AI is constrained to a specific local database (SQLite), preventing hallucinations and ensuring only available inventory is recommended.
* **Structured AI Outputs:** Utilizes **Pydantic** to force the LLM to return strict, predictable JSON data, making it reliable for frontend rendering.
* **Full-Stack Integration:** Built with a **Flask** backend that communicates with the Gemini API and serves a responsive UI styled with **TailwindCSS**.
* **Secure Configuration:** Uses `python-dotenv` to securely manage API keys.

## 🛠️ Tech Stack

* **Backend:** Python, Flask, SQLite
* **AI / LLM:** Google GenAI SDK (`gemini-flash-latest`), Pydantic
* **Frontend:** HTML5, TailwindCSS (CDN)

## ⚙️ How to Run Locally

### 1. Clone the repository and navigate to the project
```bash
git clone [https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git](https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git)
cd YOUR-REPO-NAME