import instaloader

def recon_instagram(username):
    print(f"[+] Starting Instagram recon for {username}")
    L = instaloader.Instaloader()
    try:
        profile = instaloader.Profile.from_username(L.context, username)
        print(f"Full Name: {profile.full_name}")
        print(f"Followers: {profile.followers}")
        print(f"Following: {profile.followees}")
        print(f"Posts: {profile.mediacount}")
    except Exception as e:
        print(f"[!] Failed to retrieve profile: {e}")
