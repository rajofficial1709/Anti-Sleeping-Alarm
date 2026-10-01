# 👁️ Anti-Sleeping Alarm System

An AI-based Anti-Sleeping Alarm System designed to detect signs of drowsiness using a camera and trigger an alarm when the user's eyes remain closed for a certain period of time.

The system uses **Python, OpenCV, Haar Cascade Classifiers, and Arduino** to monitor the user's eyes and activate an external buzzer/LED when drowsiness is detected.

---

## 📌 Project Overview

Driver drowsiness is one of the major causes of road accidents. This project provides a simple real-time solution for detecting eye closure and generating an alert.

The camera continuously captures video frames. OpenCV detects the user's face and eyes using Haar Cascade classifiers. If the eyes remain closed for a predefined period, Python sends an `"ALARM"` command to the Arduino through serial communication.

Arduino receives the command and activates the connected buzzer or LED.

---

## 🚀 Features

- Real-time face detection
- Real-time eye detection
- Drowsiness detection based on eye closure
- Automatic alarm generation
- Python-Arduino serial communication
- Camera-based monitoring
- External buzzer/LED control
- Simple and low-cost implementation

---

## 🛠️ Technologies Used

### Software

- Python
- OpenCV
- Haar Cascade Classifier
- PySerial

### Hardware

- Arduino
- Webcam / Camera
- Buzzer or LED
- Jumper wires
- Breadboard

---

## 📂 Project Structure

```text
Anti-Sleeping-Alarm/
│
├── firsteye.py
├── main.cpp
├── README.md

#How It Works
        Camera
           ↓
    Capture Video Frame
           ↓
      Face Detection
           ↓
       Eye Detection
           ↓
   Are Eyes Closed?
       ↙       ↘
     YES        NO
      ↓          ↓
  Drowsiness   Continue
   Detected
      ↓
 Send "ALARM"
      ↓
    Arduino
      ↓
 Buzzer / LED ON
