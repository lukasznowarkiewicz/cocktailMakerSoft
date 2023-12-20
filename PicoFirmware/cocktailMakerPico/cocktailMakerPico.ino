#define LED_PIN 13 // Assuming the onboard LED is connected to pin 13
#define NUM_RELAYS 8
#define COMMAND_LENGTH 5

int outPins[NUM_RELAYS] = {2, 3, 4, 5, 6, 7, 8, 9};

void flashLED(int count, int delayTime) {
  for (int i = 0; i < count; i++) {
    digitalWrite(LED_BUILTIN, LOW);
    delay(delayTime);
    digitalWrite(LED_BUILTIN, HIGH);
    delay(delayTime);
  }
}

void setup() {
  Serial.begin(115200);
  pinMode(LED_BUILTIN, OUTPUT);
  flashLED(2, 50); // Flash onboard LED twice to indicate startup
  for (int i = 0; i < NUM_RELAYS; i++) {
    pinMode(outPins[i], OUTPUT);
    digitalWrite(outPins[i], HIGH);
    delay(100);
  }
}

void loop() {
  if (Serial.available() >= COMMAND_LENGTH) {
    String command = Serial.readStringUntil('\n');
    handleCommand(command);
  }
}

void handleCommand(String command) {
  flashLED(1, 50);
  command.trim();
  String module = command.substring(0, 2);
  String action = command.substring(3);

  for (int i = 0; i < NUM_RELAYS; i++) {
    if (module == "P" + String(i + 1)) {
      int pin = outPins[i];
      if (action == "ON") {
        digitalWrite(pin, LOW);
        Serial.println(module + ": ON - OK");
        flashLED(2, 50);
      } else if (action == "OFF") {
        digitalWrite(pin, HIGH);
        Serial.println(module + ": OFF - OK");
        flashLED(2, 50);
      } else {
        Serial.println("Unknown action: " + action);
      }
      return; // Exit loop after processing the command
    }
  }

  Serial.println("Unknown module: " + module);
}
