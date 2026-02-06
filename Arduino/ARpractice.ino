const int buttonPin = 2;

void setup() {
  pinMode(7, OUTPUT);
  pinMode(buttonPin, INPUT_PULLUP);
}

void loop() {
 int buttonState = digitalRead(buttonPin);

if (buttonState == LOW) {   
    digitalWrite(7, HIGH);
    delay(500);
    digitalWrite(7, LOW);
    delay(500);
  } else {
    digitalWrite(7, LOW); 
  }
}


