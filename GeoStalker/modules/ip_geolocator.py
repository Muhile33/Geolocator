import requests

def locate_ip(ip):
    print(f"[+] Geolocating IP: {ip}")
    try:
        res = requests.get(f"https://ipinfo.io/{ip}/json")
        data = res.json()
        for key, value in data.items():
            print(f"{key.title():15}: {value}")
    except Exception as e:
        print(f"[!] Failed to geolocate IP: {e}")
