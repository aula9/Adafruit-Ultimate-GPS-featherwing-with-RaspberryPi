import folium

# List of coordinates (latitude, longitude) representing the route
# NOTE: This list can be dynamically updated using GPS data from the previous code.
#       For example, after extracting latitude and longitude from the NMEA string:
#           lat = convert_to_degrees(float(nmea_latitude))
#           longi = convert_to_degrees(float(nmea_longitude))
#       You can append the new point like this:
#           route.append((float(lat), float(longi)))


# List of coordinates (latitude, longitude) representing the route
route = [
    (34.7304, 36.7097),
    (34.7310, 36.7105),
    (34.7322, 36.7120),
    (34.7330, 36.7135),
    (34.7340, 36.7150)
]

# Create a map centered at the first coordinate in the route
map = folium.Map(location=route[0], zoom_start=15)

# Draw the route as a blue polyline on the map
folium.PolyLine(route, color="blue", weight=5).add_to(map)

# Display the map directly in Google Colab
map
