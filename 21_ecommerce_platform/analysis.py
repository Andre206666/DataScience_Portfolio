import pandas as pd
from database import get_all_books

def analyze_books():
    df = get_all_books()

    top_expensive = df.sort_values("price", ascending=False).head(5)

    top_rated = df.sort_values("rating_num", ascending=False).head(5)

    return top_expensive, top_rated

if __name__ == "__main__":
    expensive, rated = analyze_books()
    print(f"\n Top 5 most expensive")
    print(expensive[["title", "price"]])
    print(f"\n Top 5 Highest Rated")
    print(rated[["title", "rating_num"]])

