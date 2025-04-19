import cv2
import os

def process_drone_images(folder_path):
    print(f"[+] Processing drone images in {folder_path}")
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            img_path = os.path.join(folder_path, filename)
            img = cv2.imread(img_path)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            edges = cv2.Canny(gray, 50, 150)
            output_path = os.path.join(folder_path, f"edge_{filename}")
            cv2.imwrite(output_path, edges)
            print(f"[+] Saved: {output_path}")
