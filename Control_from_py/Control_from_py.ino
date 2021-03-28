void setup() {
  Serial.begin(57600);  // start serial for output
  Serial.flush();
  
  pinMode(13, OUTPUT); // Green 1
  pinMode(12, OUTPUT); // Green 2
  pinMode(11, OUTPUT); // Yellow
  pinMode(10, OUTPUT); // Red
}

void loop() {
  int in = Serial.read();
  Serial.print(in);
  Serial.print("\n");
  
  // If 0 is recieved from python show no LEDs
  if (in == 48) {
    digitalWrite(13, LOW);
    digitalWrite(12, LOW);
    digitalWrite(11, LOW);
    digitalWrite(10, LOW);
  }
  // If 1 is recieved from python show 1 LEDs
  if (in == 49) {
    digitalWrite(13, HIGH);
    digitalWrite(12, LOW);
    digitalWrite(11, LOW);
    digitalWrite(10, LOW);
  }
  // If 2 is recieved from python show 2 LEDs
  if (in == 50) {
    digitalWrite(13, HIGH);
    digitalWrite(12, HIGH);
    digitalWrite(11, LOW);
    digitalWrite(10, LOW);
  }
  // If 3 is recieved from python show 3 LEDs
  if (in == 51) {
    digitalWrite(13, HIGH);
    digitalWrite(12, HIGH);
    digitalWrite(11, HIGH);
    digitalWrite(10, LOW);
  }
  // If 4 is recieved from python show 4 LEDs
  if (in == 52) {
    digitalWrite(13, HIGH);
    digitalWrite(12, HIGH);
    digitalWrite(11, HIGH);
    digitalWrite(10, HIGH);
  }
  delay(100);
}
