import bs4
import requests
from dataclasses import dataclass
#print(qpr_links)

@dataclass
class Story:
    link: [str]
    content: [str]




def find_charlie_stories(links):
    charlie_links = []
    for link in links:
        page = requests.get(link)
        soup = bs4.BeautifulSoup(page.text, "lxml")
        for item in soup:
            if 'Warburton' in item.text:
                charlie_links.append(link)
                return Story(
                    link=link,
                    content=item.text
                )

    return charlie_links

def send_charlie_stories(stories):
    for story in stories:
        pass





if __name__ == '__main__':
    print(find_charlie_stories(['https://www.westlondonsport.com/qpr/gallen-qpr-should-switch-barbet-and-play-dunne-if-mccallums-injury-keeps-him-out']))