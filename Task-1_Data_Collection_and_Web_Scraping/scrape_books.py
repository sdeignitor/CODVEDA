import requests
from bs4 import BeautifulSoup
import pandas as pd

base_url = "http://books.toscrape.com/catalogue/page-{}.html"
all_books = []

for page in range(1, 6):  # Pages 1 to 5
    url = base_url.format(page)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    books = soup.find_all('article', class_='product_pod')
    print(f"Scraping page {page}, found {len(books)} books")

    if not books:
        print(f"No books found on page {page}")
        continue

    for book in books:
        title = book.h3.a['title']
        price = book.find('p', class_='price_color').text
        availability = book.find('p', class_='instock availability').text.strip()
        rating = book.find('p', class_='star-rating')['class'][1]  # ✅ FIXED

        all_books.append({
            'Title': title,
            'Price': price,
            'Availability': availability,
            'Rating': rating
        })

# Save to CSV
df = pd.DataFrame(all_books)
df.to_csv('books.csv', index=False)

print("✅ Scraping complete. Data saved to 'books.csv'")


