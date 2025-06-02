import exifread
from color_utils.printx import print_success, print_error, print_info

def get_decimal_from_dms(dms, ref):
    degrees = dms.values[0].num / dms.values[0].den
    minutes = dms.values[1].num / dms.values[1].den
    seconds = dms.values[2].num / dms.values[2].den

    dec = degrees + (minutes / 60.0) + (seconds / 3600.0)
    if ref in ['S', 'W']:
        dec = -dec
    return dec

def extract_geotag(image_path):
    print_info(f"Extracting geotag from: {image_path}")
    try:
        with open(image_path, 'rb') as f:
            tags = exifread.process_file(f)
            if not tags:
                print_error("No EXIF tags found.")
                return None
            gps_latitude = tags.get('GPS GPSLatitude')
            gps_latitude_ref = tags.get('GPS GPSLatitudeRef')
            gps_longitude = tags.get('GPS GPSLongitude')
            gps_longitude_ref = tags.get('GPS GPSLongitudeRef')

            if not gps_latitude or not gps_latitude_ref or not gps_longitude or not gps_longitude_ref:
                print_error("No GPS info found in EXIF.")
                return None

            lat = get_decimal_from_dms(gps_latitude, gps_latitude_ref.values)
            lon = get_decimal_from_dms(gps_longitude, gps_longitude_ref.values)
            print_success(f"Found GPS coordinates: {lat}, {lon}")
            return (lat, lon)
    except Exception as e:
        print_error(f"Error reading EXIF: {e}")
        return None

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python image_geotag.py <image_path>")
        sys.exit(1)
    image_path = sys.argv[1]
    extract_geotag(image_path)
    if extract_geotag(image_path) is None:
        print_error("No geotag found or error extracting geotag.")
    else:
        print_success("Geotag extraction completed successfully.")
        sys.exit(0)