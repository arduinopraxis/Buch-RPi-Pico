# Pico - LED mit PWM
# Datei: buch-rpi-pico-kap4-led-pwm.py

import machine
import utime

# Variablen
potentiometer = machine.ADC(28)

#PWM
pwm = machine.PWM(machine.Pin(15))
pwm.freq(1000)


while True:
    pwm.duty_u16(potentiometer.read_u16())