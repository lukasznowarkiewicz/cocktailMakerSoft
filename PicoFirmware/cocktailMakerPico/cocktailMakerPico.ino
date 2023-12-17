//#include "Arduino.h"
#define P1 2
#define P2 3
#define P3 4
#define P4 5
#define P5 6
#define P6 7
#define P7 8
#define P8 9
int outPins[] = {P1, P2, P3, P4, P5, P6, P7, P8};

void flashLEDOnce(){
      digitalWrite(LED_BUILTIN, LOW);
      delay(50);
      digitalWrite(LED_BUILTIN, HIGH);
  
}

void flashLEDTwice(){
      digitalWrite(LED_BUILTIN, LOW);
      delay(50);
      digitalWrite(LED_BUILTIN, HIGH);
      delay(50);
      digitalWrite(LED_BUILTIN, LOW);
      delay(50);
      digitalWrite(LED_BUILTIN, HIGH);
      delay(50);
}

void setup() {
  Serial.begin(115200);
  Serial.println("I m alive");
  if (!Serial.available()) {}
  for (int i = 0; i < 8; i++) {
    pinMode(outPins[i], OUTPUT);
    delay(100);
    digitalWrite(outPins[i], HIGH);
  }
  pinMode(LED_BUILTIN, OUTPUT);
  digitalWrite(LED_BUILTIN, HIGH);
  Serial.println("I'm alive 2");
}


void loop() {
  if (Serial.available()) {
    String command = Serial.readStringUntil('\n');
    digitalWrite(LED_BUILTIN, LOW);
    delay(100);
    handleCommand(command);
    digitalWrite(LED_BUILTIN, HIGH);
  }
}

void handleCommand(String command) {
  command.trim();
  String module = command.substring(0, 2);
  String action = command.substring(3);

  int pin;

  if (module == "P1") {
    pin = P1;
    if (action == "ON") {
      digitalWrite(pin, LOW);
      Serial.println("P1: ON - OK");
      flashLEDTwice();
    } else if (action == "OFF") {
      digitalWrite(pin, HIGH);
      Serial.println("P1: OFF - OK");
      flashLEDTwice();
    } else {
      Serial.println("Unknown action: " + action);
    }
  }
}
