Face Recognition Based Student Attendance System 🧠
This is a modular Python-based attendance system using facial recognition. It captures attendance from a webcam or 5G IP camera, records it in a CSV file, and can automatically email the report.
📦 Features

🎦 Real-time face recognition using OpenCV
🧠 Face training using LBPH algorithm
📸 Face dataset collection per student
📝 Automatic attendance CSV generation
📧 Email attendance report to specified address
✅ Auto-quits after successful recognition
⏳ Auto exits if no face is recognized in 10 seconds

🔧 Requirements

Python 3.7+
opencv-python
numpy
pandas

Installation

Clone the repository:

git clone https://github.com/yourusername/student-attendance-system.git
cd student-attendance-system


Install required Python packages:

pip install opencv-python opencv-contrib-python numpy pandas

Usage
1. Capture Images for Students
Run the script to capture images of students for training:
python capture_images.py

This will open your webcam and save multiple images of the student's face in the dataset folder. Each student should have a folder named like ID_Name (e.g., 1_John).
2. Train the Model
Train the face recognizer model on the captured images:
python train.py

The trained model will be saved in the trainer/ folder.
3. Recognize Faces and Mark Attendance
Run the face recognition script:
python recognize.py

The webcam will open and automatically recognize faces. When a face is recognized, attendance is marked and saved in attendance.csv. The program will exit automatically after recognizing a face or you can press q to quit manually.
4. (Optional) Send Attendance Email
You can send the attendance CSV via email using:
python send_email.py

Configure your Gmail and app password in the script before running.
Notes

Use app passwords for Gmail if you have 2FA enabled. You can generate one from your Google Account security settings.
The face recognizer uses LBPH algorithm from OpenCV’s cv2.face module.
Adjust the recognition confidence threshold (conf < 70 in recognize.py) if needed.

