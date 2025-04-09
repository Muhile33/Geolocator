from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

def extract_geotag(image_path):
    def get_decimal(coord, ref):
        degrees, minutes, seconds = coord
        decimal = float(degrees[0]) + float(minutes[0]) / 60 + float(seconds[0]) / 3600
        if ref in ['S', 'W']:
            decimal = -decimal
        return decimal

    img = Image.open(image_path)
    exif_data = img._getexif()
    gps_data = {}
    
    if not exif_data:
        return None
    
    for tag, val in exif_data.items():
        tag_name = TAGS.get(tag, tag)
        if tag_name == "GPSInfo":
            for key in val:
                decode = GPSTAGS.get(key, key)
                gps_data[decode] = val[key]

    if "GPSLatitude" in gps_data and "GPSLongitude" in gps_data:
        lat = get_decimal(gps_data["GPSLatitude"], gps_data.get("GPSLatitudeRef", "N"))
        lon = get_decimal(gps_data["GPSLongitude"], gps_data.get("GPSLongitudeRef", "E"))
        return lat, lon
    return None
