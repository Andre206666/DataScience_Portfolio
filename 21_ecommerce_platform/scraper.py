import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_books(pages=5):
    all_books = []

    for page in range(1, pages + 1):
        url = f"http://books.toscrape.com/catalogue/page-{page}.html"

        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        books = soup.find_all("article", class_="product_pod")

        for book in books:
            title = book.h3.a["title"]
            price = book.find("p", class_="price_color").text
            rating = book.p["class"][1]
            all_books.append({"title": title, "price": price, "rating": rating})

    return pd.DataFrame(all_books)

if __name__ == "__main__":
    df = scrape_books(2)
    print(df.head())
    print(df.shape)


