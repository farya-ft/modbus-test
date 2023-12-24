#include <Arduino.h>
#include <Sim800L.h>
#include <SoftwareSerial.h>               


// D2: RX from STM32
// D8: TX from STM32
Sim800L GSM(D2, D8);

/*
 * In alternative:
 * Sim800L GSM;                       // Use default pinout
 * Sim800L GSM(RX, TX, RESET);        
 * Sim800L GSM(RX, TX, RESET, LED);
 */


bool error; 					//to catch the response of sendSms


void setup(){
	GSM.begin(115200); 			
	error=GSM.sendSms((char*)"+491795228587",(char*)"hello from arduino");
}

void loop(){
	//do nothing
}