# modules/cross_check.py
import aiohttp, asyncio

PLATFORMS = {
    "Twitter": "https://twitter.com/{}",
    "Facebook": "https://facebook.com/{}",
    "GitHub": "https://github.com/{}",
    "TikTok": "https://www.tiktok.com/@{}",
    # Add more...
}

async def check_platform(username):
    async with aiohttp.ClientSession() as session:
        results = {}
        for platform, url in PLATFORMS.items():
            async with session.get(url.format(username)) as res:
                results[platform] = res.status == 200
        return results
