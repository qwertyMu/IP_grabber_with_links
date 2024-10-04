# Lists & Loops

import geocoder
import webbrowser

subject_IP_list = ["8.8.8.8", "1.1.1.1", "216.58.194.164", "173.0.113.110"]

for ip in subject_IP_list:
    co_ordinates = geocoder.ipinfo(ip)
    if co_ordinates.ok:
        latlng = co_ordinates.latlng  # This will be [latitude, longitude]
        if latlng:
            lat, lng = latlng
            map_url = f"https://maps.google.com/maps?q={lat},{lng}"
            print(f"{ip}: {map_url}")
            webbrowser.open(map_url)
        else:
            print(f"{ip}: Location not found")
    else:
        print(f"{ip}: Geocoding failed")