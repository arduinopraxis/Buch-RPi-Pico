# Pico - OLED-Display
# Datei: buch-rpi-pico-kap6-oled.py

#Bibliotheken
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import utime

#Variablen/Objekte
sda=machine.Pin(8)
scl=machine.Pin(9)
i2c = machine.I2C(0, scl=scl, sda=sda, freq=100000)
oled = SSD1306_I2C(128, 32, i2c)

#Hauptprogramm
while True:
    oled.text('Hello', 0, 0)
    oled.text('RPi Pico', 10, 12)
    oled.show()
    utime.sleep(1)