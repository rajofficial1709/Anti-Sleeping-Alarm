import cv2
import time
import serial

# Initialize Arduino Communication
arduino = serial.Serial('COM7', 9600, timeout=1)  # Replace COM7 with your Arduino port
time.sleep(2)  # Allow Arduino to initialize

# Load Haar cascades for face and eye detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")

# OpenCV Camera Initialization
cap = cv2.VideoCapture(0)  # Replace 0 with your camera index if needed
if not cap.isOpened():
    print("Error: Camera not accessible!")  
    arduino.close() 
    exit()

# Variables for eye state detection
eye_closed_start = None
alarm_triggered = False

print("Starting eye detection... Press 'q' to exit.")

# Infinite loop for detection
while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Cannot read frame from camera.")
        break

    # Convert the frame to grayscale for detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
    eyes_detected = False

    for (x, y, w, h) in faces:
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]

        # Detect eyes within the face ROI
        eyes = eye_cascade.detectMultiScale(roi_gray)

        for (ex, ey, ew, eh) in eyes:
            # Draw a red rectangle around detected eyes
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 0, 255), 2)
            eyes_detected = True

    # Logic for eye closure and alarm
    if not eyes_detected:  # If eyes are not detected
        if eye_closed_start is None:
            eye_closed_start = time.time()  # Start the closed-eye timer
        elif time.time() - eye_closed_start > 5:  # If closed for more than 3 seconds
            if not alarm_triggered:
                print("Eyes closed for more than 5 seconds. Triggering alarm...")
                arduino.write(b'ALARM\n')  # Send alarm signal to Arduino
                alarm_triggered = True
    else:  # Eyes are open
        eye_closed_start = None  # Reset the timer
        if alarm_triggered:
            print("Eyes opened. Resetting alarm.")
            arduino.write(b'RESET\n')  # Send reset signal to Arduino
            alarm_triggered = False

    # Display the video feed
    cv2.imshow("Eye Detection", frame)

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()
arduino.close()
