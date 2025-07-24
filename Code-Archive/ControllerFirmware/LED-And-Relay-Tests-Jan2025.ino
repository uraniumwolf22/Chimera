
#define LightRelay 2          //Relay pin definitions
#define InverterRelay 3
#define RegulatorRelay 4
#define ChargingRelay 5

#define TruckVoltageSensor 14       //Voltage sensor pin definitions
#define AuxillaryVoltageSensor 15
#define RegulatorVoltageSensor 16

#include <Wire.h> 
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27,20,4);  // set the LCD address to 0x27 for a 16 chars and 2 line display

bool RelayStatus[] = {false, false, false, false};  //Power status of relays

float rOhm1 = 30000.0;  //Value of R1
float rOhm2 = 7500.0;   //Value of R2
float baseVoltage = 5;  //System base voltage.  Calibrate to system input voltage

float VoltageSamples[20];   //Voltage sample array for calculating average


float ReadVoltage(int source){ 
  long sum;   
  for(int i = 0; i < 20; i++){    //Take 20 samples of the analog pins voltage
    VoltageSamples[i] = ((analogRead(source) * baseVoltage) / 1024.0) * (rOhm1 + rOhm2) / rOhm2;   //calculate true voltage value

    //might need to add delay here?
  }
  for (int i = 0; i < 20; i++){   //average out voltage
    long sum = 0;
    sum += VoltageSamples[i];
    sum = ((float) sum) / 20;
  }
    return sum;  //return the average voltage over 20 samples
}



  int toggleRelay(int relay){   //toggle relay status
    
    switch(relay){

      case LightRelay:{       //change state of relay and update the relay status in memory
        digitalWrite(relay, !RelayStatus[0]);
        RelayStatus[0] = !RelayStatus[0];
        break;
      }

      case InverterRelay:{
        digitalWrite(relay, !RelayStatus[1]);
        RelayStatus[1] = !RelayStatus[1];
        break;
      }

      case RegulatorRelay:{
        digitalWrite(relay, !RelayStatus[2]);
        RelayStatus[2] = !RelayStatus[2];
        break;
      }
    }
    return 0;
  }


int RegulatorVoltage = 12.2;
int TruckVoltage = 28.6;
int AuxillaryVoltage = 25.2;

#define LightRelayPage 1

void Display(int page){
  switch(page){
    case LightRelayPage:{
      d
    }
  }
}


void setup() {
  // put your setup code here, to run once:
pinMode(LightRelay, OUTPUT);
pinMode(InverterRelay, OUTPUT);
pinMode(RegulatorRelay, OUTPUT);

lcd.init();
lcd.backlight();

}

void loop() {
delay(1000);
toggleRelay(RegulatorRelay);
}
