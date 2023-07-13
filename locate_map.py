from geopy.geocoders import Nominatim
import folium
import os

def locate(coordinates):
    geolocator = Nominatim(user_agent="my_app")
    map = folium.Map(location=coordinates[0][0], zoom_start=3, min_zoom=3,
    control_scale=True, tiles='OpenStreetMap')

    for coord in coordinates[0]:
        location = geolocator.reverse(coord, exactly_one=True)
        if location:
            address = location.address
        else:
            address = "Unknown Address"

        folium.Marker(
            location=coord,
            popup=address,
            icon=folium.Icon(color="blue", icon="microchip", prefix='fa')
        ).add_to(map)

    for coord in coordinates[1]:
        location = geolocator.reverse(coord, exactly_one=True)
        if location:
            address = location.address
        else:
            address = "Unknown Address"

        folium.Marker(
            location=coord,
            popup=address,
            icon=folium.Icon(color="red", icon="ship", prefix='fa')
        ).add_to(map)

    current_dir = os.getcwd()

    map_storage_dir = os.path.join(current_dir, "maps")
    if not os.path.exists(map_storage_dir):
        os.makedirs(map_storage_dir)

    map.save(os.path.join(map_storage_dir, "map.html"))