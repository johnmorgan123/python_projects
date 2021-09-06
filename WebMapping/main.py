from json import load, loads
import folium
import pandas
import requests
import csv
import io

#response = requests.get("https://volcano.si.edu/includes/tdpmap/volcanoes.txt")
#response.raise_for_status()
#world_data = list(csv.DictReader(io.StringIO(response.text), dialect=csv.excel_tab))


data = pandas.read_csv("Volcanoes.txt")
world = open('world.json')

lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def colour_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'


map = folium.Map(location=[28.135480, -15.434426], zoom_start= 15, tiles = "Stamen Terrain")

fgv = folium.FeatureGroup(name="Volcanoes")
fgp = folium.FeatureGroup(name="Population")
fgs = folium.FeatureGroup(name="shite")


fgs.add_child(folium.Marker(location=[28.134297, -15.434597], popup="McDonalds", icon=folium.Icon(color='pink')))
fgs.add_child(folium.Marker(location=[28.142410, -15.429842], popup="Skate Park", icon=folium.Icon(color='darkpurple')))

for lt, ln, elev in zip(lat, lon, elev):
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius=6,  popup=str(elev) + 'm',
    fill_color=colour_producer(elev), color = 'grey', fill_opacity=0.7))

world_data = world.read()
world_data = loads(world_data[world_data.find('{'):])

fgp.add_child(folium.GeoJson(data=world_data , style_function=lambda x: {'fillColor' : 'green'
if x['properties']['POP2005'] < 10000000 else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(fgs)
map.save("map.html")



