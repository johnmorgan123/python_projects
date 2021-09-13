import requests
from bs4 import BeautifulSoup

r = requests.get("https://pythonizing.github.io/data/real-estate/rock-springs-wy/LCWYROCKSPRINGS/", headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
c = r.content

soup = BeautifulSoup(c, "html.parser")

all = soup.find_all("div", {"class":"propertyRow"})
all[0].find("h4", {"class":"propPrice"}).text.replace("\n","").replace(" ","")

for item in all:
    print(item.find("h4", {"class":"propPrice"}).text.replace("\n","").replace(" ",""))
    print(item.find_all("span", {"class":"propAddressCollapse"})[0].text)
    print(item.find_all("span", {"class":"propAddressCollapse"})[1].text)
    try:
        print(item.find("span", {"class":"infoBed"}).find("b").text)
    except:
        print(None)

    try:
        print(item.find("span", {"class":"infoSqFt"}).find("b").text)
    except:
        print(None)

    try:
        print(item.find("span", {"class": "infoValueFullBath"}).find("b").text)
    except:
        print(None)

    try:
        print(item.find("span", {"class":"infoValueHalfBath"}).find("b").text)
    except:
        print(None)

    for column_group in item.find_all("div",{"class":"columnGroup"}):
        print(column_group)
        for feature_group, feature_name in zip(column_group.find_all("span", {"class":"featureGroup"}), column_group.find_all("span", {"class":"featureName"})):
            print(feature_group.text, feature_name.text)
            if "Lot Size" in feature_group.text:
                print(feature_name.text)
    print("")