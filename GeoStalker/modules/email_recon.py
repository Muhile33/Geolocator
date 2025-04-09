import requests

def check_email_in_hibp(email):
    """Check if the email is part of any known breaches via HaveIBeenPwned API."""
    url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}"
    headers = {
        "User-Agent": "GeoStalker",
        "hibp-api-key": "your-api-key-here"  # You will need a free API key from https://haveibeenpwned.com/API
    }

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            breaches = response.json()
            breach_info = [breach['Name'] for breach in breaches]
            return f"Email {email} found in breaches: {', '.join(breach_info)}"
        elif response.status_code == 404:
            return f"Email {email} not found in any breaches."
        else:
            return "Error while fetching breach data."
    except requests.RequestException as e:
        return f"Error checking email: {e}"

def check_domain(domain):
    """Check if the domain is linked to any social media accounts."""
    # Placeholder logic: This can be expanded with domain lookup services or APIs
    social_media_domains = ['facebook.com', 'twitter.com', 'instagram.com', 'linkedin.com']
    
    if domain in social_media_domains:
        return f"Domain {domain} is linked to a social media platform."
    else:
        return f"Domain {domain} does not seem to be linked to major social media platforms."
