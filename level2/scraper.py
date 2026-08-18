import requests
from bs4 import BeautifulSoup
import csv

url = "http://books.toscrape.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

books = soup.find_all("article", class_="product_pod")

data = []
for book in books:
    title = book.h3.a["title"]
    price = book.find("p", class_="price_color").text
    data.append({"title": title, "price": price})
    print(f"{title} - {price}")

with open("books.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["title", "price"])
    writer.writeheader()
    writer.writerows(data)

print(f"\nSaved {len(data)} books to books.csv")