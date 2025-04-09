import random
import requests

def get_random_user_agent():
    """Return a random user-agent from a predefined list."""
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0"
    ]
    return random.choice(user_agents)

def safe_get(url, headers=None):
    """Send a GET request with a safe timeout and error handling."""
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # Raise an exception for 4xx/5xx responses
        return response
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

def print_pretty(data):
    """Print data in a human-readable format (for debugging)."""
    print("\n" + "="*50)
    print(data)
    print("="*50 + "\n")
