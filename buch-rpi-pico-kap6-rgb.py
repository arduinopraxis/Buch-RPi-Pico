# RPi Pico - RGB LED
# Datei: buch-rpi-pico-kap6-rgb.py

#Bibliotheken
from machine import Pin, PWM
import utime

#Variablen/Objekte
pwm_rot = machine.PWM(machine.Pin(6))
pwm_rot.freq(1000)
pwm_gruen = machine.PWM(machine.Pin(7))
pwm_gruen.freq(1000)
pwm_blau = machine.PWM(machine.Pin(8))
pwm_blau.freq(1000)

# Funktionen
def rgb(red, green, blue):
    red=red*64
    green=green*64
    blue=blue*64    
    pwm_rot.duty_u16(red)
    pwm_gruen.duty_u16(green)
    pwm_blau.duty_u16(blue)


#Loop
while True:
    #rot
    rgb(0, 1023, 1023)
    utime.sleep(1)
    #gelb
    rgb(0, 0, 1023)
    utime.sleep(1)
    #blau
    rgb(1023, 1023, 0)
    utime.sleep(1)
    
    



        



