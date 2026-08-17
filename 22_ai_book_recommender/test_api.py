import os
from dotenv import load_dotenv
from google import genai

current_folder = os.path.dirname(os.path.abspath(__file__))
env_path = os.path.join(current_folder, ".env")

load_dotenv(env_path)
api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

print("Connecting to Gemini...")

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="Name exactly 3 classic science fiction books. Just the titles."
)

print("\nGemini Response:")
print(response.text)