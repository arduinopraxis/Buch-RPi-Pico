# Pico - State Machine Blink wenn Analog-Level
# Datei: buch-rpi-pico-kap8-sm-blink-analog.py

from rp2 import PIO, StateMachine, asm_pio
from machine import Pin
import utime

# Variablen/Objekte
potentiometer = machine.ADC(28)

# State Machine
@asm_pio(set_init=PIO.OUT_LOW)
def blink():
    wrap_target()
    set(pins, 1)   [31]
    nop()          [31]
    nop()          [31]
    set(pins, 0)   [31]
    nop()          [31]
    nop()          [31]
    wrap()
    
@asm_pio(set_init=PIO.OUT_LOW)
def blink2():
    wrap_target()
    set(pins, 1)   [31]
    nop()          [31]
    nop()          [31]
    nop()          [31]
    nop()          [31]
    nop()          [31]
    nop()          [31]
    nop()          [31]
    nop()          [31]
    set(pins, 0)   [31]
    nop()          [31]
    nop()          [31]
    nop()          [31]
    nop()          [31]
    nop()          [31]
    nop()          [31]
    nop()          [31]
    nop()          [31]
    wrap()
    

sm1 = StateMachine(1, blink, freq=1000, set_base=Pin(15))
sm2 = StateMachine(2, blink2, freq=1000, set_base=Pin(14))


#Loop
while True:
    pot=potentiometer.read_u16()
    if pot > 40000:
        sm1.active(1)  
    else:
        sm1.active(0)
    if pot > 10000:
        sm2.active(1)  
    else:
        sm2.active(0)
    utime.sleep(0.2)
        
    
    
    

