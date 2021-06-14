# RPi Pico - Umrechung Celsius/Fahrenheit-Fahrenheit/Celsius
# Datei: buch-rpi-pico-kap3-tempumrechnung.py

import machine
import utime


    
def ConvFtoC(tempF):
    tempC=((tempF-32)/1.8)
    return tempC

def ConvCtoF(tempC):
    tempF=(tempC*1.8)+32
    return tempF
    


while True:
    celsius=ConvFtoC(98)
    print("Celsius:")
    print(celsius)
    utime.sleep(1)
    fahrenheit=ConvCtoF(celsius)
    print("Fahrenheit:")
    print(fahrenheit)
    utime.sleep(1)
    
    

