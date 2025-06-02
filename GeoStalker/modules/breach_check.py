import requests
from color_utils.printx import print_success, print_error, print_info

HIBP_API = "https://haveibeenpwned.com/api/v3/breachedaccount/{}"
USER_AGENT = "GeoStalker"

def email_breach_check(email, api_key=None):
    headers = {
        "User-Agent": USER_AGENT
    }
    if api_key:
        headers["hibp-api-key"] = api_key
    print_info(f"Checking breaches for: {email}")
    try:
        resp = requests.get(HIBP_API.format(email), headers=headers)
        if resp.status_code == 200:
            breaches = resp.json()
            print_success(f"Found {len(breaches)} breaches for {email}")
            return breaches
        elif resp.status_code == 404:
            print_success(f"No breaches found for {email}")
            return []
        else:
            print_error(f"Error: HTTP {resp.status_code}")
            return None
    except Exception as e:
        print_error(f"Exception: {e}")
        return None

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python email_breach.py <email> [hibp_api_key]")
        sys.exit(1)
    email = sys.argv[1]
    key = sys.argv[2] if len(sys.argv) > 2 else None
    breaches = email_breach_check(email, key)
    if breaches is not None:
        for breach in breaches:
            print(f"- {breach['Name']}: {breach['Title']}")
