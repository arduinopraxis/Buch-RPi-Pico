# Pico - State Machine Blink
# Datei: buch-rpi-pico-kap8-sm-blink.py

from rp2 import PIO, StateMachine, asm_pio
from machine import Pin
import utime


#Blink
@rp2.asm_pio(set_init=rp2.PIO.OUT_LOW)
def blink():
    wrap_target()
    set(pins, 1)   [31]
    nop()          [31]
    nop()          [31]
    nop()          [31]
    nop()          [31]
    set(pins, 0)   [31]
    nop()          [31]
    nop()          [31]
    nop()          [31]
    nop()          [31]
    wrap()

# State Machine
sm = rp2.StateMachine(0, blink, freq=1000, set_base=Pin(25))

#Programm
sm.active(1)
utime.sleep(3)
sm.active(0)
    
    
