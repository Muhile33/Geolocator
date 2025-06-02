import instaloader
from color_utils.printx import print_success, print_error, print_info

def instagram_recon(username):
    print_info(f"Fetching Instagram data for: {username}")
    L = instaloader.Instaloader()
    try:
        profile = instaloader.Profile.from_username(L.context, username)
    except Exception as e:
        print_error(f"Failed to fetch profile: {e}")
        return None
    
    data = {
        "Username": profile.username,
        "Full Name": profile.full_name,
        "Bio": profile.biography,
        "Followers": profile.followers,
        "Following": profile.followees,
        "Posts": profile.mediacount,
        "External URL": profile.external_url,
        "Is Private": profile.is_private,
        "Is Verified": profile.is_verified,
    }
    print_success(f"Data fetched successfully for {username}")
    return data

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python instagram_recon.py <instagram_username>")
        sys.exit(1)
    username = sys.argv[1]
    info = instagram_recon(username)
    if info:
        for k, v in info.items():
            print(f"{k}: {v}")

