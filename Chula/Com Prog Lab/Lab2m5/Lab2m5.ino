#include <M5Stack.h>

int ledPin = 22;
int ledState = LOW;

void setup() {
  M5.begin();
  pinMode(ledPin, OUTPUT);
  digitalWrite(ledPin, ledState);
  M5.update();
}

void loop() {
  // put your main code here, to run repeatedly:
  if (M5.BtnC.wasPressed()) {
    ledState = !ledState;
    digitalWrite(ledPin, ledState);
    }
  M5.update();
}
