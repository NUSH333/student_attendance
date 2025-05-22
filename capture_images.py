import cv2
import os

def capture():
    name = input("Enter Student Name: ").strip()
    student_id = input("Enter Student ID: ").strip()

    folder_name = f"{student_id}_{name}"
    path = os.path.join("dataset", folder_name)
    os.makedirs(path, exist_ok=True)

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    cap = cv2.VideoCapture(0)

    print("Starting image capture. Press 'q' to quit early.")
    count = 0
    max_images = 50

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

        if len(faces) > 0:
            # Take the first detected face only
            (x, y, w, h) = faces[0]
            face_img = gray[y:y+h, x:x+w]

            count += 1
            img_name = os.path.join(path, f"{student_id}_{count}.jpg")
            cv2.imwrite(img_name, face_img)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        cv2.putText(frame, f"Capturing images for {name} - {student_id} ({count}/{max_images})",
                    (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

        cv2.imshow("Capture Images", frame)

        if cv2.waitKey(1) & 0xFF == ord('q') or count >= max_images:
            break

    cap.release()
    cv2.destroyAllWindows()
    print(f"Captured {count} images for {name} ({student_id})")

if __name__ == "__main__":
    capture()
