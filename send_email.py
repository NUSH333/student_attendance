import smtplib
from email.message import EmailMessage

def send_report():
    sender_email = "anu123@example.com"
    sender_password = "...................."  # Use your app password here
    receiver_email = "xyzz0@example.com"

    subject = "Attendance Report"
    body = "Please find the attached attendance report."

    try:
        with open('attendance.csv', 'rb') as f:  # open in binary mode
            attachment_data = f.read()
    except FileNotFoundError:
        print("attendance.csv not found! Please run recognition first.")
        return

    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg.set_content(body)
    msg.add_attachment(attachment_data, maintype='text', subtype='csv', filename='attendance.csv')

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(sender_email, sender_password)
            smtp.send_message(msg)
        print("Attendance email sent successfully.")
    except Exception as e:
        print("Failed to send email:", e)

if __name__ == "__main__":
    send_report()
