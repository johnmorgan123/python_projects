import requests
import bs4

res = requests.get("https://www.abamaxa.com/")
soup = bs4.BeautifulSoup(res.text, 'lxml')

logo = soup.select('img')[0]
logosrc = logo['src']

print(logosrc)
image_link = requests.get('https://www.abamaxa.com/static/logo/abamaxa_logo_small2.png')

f = open('abamaxalogo.png', 'wb')
f.write(image_link.content)
f.close()