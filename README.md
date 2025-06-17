# 📚 Book Data Analysis Using Web Scraping and Power BI

This project demonstrates how to collect book data through web scraping and uncover insights using data visualization tools. The dataset was extracted from [Books to Scrape](https://books.toscrape.com), a mock e-commerce site for practicing web scraping.

![Dashboard Overview](Page-1.png)
![Dashboard Detail](Page-2.png)

---

## 🛠️ Tools & Technologies

- **Python** (BeautifulSoup, Requests)
- **Power BI**
- **CSV (Data storage)**
- **Web Scraping**

---

## 🧹 Data Collection

Python was used to scrape 20 pages of the Books to Scrape website. For each book, the following fields were extracted:

- Title
- Price (in €)
- Rating (converted from star-rating classes to numbers)
- Genre (by navigating to individual book pages)

### 🔄 Script Overview
```python
from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin
import csv
