
from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin
import csv

base_url = 'https://books.toscrape.com/catalogue/page-{}.html'

with open('bookstoscrape.csv', 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Title', 'Price', 'Ratings', 'Genre'])  # Write header once

    for page in range(1, 21):
        url = base_url.format(page)
        source = requests.get(url)
        soup = BeautifulSoup(source.text, 'lxml')

        books = soup.find_all('li', class_='col-xs-6 col-sm-4 col-md-3 col-lg-3')

        for book in books:
            title = book.h3.a['title']
            price = book.find('p', class_='price_color').text.strip()

            rating_tag = book.find('p', class_='star-rating')
            rating_class = rating_tag['class'][1]
            rating_map = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}
            ratings = rating_map.get(rating_class, 0)

            relative_url = book.h3.a['href']
            book_url = urljoin('http://books.toscrape.com/catalogue/', relative_url)

            book_page = requests.get(book_url).text
            book_soup = BeautifulSoup(book_page, 'lxml')
            breadcrumb = book_soup.find('ul', class_='breadcrumb')
            genre = breadcrumb.find_all('li')[2].text.strip()

            csv_writer.writerow([title, price, ratings, genre])

        print(f"Page {page} scraped successfully.")
