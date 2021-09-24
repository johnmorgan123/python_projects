from dataclasses import dataclass
import requests
import bs4
import json
import smtplib
import getpass


@dataclass
class Links:
    qpr: [str]
    scum: [str]


class Links2:
    def __init__(self, qpr, scum):
        self.qpr = qpr
        self.scum = scum


def find_links(url):
    page = requests.get(url)
    soup = bs4.BeautifulSoup(page.text, "lxml")

    links = [a["href"] for a in soup.find_all("a", href=True)]
    return links


def sort_links(all_links):
    qpr_links = []
    scumbag_links = []
    for link in all_links:
        if 'qpr' in link:
            qpr_links.append(link)
        if 'chelsea' in link:
            scumbag_links.append(link)

    print("QPR links:", ", ".join(qpr_links))
    print("scumbag links:", ", ".join(scumbag_links))

    return Links(qpr_links, scumbag_links)

def convert_list(links):
    return json.dumps(links)

def send_email(links):
    smtp_object = smtplib.SMTP('smtp.gmail.com', 587)
    smtp_object.ehlo()
    smtp_object.starttls()

    email = getpass.getpass("Email: ")
    password = getpass.getpass("Password: ")
    smtp_object.login(email, password)
    from_adress = email
    to_adress = 'johnmorgan258@gmail.com'

    subjectqpr = "Here's the QPR links Chris!"
    subjectscum = "Here's links to ScumBag articles:"


    messageqpr = convert_list(links.qpr)
    messagescum = convert_list(links.scum)

    msgqpr = "Subject: "+subjectqpr+'\n'+messageqpr
    msgscum = "Subject: "+subjectqpr+'\n'+messagescum

    smtp_object.sendmail(from_adress, to_adress, msgqpr)
    smtp_object.sendmail(from_adress, to_adress, msgscum)
    smtp_object.quit()

def main():
     links = find_links("https://www.westlondonsport.com/")
     sorted_links = sort_links(links)
     send_email(sorted_links)


if __name__ == '__main__':
    main()


