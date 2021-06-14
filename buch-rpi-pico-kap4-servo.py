# Pico - Servo gesteuert über Analog
# Datei: buch-rpi-pico-kap4-servo.py

import machine
import utime
from servo import Servo

# Variablen
potentiometer = machine.ADC(28)
servo1 = Servo(15)

while True:
    pwm=potentiometer.read_u16()
    pos=int(pwm/64)
    servo1.goto(pos)