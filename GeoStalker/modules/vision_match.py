import face_recognition

def compare_faces(image1, image2):
    print(f"[+] Comparing {image1} and {image2}")
    try:
        img1 = face_recognition.load_image_file(image1)
        img2 = face_recognition.load_image_file(image2)

        enc1 = face_recognition.face_encodings(img1)[0]
        enc2 = face_recognition.face_encodings(img2)[0]

        match = face_recognition.compare_faces([enc1], enc2)[0]
        print("[=] Match result:", "✔️ Match" if match else "❌ No Match")
    except Exception as e:
        print(f"[!] Error in face matching: {e}")