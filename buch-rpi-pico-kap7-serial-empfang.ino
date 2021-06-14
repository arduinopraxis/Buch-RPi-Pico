// RPi Pico - Daten empfangen
// Datei: buch-rpi-pico-kap7-serial-empfang.ino

#include <SoftwareSerial.h>

// UART RX, TX
SoftwareSerial PicoSerial(2, 3);

String Datastring;
char serChar;

void setup() 
{
  Serial.begin(9600);
  Serial.println("Daten empfangen...");
  Serial.println("------------------");

  PicoSerial.begin(9600);

}

void loop() 
{
  if (PicoSerial.available() > 0) 
  {
    serChar=PicoSerial.read();
    Datastring.concat(serChar);
    if(serChar == '\n')
    {
      Serial.print(Datastring);
    }
    
  }

}
