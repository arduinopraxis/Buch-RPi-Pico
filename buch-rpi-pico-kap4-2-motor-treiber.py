# Pico - Ansteuerung Motor-Treiber mit 2 Motoren
# Datei: buch-rpi-pico-kap4-2-motor-treiber.py

#Bibliotheken
import machine
import utime

#Variablen
#Motor A
motAPWM = machine.PWM(machine.Pin(6))
motAPWM.freq(1000)
motAIn1=machine.Pin(7, machine.Pin.OUT)
motAIn2=machine.Pin(8, machine.Pin.OUT)
motStby=machine.Pin(9, machine.Pin.OUT)
#Motor B
motBPWM = machine.PWM(machine.Pin(10))
motBPWM.freq(1000)
motBIn1=machine.Pin(11, machine.Pin.OUT)
motBIn2=machine.Pin(12, machine.Pin.OUT)

#Funktionen

#Loop
while True:
    motStby.value(1)
    #Vorwärts A
    motAPWM.duty_u16(40000)
    motAIn1.value(1)
    motAIn2.value(0)
    print("Motor A Vor")
    #Vorwärts B
    motBPWM.duty_u16(40000)
    motBIn1.value(1)
    motBIn2.value(0)
    print("Motor B Vor")
    utime.sleep(2)
    #Rückwärts A
    motAPWM.duty_u16(10000)
    motAIn1.value(0)
    motAIn2.value(1)
    print("Motor A Rück")
    #Rückwärts B
    motBPWM.duty_u16(10000)
    motBIn1.value(0)
    motBIn2.value(1)
    print("Motor B Rück")
    utime.sleep(2)
