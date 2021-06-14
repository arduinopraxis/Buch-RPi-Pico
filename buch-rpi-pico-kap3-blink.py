# Pico - Blink
# Datei: buch-rpi-pico-kap3-blink.py

#Bibliotheken
import machine
import utime

#Variablen
led=machine.Pin(25, machine.Pin.OUT)

#Funktionen

#Loop
while True:
    led.value(1)
    utime.sleep(1)
    led.value(0)
    utime.sleep(1)
