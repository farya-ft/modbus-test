#include <Arduino.h>
#include <ArduinoRS485.h> // ArduinoModbus depends on the ArduinoRS485 library
#include <ArduinoModbus.h>
#include <HardwareSerial.h>

// Define the serial port (Serial, Serial1, Serial2, etc.) based on your Arduino board
HardwareSerial mySerial(D2, D8);  // For Arduino boards with multiple hardware serial ports, like Arduino Mega or Arduino Due

const int ledPin = LED_BUILTIN;


void setup() {
  Serial.begin(9600);
  mySerial.begin(115200);

  Serial.println("Modbus RTU Server LED");
  mySerial.println("Modbus RTU Server LED");

  // start the Modbus RTU server, with (slave) id 1
  if (!ModbusRTUServer.begin(1, 9600)) {
    Serial.println("Failed to start Modbus RTU Server!");
    while (1);
  }

  // configure the LED
  pinMode(ledPin, OUTPUT);
  digitalWrite(ledPin, LOW);

   // configure the LED
  pinMode(D5, OUTPUT);
  digitalWrite(D5, LOW);


  // configure a single coil at address 0x00
  ModbusRTUServer.configureCoils(0x00, 2);
}

void loop() {
  // poll for Modbus RTU requests
  int packetReceived = ModbusRTUServer.poll();

  if(packetReceived) {
    // read the current value of the coil
    int coilValue = ModbusRTUServer.coilRead(0x00);
    int coilValue1 = ModbusRTUServer.coilRead(0x01);
    if (coilValue) {
      // coil value set, turn LED on
      digitalWrite(ledPin, HIGH);
    } else {
      // coil value clear, turn LED off
      digitalWrite(ledPin, LOW);
    }

    if (coilValue1) {
      // coil value set, turn LED on
      digitalWrite(D5, HIGH);
    } else {
      // coil value clear, turn LED off
      digitalWrite(D5, LOW);
    }
  }
}