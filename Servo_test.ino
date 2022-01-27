#include <Servo.h>
Servo servo1;
int value = 0;
int angle = 0;

void setup() {
  // put your setup code here, to run once:
  servo1.attach(7);
  //Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
    // scan from 0 to 180 degrees
    servo1.write(3);
    delay(5000);
    servo1.write(43);
    delay(10000);
}
