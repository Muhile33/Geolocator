import webbrowser
from geopy.geocoders import Nominatim

def trace_webcam_from_ig(username):
    # Assume we have a method to download an IG image and extract geotag
    image_path = download_latest_ig_post(username)
    gps = extract_geotag(image_path)
    
    if gps:
        lat, lon = gps
        locator = Nominatim(user_agent="GeoStalker")
        location = locator.reverse((lat, lon), language='en')
        
        print(f"[+] Possible location: {location.address}")
        find_nearby_webcams(lat, lon)
        return f"[✓] Traced location: {location.address} with coordinates: {lat}, {lon}"
    
    return "[x] No geotag found in Instagram photo."

def find_nearby_webcams(lat, lon):
    # A mock method to simulate webcam search by geolocation
    print(f"Searching for webcams near {lat}, {lon}...")
    webbrowser.open(f"https://www.insecam.org/en/bycountry/")  # Open the insecam webpage
