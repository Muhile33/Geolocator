import argparse
from modules import (
    Instagram_recon, ip_geolocator, image_geotag, vision_match, tor_proxy,
    report_gen, discord_telegram_recon, map_view, drone_recon,
    username_search, breach_check
)

parser = argparse.ArgumentParser(description="GeoStalker - OSINT Recon Tool")

parser.add_argument("--insta", help="Instagram username")
parser.add_argument("--ip", help="IP address")
parser.add_argument("--image", help="Path to image with EXIF")
parser.add_argument("--match", nargs=2, help="Compare 2 faces/images")
parser.add_argument("--tor", help="Use Tor to access a URL")
parser.add_argument("--report", action="store_true", help="Generate PDF Report")
parser.add_argument("--discord", help="Discord tag")
parser.add_argument("--telegram", help="Telegram @username")
parser.add_argument("--map", nargs=2, help="Generate map from lat lon")
parser.add_argument("--drone", help="Folder path with drone images")
parser.add_argument("--username", help="Username to scan across platforms")
parser.add_argument("--breach", help="Email to check breach status")

args = parser.parse_args()

if args.insta: Instagram_recon.recon_instagram(args.insta)
if args.ip: ip_geolocator.locate_ip(args.ip)
if args.image: image_geotag.trace_image(args.image)
if args.match: vision_match.compare_faces(args.match[0], args.match[1])
if args.tor: tor_proxy.tor_request(args.tor)
if args.report:
    data = {
        "Recon Summary": "Placeholder summary for now. (Fill later.)"
    }
    report_gen.generate_pdf_report(data)
if args.discord: discord_telegram_recon.recon_discord(args.discord)
if args.telegram: discord_telegram_recon.recon_telegram(args.telegram)
if args.map: map_view.create_trace_map(float(args.map[0]), float(args.map[1]))
if args.drone: drone_recon.process_drone_images(args.drone)
if args.username: username_search.search_username(args.username)
if args.breach: breach_check.check_breach(args.breach)


