# Pico - Messung interne Spannung des Temperatur-Sensors
# Datei: buch-rpi-pico-kap5-tempsensor-intern.py


import machine
import utime

#Variablen/Objekte
sensor_temp = machine.ADC(4)
conversion_factor = 3.3 / (65535)

#Loop
while True:
    reading = sensor_temp.read_u16() * conversion_factor
    
    temperature = 27 - (reading - 0.706)/0.001721
    print(temperature)
    utime.sleep(2)