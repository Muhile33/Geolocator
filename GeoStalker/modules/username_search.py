import requests
from color_utils.printx import print_success, print_error, print_info
import json
import os

PLATFORMS_FILE = os.path.join(os.path.dirname(__file__), '../data/platforms.json')

def load_platforms():
    try:
        with open(PLATFORMS_FILE) as f:
            return json.load(f)
    except Exception as e:
        print_error(f"Failed to load platforms.json: {e}")
        return {}

def username_lookup(username):
    platforms = load_platforms()
    results = {}
    print_info(f"Searching username '{username}' on platforms...")
    for platform in platforms.get("platforms", []):
        url = platform.get("url").replace("{username}", username)
        try:
            r = requests.get(url)
            if r.status_code == 200:
                results[platform["name"]] = url
                print_success(f"Found on {platform['name']}: {url}")
            else:
                print_info(f"Not found on {platform['name']}")
        except Exception as e:
            print_error(f"Error checking {platform['name']}: {e}")
    return results

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python username_lookup.py <username>")
        sys.exit(1)
    uname = sys.argv[1]
    username_lookup(uname)
