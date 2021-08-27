import requests
import bs4

res = requests.get("https://en.wikipedia.org/wiki/Queens_Park_Rangers_F.C.")
soup = bs4.BeautifulSoup(res.text, "lxml")

first_item = soup.select('.toctext')[0]
print(first_item.text)

for i in soup.select('.toctext'):
    print(i.text)
