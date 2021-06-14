# Pico - Ausgang LED
# Datei: buch-rpi-pico-kap4-ausgang-led.py

#Bibliotheken
import machine
import utime

#Variablen
led=machine.Pin(14, machine.Pin.OUT)

#Funktionen

#Loop
while True:
    led.value(1)
    utime.sleep(1)
    led.value(0)
    utime.sleep(1)