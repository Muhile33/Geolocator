import face_recognition
import cv2
from color_utils.printx import print_success, print_error, print_info

def face_match(known_image_path, unknown_image_path):
    print_info("Loading images...")
    known_image = face_recognition.load_image_file(known_image_path)
    unknown_image = face_recognition.load_image_file(unknown_image_path)

    print_info("Encoding known image...")
    known_encodings = face_recognition.face_encodings(known_image)
    if not known_encodings:
        print_error("No face found in known image.")
        return False
    known_encoding = known_encodings[0]

    print_info("Encoding unknown image...")
    unknown_encodings = face_recognition.face_encodings(unknown_image)
    if not unknown_encodings:
        print_error("No face found in unknown image.")
        return False
    unknown_encoding = unknown_encodings[0]

    results = face_recognition.compare_faces([known_encoding], unknown_encoding)
    if results[0]:
        print_success("Faces MATCH!")
        return True
    else:
        print_error("Faces DO NOT match.")
        return False

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python face_match.py <known_image> <unknown_image>")
        sys.exit(1)
    known_img = sys.argv[1]
    unknown_img = sys.argv[2]
    face_match(known_img, unknown_img)
