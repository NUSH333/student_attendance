import cv2
import os
import numpy as np

def train():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    faces = []
    ids = []

    dataset_path = 'dataset'

    for student_folder in os.listdir(dataset_path):
        path = os.path.join(dataset_path, student_folder)
        if not os.path.isdir(path):
            continue
        try:
            student_id = int(student_folder.split('_')[0])
        except ValueError:
            print(f"Skipping folder {student_folder}, cannot extract ID")
            continue

        # Debug print - folder and ID found
        print(f"Found folder: {student_folder}, ID: {student_id}, processing images...")

        for image_name in os.listdir(path):
            image_path = os.path.join(path, image_name)
            # Debug print - image being processed
            print(f"Processing image: {image_path}")

            img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
            if img is None:
                print(f"Warning: Could not read image {image_path}")
                continue

            faces_rects = detector.detectMultiScale(img)
            for (x, y, w, h) in faces_rects:
                faces.append(img[y:y+h, x:x+w])
                ids.append(student_id)

    if len(faces) == 0:
        print("No faces found for training!")
        return

    recognizer.train(faces, np.array(ids))
    os.makedirs('trainer', exist_ok=True)
    recognizer.save('trainer/trainer.yml')
    print(f"Training complete. {len(set(ids))} students trained.")

if __name__ == "__main__":
    train()
