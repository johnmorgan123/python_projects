import requests
import bs4

result = requests.get("https://en.wikipedia.org/wiki/Queens_Park_Rangers_F.C.")
print(type(result))
#print(result.text)

soup = bs4.BeautifulSoup(result.text, "lxml") #creates a soup that python can easily take from
#print(soup)


page_title = soup.select('title')[0].getText()#converts to a string
print(page_title)
site_paragraphs = soup.select('p')[0].getText()
type(site_paragraphs[0])

res = requests.get("https://en.wikipedia.org/wiki/Queens_Park_Rangers_F.C.")

