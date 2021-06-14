# Pico - Ansteuerung Motor-Treiber
# Datei: buch-rpi-pico-kap4-motor-treiber.py

#Bibliotheken
import machine
import utime

#Variablen
motPWM = machine.PWM(machine.Pin(6))
motPWM.freq(1000)
motIn2=machine.Pin(7, machine.Pin.OUT)
motIn1=machine.Pin(8, machine.Pin.OUT)
motStby=machine.Pin(9, machine.Pin.OUT)

#Funktionen

#Hauptprogramm
while True:
    motStby.value(1)
    #Vorwärts
    motPWM.duty_u16(40000)
    motIn1.value(1)
    motIn2.value(0)
    print("Motor Vorwärts")
    utime.sleep(2)
    #Rückwärts
    motPWM.duty_u16(10000)
    motIn1.value(0)
    motIn2.value(1)
    print("Motor Rückwärts")
    utime.sleep(2)