import folium
map = folium.Map(location=[17.441677,78.364666],zoom_start=6,tiles="OpenStreetMap")

fg = folium.FeatureGroup(name="My Map")

fg.add_child(folium.Marker(location = [17.441677,78.364666],popup="Hostel",icon=folium.Icon(color='green')))

map.add_child(fg)

map.save("Map1.html")

