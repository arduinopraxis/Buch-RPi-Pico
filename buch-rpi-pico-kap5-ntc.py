# Pico - Temperaturmessung mit NTC
# Datei: buch-rpi-pico-kap5-ntc.py

#Bibliotheken
import machine
import utime

# Variablen/Objekte
pinAnalog = machine.ADC(27)
Wid25Grad= 10000
WidOhm= 10000
Temp = 0

# Funktionen
def steinhart_temperatur_C(r, Ro=Wid25Grad, To=25.0, beta=3950.0):
    import math
    steinhart = math.log(r / Ro) / beta      # log(R/Ro) / beta
    steinhart += 1.0 / (To + 273.15)         # log(R/Ro) / beta + 1/To
    steinhart = (1.0 / steinhart) - 273.15   # Invert, convert to C
    return steinhart

 

# Hauptprogramm
while True:
    thermistor = pinAnalog.read_u16()
    R = WidOhm / (65535/thermistor -1 )
    Temp=steinhart_temperatur_C(R)
    print(Temp)
    utime.sleep(2)
