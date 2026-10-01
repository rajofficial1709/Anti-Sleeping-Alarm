#include <Arduino.h>

#define ALARM_PIN 8  // Pin connected to a buzzer or LED

void setup() {
    Serial.begin(9600);  // Initialize serial communication
    pinMode(ALARM_PIN, OUTPUT);
    digitalWrite(ALARM_PIN, LOW);  // Ensure alarm is off initially
}

void loop() {
    if (Serial.available() > 0) {
        String data = Serial.readStringUntil('\n');  // Read data from Python
        if (data == "ALARM") {
            digitalWrite(ALARM_PIN, HIGH);  // Turn on alarm
        } else if (data == "RESET") {
            digitalWrite(ALARM_PIN, LOW);   // Turn off alarm
        }
    }
}
