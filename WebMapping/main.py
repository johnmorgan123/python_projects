import folium
import pandas
import requests
import csv
import io

response = requests.get("https://volcano.si.edu/includes/tdpmap/volcanoes.txt")
response.raise_for_status()
world_data = list(csv.DictReader(io.StringIO(response.text), dialect=csv.excel_tab))


data = pandas.read_csv("Volcanoes.txt")
for item in world_data:
    lat = list(item["LAT"])
    lon = list(item["LONG"])

map = folium.Map(location=[28.135480, -15.434426], zoom_start= 15, tiles = "Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")


fg.add_child(folium.Marker(location=[28.134297, -15.434597], popup="McDonalds", icon=folium.Icon(color='green')))
fg.add_child(folium.Marker(location=[28.142410, -15.429842], popup="Skate Park", icon=folium.Icon(color='red')))

for lt, ln in zip(lat, lon):
    fg.add_child(folium.Marker(location=[lt, ln], popup="markers", icon=folium.Icon(color='blue')))

map.add_child(fg)

map.save("map.html")



