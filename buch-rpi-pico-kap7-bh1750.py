# Pico - I2C mit BH1750
# Datei: buch-rpi-pico-kap7-bh1750.py

# Bibliothek
from machine import Pin, I2C
from bh1750 import BH1750
import utime

# I2C
sda=machine.Pin(8)
scl=machine.Pin(9)
i2c = I2C(0, scl=scl, sda=sda, freq=100000)

#Sensor
s = BH1750(i2c)

# Hauptprogramm
while True:
    lux=s.luminance(BH1750.ONCE_HIRES_1)
    luxInt=int(lux)
    print(luxInt)
    utime.sleep(2)