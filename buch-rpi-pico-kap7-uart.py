# Raspberry Pi Pico - UART
# Datei: buch-rpi-pico-kap7-uart.py

# Bibliothek
from machine import UART
import utime

# Variablen/Objekte
uart0 = UART(0,9600)
#uart0 = machine.UART(id=0,baudrate=9600,bits=8,parity=None,stop=1)
 

# Hauptprogramm
while True:
    uart0.write('Daten von Pico\n')
    utime.sleep(10)