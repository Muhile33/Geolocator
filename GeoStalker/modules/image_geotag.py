from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

def get_exif_data(image_path):
    image = Image.open(image_path)
    image.verify()
    return image._getexif()

def trace_image(path):
    print(f"[+] Analyzing image: {path}")
    exif = get_exif_data(path)
    if not exif:
        print("[-] No EXIF data found.")
        return
    for tag, value in exif.items():
        tag_name = TAGS.get(tag, tag)
        print(f"{tag_name:25}: {value}")
