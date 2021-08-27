#getting the title of every book with a 3 star rating
import requests
import bs4

base_url = 'https://books.toscrape.com/catalogue/page-{}.html'
page_number = 13


res = requests.get(base_url.format(page_number))
soup = bs4.BeautifulSoup(res.text, 'lxml')

products = soup.select(".product_pod")
example = products[0]

#[] == example.selsect(".star-rating.Three")
title = example.select('a')[1]['title']
print(title)
print("----------")

three_star_titles = []

for i in range(1, 51):

    scrape_url = base_url.format(i)
    res = requests.get(scrape_url)

    soup = bs4.BeautifulSoup(res.text, 'lxml')
    books = soup.select(".product_pod")

    for book in books:

        if len(book.select('.star-rating.Three')) != 0:
            book_title = book.select('a')[1]['title']
            three_star_titles.append((book_title))

#print(three_star_titles)

for item in three_star_titles:
    print(item)