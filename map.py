import folium
import pandas
data = pandas.read_csv("volcanoes.txt")
lat = list(data['LAT'])
lon = list(data['LON'])
elev = list(data['ELEV'])

def color_producer(elevation):
    if elevation<1500:
         return 'green'
    elif 1500<= elevation <3000:
        return 'orange'
    else:
        return 'red'

map = folium.Map(location=[38.58,-99.09],zoom_start=6,tiles="OpenStreetMap")

fg = folium.FeatureGroup(name="My Map")
for lt,ln,el in zip(lat,lon,elev):
    fg.add_child(folium.CircleMarker(location = [lt,ln],radius = 6,popup=str(el) + ' m',fill_color=color_producer(el), color = "grey", fill_opacity = 0.7))

map.add_child(fg)

map.save("Map1.html")

