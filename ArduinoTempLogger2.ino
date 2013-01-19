/* Modified temperature sensor sketch. Original written by ladyada.
   This sketch is designed to read serial data sent by python script 
   and send the humidity and temperature from a DHT11
 */

#include "DHT.h"
#define DHTPIN 2     // what pin we're connected to
#define DHTTYPE DHT11   // DHT 11 

int val = 0;

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600); 
  dht.begin();
}

void loop() {
  // Reading temperature or humidity takes about 250 milliseconds!
  // Sensor readings may also be up to 2 seconds 'old' (its a very slow sensor)
  float h = dht.readHumidity();
  float t = dht.readTemperature();

if (Serial.available()) {
 val = Serial.read();
  if (val > '3' && val <='4') { //only if a 4 is received

    if (isnan(t) || isnan(h)) {
      Serial.println("Failed to read from DHT");
  }   else  {  
      Serial.print("Kitchen ");
      Serial.print("Humidity: "); 
      Serial.print(h);
      Serial.print(" %");
      Serial.print(" \t");
      Serial.print(" Temperature: "); 
      Serial.print((t*9.0/5.0+32));
      Serial.println(" *C");

  }
    }
}
}


