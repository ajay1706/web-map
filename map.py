import folium
map = folium.Map(location=[17.441677,78.364666],zoom_start=6,tiles="OpenStreetMap")

fg = folium.FeatureGroup(name="My Map")
for cordinates in [[17.441677,78.364666],[17.651677,78.408666],]:
    fg.add_child(folium.Marker(location = cordinates,popup="Hostel",icon=folium.Icon(color='green')))

map.add_child(fg)

map.save("Map1.html")

