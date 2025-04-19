import requests, json, random

def search_username(username):
    with open("Data/platforms.json") as f:
        platforms = json.load(f)
    with open("Data/user_agents.txt") as f:
        agents = f.read().splitlines()

    print(f"[+] Stealth username recon for: {username}")
    for platform, data in platforms.items():
        url = data["url"].format(username)
        headers = {'User-Agent': random.choice(agents)}
        try:
            r = requests.get(url, headers=headers, timeout=5)
            if r.status_code == 200:
                print(f"[FOUND] {platform}: {url}")
            else:
                print(f"[--] {platform}: Not found")
        except:
            print(f"[!!] Error checking {platform}")

