# RPi Pico - LED-Ampel
# Datei: buch-rpi-pico-kap5-led-ampel.py

#Bibliotheken
import machine
import utime

#Variablen/Objekte
potentiometer = machine.ADC(27)

led1=machine.Pin(6, machine.Pin.OUT)
led2=machine.Pin(7, machine.Pin.OUT)
led3=machine.Pin(8, machine.Pin.OUT)
led4=machine.Pin(9, machine.Pin.OUT)


#Loop
while True:
    pot=potentiometer.read_u16()
    if pot > 20000:
        led1.value(1)
        print("LED1 ON")
    else:
        led1.value(0)
        print("LED1 OFF")
        
    if pot > 30000:
        led2.value(1)
        print("LED2 ON")
    else:
        led2.value(0)
        print("LED2 OFF")
        
    if pot > 40000:
        led3.value(1)
        print("LED3 ON")
    else:
        led3.value(0)
        print("LED3 OFF")
        
    if pot > 50000:
        led4.value(1)
        print("LED4 ON")
    else:
        led4.value(0)
        print("LED4 OFF")
        
    utime.sleep(0.5)    
        


