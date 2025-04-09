import argparse
import sys
from modules.ig_lookup import lookup_instagram_profile
from modules.geo_photo import extract_geotag
from modules.webcam_trace import trace_webcam_from_ig
from modules.report_gen import generate_report
from modules.tor_proxy import use_tor_proxy
from modules.vision_match import match_face

def parse_args():
    parser = argparse.ArgumentParser(description="GeoStalker OSINT Tool")
    parser.add_argument('--target', required=True, help="Target username or email")
    parser.add_argument('--platform', required=True, choices=['instagram', 'email'], help="Platform to target (Instagram or Email)")
    parser.add_argument('--type', required=True, choices=['trace', 'report', 'proxy', 'vision'], help="Action type")
    parser.add_argument('--output', choices=['pdf', 'html'], help="Output format for reports (only for report action)")
    parser.add_argument('--mode', choices=['face_match', 'scene_match'], help="Face/Scene matching mode (only for vision action)")
    return parser.parse_args()

def main():
    args = parse_args()
    
    if args.type == "trace":
        if args.platform == "instagram":
            print(trace_webcam_from_ig(args.target))
        # Other platforms can be added later
    
    elif args.type == "report":
        if args.platform == "instagram":
            result = trace_webcam_from_ig(args.target)
            if args.output:
                generate_report(result, output_format=args.output)
    
    elif args.type == "proxy":
        use_tor_proxy()

    elif args.type == "vision":
        if args.mode == "face_match":
            match_face(args.target)  # For future face/scene matching

if __name__ == "__main__":
    main()
