import cv2
import numpy as np
import os
import pandas as pd
from datetime import datetime
import time

def recognize():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('trainer/trainer.yml')
    detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    student_info = {}
    for folder in os.listdir('dataset'):
        if '_' in folder:
            sid, name = folder.split('_', 1)
            try:
                student_info[int(sid)] = name
            except ValueError:
                continue

    cap = cv2.VideoCapture(0)
    attendance = {}

    print("Starting recognition...")
    start_time = time.time()
    timeout = 10  # seconds of only unknowns before quitting

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = detector.detectMultiScale(gray, 1.2, 5)

        recognized_face = False

        for (x, y, w, h) in faces:
            face_img = gray[y:y+h, x:x+w]
            id_, conf = recognizer.predict(face_img)

            if conf < 70:
                name = student_info.get(id_, "Unknown")
                label = f"{name} - {id_}"
                attendance[id_] = {
                    "name": name,
                    "time": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                }
                recognized_face = True
                break  # stop once we recognize one person
            else:
                label = "Unknown"

            cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)
            cv2.putText(frame, label, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255,255,255), 2)

        cv2.imshow("Recognize", frame)

        # Exit if known face recognized
        if recognized_face:
            print(f"Recognized {name}, attendance marked.")
            break

        # Exit if only unknowns seen for too long
        if time.time() - start_time > timeout:
            print("Only unknown faces detected for 10 seconds. Exiting.")
            break

        # Optional manual quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("Manual quit.")
            break

    cap.release()
    cv2.destroyAllWindows()

    if attendance:
        df = pd.DataFrame([
            {"StudentID": k, "Name": v["name"], "Time": v["time"]}
            for k, v in attendance.items()
        ])
        df.to_csv('attendance.csv', index=False)
        print("Attendance recorded successfully.")
    else:
        print("No attendance to record.")

if __name__ == "__main__":
    recognize()
