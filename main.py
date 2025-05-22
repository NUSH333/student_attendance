import time
import capture_images
import train_model
import recognize
import send_email

def main():
    while True:
        print("\nStudent Attendance System Menu")
        print("1. Check Camera")
        print("2. Capture Images")
        print("3. Train Images")
        print("4. Recognize & Mark Attendance")
        print("5. Send Attendance Email")
        print("6. Quit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            check_camera()
        elif choice == '2':
            capture_images.capture()
        elif choice == '3':
            train_model.train()
        elif choice == '4':
            recognize.recognize()
        elif choice == '5':
            send_email.send_report()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice! Try again.")

def check_camera():
    import cv2
    cap = cv2.VideoCapture(0)  # or your camera stream URL here
    if not cap.isOpened():
        print("Cannot open camera")
        return
    print("Press 'q' to exit camera check")
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break
        cv2.imshow('Camera Check', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
