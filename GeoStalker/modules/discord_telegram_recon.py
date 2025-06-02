import requests
from color_utils.printx import print_success, print_error, print_info

def check_discord_user(user_id):
    url = f"https://discord.com/api/v9/users/{user_id}"
    try:
        r = requests.get(url)
        if r.status_code == 200:
            data = r.json()
            print_success(f"Discord user found: {data['username']}#{data['discriminator']}")
            return data
        else:
            print_error(f"Discord user not found or rate limited.")
            return None
    except Exception as e:
        print_error(f"Error querying Discord API: {e}")
        return None

def check_telegram_username(username):
    # Telegram has no public API for username lookup,
    # so this is just a placeholder for scraping or using a 3rd party API.
    print_info(f"Telegram username lookup is experimental. Cannot perform direct lookup for {username}")
    return None

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print("Usage: python discord_telegram.py <discord|telegram> <id_or_username>")
        sys.exit(1)
    platform = sys.argv[1].lower()
    identifier = sys.argv[2]
    if platform == "discord":
        check_discord_user(identifier)
    elif platform == "telegram":
        check_telegram_username(identifier)
    else:
        print("Platform must be 'discord' or 'telegram'")
