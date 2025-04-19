import requests

def check_breach(email):
    print(f"[+] Checking breaches for {email}")
    headers = {"User-Agent": "GeoStalker"}
    url = f"https://haveibeenpwned.com/unifiedsearch/{email}"
    try:
        r = requests.get(url, headers=headers, timeout=8)
        if "No breached account" in r.text:
            print("[-] No breaches found.")
        else:
            print("[!!] Breach detected!")
            print(r.text[:500])
    except:
        print("[-] Error reaching haveibeenpwned.")
