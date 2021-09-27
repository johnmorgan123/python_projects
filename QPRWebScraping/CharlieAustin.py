import bs4
import requests
from dataclasses import dataclass
#print(qpr_links)

story_content = []

@dataclass
class Story:
    link: [str]
    content: [str]




def find_charlie_stories(links):
    stories = []
    for link in links:
        page = requests.get(link)
        soup = bs4.BeautifulSoup(page.text, "lxml")
        for item in soup:
            if 'Warburton' in item.text:
                stories.append(Story(
                    link=link,
                    content=cleanup_story(item.text)
                ))

    return stories


def cleanup_story(text):
    text = text.replace("\n", " ")
    text = text.replace("©", '')
    return text



def send_charlie_stories(stories):
    for story in stories:
        pass





if __name__ == '__main__':
    print(find_charlie_stories(['https://www.westlondonsport.com/qpr/gallen-qpr-should-switch-barbet-and-play-dunne-if-mccallums-injury-keeps-him-out']))


