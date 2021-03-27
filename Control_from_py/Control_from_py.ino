void setup() {
  Serial.begin(57600);  // start serial for output
  Serial.flush();
  
  pinMode(13, OUTPUT);
  pinMode(12, OUTPUT);
  pinMode(11, OUTPUT);
}

void loop() {
  int in = Serial.read();

  if (in == 49) {
    digitalWrite(13, LOW);
    digitalWrite(12, LOW);
    digitalWrite(11, HIGH);
  }
  if (in == 50) {
    digitalWrite(13, LOW);
    digitalWrite(12, HIGH);
    digitalWrite(11, LOW);
  }
  if (in == 51) {
    digitalWrite(13, HIGH);
    digitalWrite(12, LOW);
    digitalWrite(11, LOW);
  }
  
}
