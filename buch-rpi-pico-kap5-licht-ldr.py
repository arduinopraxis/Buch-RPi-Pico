# Pico - Lichtmesser mit LDR
# Datei: buch-rpi-pico-kap5-licht-ldr.py

#Bibliotheken
import machine
import utime

# Variablen/Objekte
licht = machine.ADC(27)

while True:
    lichtmesser=licht.read_u16()
    print(lichtmesser)
    utime.sleep(2)