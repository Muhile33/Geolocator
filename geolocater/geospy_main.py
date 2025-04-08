import instaloader
from geopy.geocoders import Nominatim
import folium
import argparse
import os
import webbrowser
import requests
from termcolor import colored
import pyfiglet

def banner():
    ascii_banner = pyfiglet.figlet_format("GeoSpy")
    print(colored(ascii_banner, 'green'))

def geocode_location(location_name):
    geolocator = Nominatim(user_agent="geospy_instagram")
    location = geolocator.geocode(location_name)
    if location:
        return location.latitude, location.longitude
    return None, None

def show_map(lat, lon, label):
    m = folium.Map(location=[lat, lon], zoom_start=10)
    folium.Marker([lat, lon], popup=label).add_to(m)
    map_file = f"{label.replace(' ', '_')}_location_map.html"
    m.save(map_file)
    webbrowser.open('file://' + os.path.realpath(map_file))

# ===============================
# Instagram Username Handler
# ===============================
def get_instagram_locations(username):
    L = instaloader.Instaloader()
    try:
        profile = instaloader.Profile.from_username(L.context, username)
    except:
        print(colored("[!] Failed to fetch Instagram profile. Make sure it's public.", "red"))
        return []

    locations = []

    for post in profile.get_posts():
        if post.location:
            locations.append(post.location.name)

    return list(set(locations))  # remove duplicates

def locate_instagram_user(username):
    locations = get_instagram_locations(username)

    if not locations:
        print(colored("[!] No location tags found in the posts.", "red"))
        return

    print(colored(f"\n[+] Locations found for {username}:", "cyan"))
    for loc in locations:
        print(colored(f"    {loc}", "yellow"))

    print(colored("\n[+] Geolocating locations on map...", "cyan"))
    for loc in locations:
        lat, lon = geocode_location(loc)
        if lat and lon:
            print(colored(f"[+] Found coordinates for {loc}: Latitude: {lat}, Longitude: {lon}", "green"))
            show_map(lat, lon, loc)
        else:
            print(colored(f"[!] Could not geocode {loc}", "red"))

# ===============================
# IP Address Handler
# ===============================
def get_ip_data(ip):
    url = f"https://ipapi.co/{ip}/json/"
    try:
        response = requests.get(url)
        return response.json()
    except:
        return {}

def locate_ip(ip):
    data = get_ip_data(ip)

    if 'error' in data or 'latitude' not in data:
        print(colored("[!] Failed to retrieve IP data.", "red"))
        return

    lat = data['latitude']
    lon = data['longitude']
    city = data.get('city', 'Unknown City')
    country = data.get('country_name', 'Unknown Country')

    label = f"{ip} - {city}, {country}"
    print(colored(f"\n[+] IP: {ip}", "cyan"))
    print(colored(f"    Location: {city}, {country}", "yellow"))
    print(colored(f"    Latitude: {lat}, Longitude: {lon}", "yellow"))

    show_map(lat, lon, label)

# ===============================
# Main CLI Handler
# ===============================
def main():
    banner()
    parser = argparse.ArgumentParser(description="GeoSpy - Instagram/IP Geolocation OSINT Tool")
    parser.add_argument("-u", "--username", help="Instagram username to geolocate")
    parser.add_argument("-i", "--ip", help="IP address to geolocate")
    args = parser.parse_args()

    if not args.username and not args.ip:
        print(colored("[!] Please specify either --username or --ip", "red"))
        parser.print_help()
        return

    if args.username:
        print(colored(f"[+] Looking up Instagram username: {args.username}", "cyan"))
        locate_instagram_user(args.username)

    if args.ip:
        print(colored(f"[+] Looking up IP address: {args.ip}", "cyan"))
        locate_ip(args.ip)

if __name__ == "__main__":
    main()

