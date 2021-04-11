#include <Keypad.h>
int i;
int A_en = 12; // Little/ring finger actuate
int B_en = 10; // Middle finger actuate
int C_en = 9; // First finger actuate
int D_en = 6; // Thumb actuate
int A_ph = 13; // Little/ring finger direction
int B_ph = 11; // Middle finger direction
int C_ph = 8; // First finger direction
int D_ph = 7; // Thumb direction

// Rows and columns for keypad
const byte ROWS = 4;
const byte COLS = 1;

// Define keypad
char hexaKeys[ROWS][COLS] = {
  {'1'},
  {'2'},
  {'3'},
  {'4'}
};
byte rowPins[ROWS] = {A0, A1, A2, A3};
byte colPins[COLS] = {A4};

// Create keypad object
Keypad customKeypad = Keypad(makeKeymap(hexaKeys), rowPins, colPins, ROWS, COLS);


void setup() {
  // Set baud rate
  Serial.begin(9600);
  
  pinMode(A_en, OUTPUT); //Initiates Little/Ring actuator pin
  pinMode(B_en, OUTPUT); //Initiates Middle actuator pin
  pinMode(C_en, OUTPUT); //Initiates First actuator pin
  pinMode(D_en, OUTPUT); //Initiates Thumb actuator pin
  pinMode(A_ph, OUTPUT); //Initiates Little/Ring direction pin
  pinMode(B_ph, OUTPUT); //Initiates Middle direction pin
  pinMode(C_ph, OUTPUT); //Initiates First direction pin
  pinMode(D_ph, OUTPUT); //Initiates Thumb direction pin

  // Initialise actuators in brake mode
  digitalWrite(A_en, LOW);   
  digitalWrite(B_en, LOW);   
  digitalWrite(C_en, LOW);   
  digitalWrite(D_en, LOW);
}


void loop() {
  // Get the input from the keypad
  char customKey = customKeypad.getKey();
  // When button 1 is pressed call the key1 function to close the pinch
  if (customKey == '1') {
    Serial.println("CLOSE!");
    key1(A_ph, B_ph, C_ph, D_ph, A_en, B_en, C_en, D_en, customKey);
  }
  // When button 2 is pressed call the key2 function to open the pinch
  if (customKey == '2') {
    Serial.println("OPEN!");
    key2(A_ph, B_ph, C_ph, D_ph, A_en, B_en, C_en, D_en, customKey);
  }
  // When button 3 is pressed call the key3 function to 
  if (customKey == '3') {
    Serial.println("SHTAP!!");
    key3(A_ph, B_ph, C_ph, D_ph, A_en, B_en, C_en, D_en, customKey);
  }
  // When button 4 is pressed call the key4 function to 
  if (customKey == '4') {
    Serial.println("SHTAP!!");
    //backward @ half speed
    key4(A_ph, B_ph, C_ph, D_ph, A_en, B_en, C_en, D_en, customKey);
  }
}

// Key1 will have the thumb and first finger contract
void key1(int A_ph, int B_ph, int C_ph, int D_ph, int A_en, int B_en, int C_en, int D_en, char customKey) {
  // Set the direction of thumb and first finger
  digitalWrite(C_ph, LOW); 
  digitalWrite(D_ph, LOW);
  // Set the speed of thumb and first finger
  analogWrite(C_en, 150);   
  analogWrite(D_en, 100); 
  return;
}
// Key2 will have the thumb and first finger retract
void key2(int A_ph, int B_ph, int C_ph, int D_ph, int A_en, int B_en, int C_en, int D_en, char customKey) {
  // Set the direction of thumb and first finger
  digitalWrite(C_ph, HIGH); 
  //digitalWrite(D_ph, HIGH);
  // Set the speed of thumb and first finger
  analogWrite(C_en, 150);   
  //analogWrite(D_en, 60); 
  return;
}
// Key3 will be to stop all movement.
void key3(int A_ph, int B_ph, int C_ph, int D_ph, int A_en, int B_en, int C_en, int D_en, char customKey) {
  // Set the motor movement for all fingers to 0
  digitalWrite(A_en, LOW);  
  digitalWrite(B_en, LOW);  
  digitalWrite(C_en, LOW);   
  digitalWrite(D_en, LOW);
  return;
}
// Key4 will close only the first finger
void key4(int A_ph, int B_ph, int C_ph, int D_ph, int A_en, int B_en, int C_en, int D_en, char customKey) {
  // Set the direction of thumb and first finger
  digitalWrite(C_ph, LOW); 
  // Set the speed of thumb and first finger
  analogWrite(C_en, 100);    
  return;
}
