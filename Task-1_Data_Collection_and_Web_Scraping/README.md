# 📚 Book Data Web Scraper

This project is part of my Data Science internship at **CODVEDA**.  
It demonstrates basic **web scraping** skills using Python to collect structured data from a website.

---

## 🔍 Task Overview

**Goal**: Scrape book information such as title, price, availability, and rating from a test e-commerce website.

**Target Website**: [books.toscrape.com](http://books.toscrape.com)

---

## 🛠️ Tools & Libraries Used

- Python
- [Requests](https://pypi.org/project/requests/)
- [BeautifulSoup (bs4)](https://pypi.org/project/beautifulsoup4/)
- [Pandas](https://pandas.pydata.org/)

---

## 📄 Features

- Scrapes data from 5 pages of the site
- Extracts the following fields:
  - Title
  - Price
  - Availability
  - Rating
- Saves data in a structured CSV format

---

## 📁 Output Sample (CSV)

| Title                     | Price  | Availability | Rating |
|--------------------------|--------|--------------|--------|
| A Light in the Attic     | £51.77 | In stock     | Three  |
| Tipping the Velvet       | £53.74 | In stock     | One    |
| Soumission               | £50.10 | In stock     | One    |
| ...                      | ...    | ...          | ...    |

---

## ▶️ How to Run

1. Install requirements:
    ```bash
    pip install requests beautifulsoup4 pandas
    ```

2. Run the script:
    ```bash
    python scrape_books.py
    ```

3. Output file: `books.csv`

---

## 📚 Learning Outcome

Through this task, I practiced:
- Inspecting web page structures using browser tools
- Using BeautifulSoup to extract specific HTML elements
- Handling pagination in scraping
- Storing scraped data using pandas

---

> 🧠 _This project was created for learning purposes as part of my internship._
