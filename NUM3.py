import requests
from bs4 import BeautifulSoup
base = "http://books.toscrape.com/catalogue/page-{}.html"
page = 1
all_books = []
while True:
    url = base.format(page)
    resp = requests.get(url)
    if resp.status_code != 200:
        break
    soup = BeautifulSoup(resp.text, "html.parser")
    books = soup.select("article.product_pod")
    if not books:
        break
    for b in books:
        title = b.h3.a["title"]
        price = b.select_one("p.price_color").text
        availability = b.select_one("p.instock.availability").text.strip()
        all_books.append({
            "title": title,
            "price": price,
            "availability": availability
        })
    page += 1
for book in all_books:
    print(book)
