from dataclasses import dataclass
import requests
import bs4
import json
import smtplib
import getpass

from CharlieAustin import send_charlie_stories


@dataclass
class Links:
    qpr: [str]
    scum: [str]


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
    return ', '.join(links)

def send_email(links):
    smtp_object = smtplib.SMTP('smtp.gmail.com', 587)
    smtp_object.ehlo()
    smtp_object.starttls()

    email = getpass.getpass("Email: ")
    password = getpass.getpass("Password: ")
    smtp_object.login(email, password)
    from_adress = email
    to_adress = 'cmorgan@abamaxa.com'

    subjectqpr = "Here's the QPR links Chris!"
    subjectscum = "Here's links to ScumBag articles:"

    messageqpr = convert_list(links.qpr)
    messagescum = convert_list(links.scum)

    msgqpr = "Subject: "+subjectqpr+'\n'+messageqpr
    msgscum = "Subject: "+subjectscum+'\n'+messagescum

    smtp_object.sendmail(from_adress, to_adress, msgqpr)
    smtp_object.sendmail(from_adress, to_adress, msgscum)
    smtp_object.quit()


def main():
    links = find_links("https://www.westlondonsport.com/")
    sorted_links = sort_links(links)
    # send_email(sorted_links)
    send_charlie_stories(sorted_links.qpr)


@dataclass
class WeedOrder:
    strain: str
    buyer_id: str
    quantity: float
    price: float


def get_weed_order_1():
    return WeedOrder(
        strain='dank',
        quantity=5.5,
        buyer_id='john',
        price=23.00
    )


def get_weed_order_2():
    return ('dank', 'john', 5.5, 23.00)


if __name__ == '__main__':
    order1 = get_weed_order_1()
    order2 = get_weed_order_2()

    print(order1.price)
    print(order2[3])

    main()


