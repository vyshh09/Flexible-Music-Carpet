const int analogPin0 = A0; // Pin where voltage is connected
const int analogPin1 = A1; // Pin where voltage is connected
const int analogPin2 = A2; // Pin where voltage is connected
const float V_REF = 5.0;  // Reference voltage (typically 5V)

void setup() {
  Serial.begin(9600); // Start the serial communication
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  int analogValue0 = analogRead(analogPin0); // Read the analog input from A0
  int analogValue1 = analogRead(analogPin1); // Read the analog input from A1
  int analogValue2 = analogRead(analogPin2); // Read the analog input from A2
  
  // Convert the analog readings to voltages
  float voltage0 = (analogValue0 / 1023.0) * V_REF;
  float voltage1 = (analogValue1 / 1023.0) * V_REF;
  float voltage2 = (analogValue2 / 1023.0) * V_REF;

  // if(voltage2 < 4.9){
  //   digitalWrite(LED_BUILTIN, HIGH);
  // Serial.print("hello");
  // Serial.println();}
  // else
  //   digitalWrite(LED_BUILTIN, LOW);    // turn the LED off by making the voltage LOW



  // // Print the analog values and voltages on the same line

  Serial.print(" | V0: ");
  Serial.print(voltage0, 3); // Print voltage with 3 decimal places


  Serial.print(" | V1: ");
  Serial.print(voltage1, 3);


  Serial.print(" | V2: ");
  Serial.print(voltage2, 3);

  Serial.println(); // Move to the next line after printing all values

  // delay(300); // Wait for 300 milliseconds
}
