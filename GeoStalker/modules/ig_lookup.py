import instaloader

def lookup_instagram_profile(username):
    L = instaloader.Instaloader()
    profile = instaloader.Profile.from_username(L.context, username)
    
    profile_info = {
        "username": profile.username,
        "full_name": profile.full_name,
        "bio": profile.biography,
        "followers": profile.followers,
        "following": profile.followees,
        "posts": profile.mediacount,
        "private": profile.is_private,
    }

    return profile_info
