Student Attendance System Using Face Recognition and 5G Camera

This project implements a face recognition–based attendance system using Python and OpenCV, with support for integrating a 5G camera for video streaming.

## Features
1) Capture face images of students
2) Train face recognition model
3) Real-time face recognition and automatic attendance marking
4) Save attendance to CSV
5) Optionally email attendance report

Setup
```Install required libraries:
pip install opencv-python numpy pandas
```
Usage
1. Capture Images
Run the capture script:
```
python capture_images.py
```
2. Train Model
Run the training script:
```
python train_model.py
```
3. Recognize and Mark Attendance
Run the recognition script:
```
python recognize.py
```
This will open your webcam and automatically detect & record attendance once a student is recognized.

4. Send Attendance Email (Optional)
Run the email script (configure your Gmail and app password first):
```
python send_email.py
```

## Using a 5G Camera
This project supports integrating a 5G camera for capturing video streams instead of using the default webcam.

## How to use a 5G Camera stream
Replace the default cv2.VideoCapture(0) with the 5G camera's video stream URL.

Note:
During recognition, press q to quit manually if needed.
Attendance CSV is saved as attendance.csv.
Use Gmail app password for email functionality if 2FA is enabled.
Dataset folder should have subfolders named as <StudentID>_<Name> containing face images.

