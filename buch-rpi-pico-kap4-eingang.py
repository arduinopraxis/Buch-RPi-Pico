# RPi Pico - Eingang einlesen
# Datei: buch-rpi-pico-kap4-eingang.py

#Bibliotheken
import machine
import utime

#Variablen
taster=machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_DOWN)
led=machine.Pin(25, machine.Pin.OUT)

#Funktionen

#Loop
while True:
    if taster.value() == 1:
        led.value(1)
        utime.sleep(0.1)
    led.value(0) 