# RPi Pico - I2C Scanner
# Datei: buch-rpi-pico-kap7-i2c-scan.py

import uos
import machine

print(uos.uname())
print("Freq: "  + str(machine.freq()) + " Hz")

i2c = machine.I2C(0)
print(i2c)

print("Available i2c devices: "+ str(i2c.scan()))