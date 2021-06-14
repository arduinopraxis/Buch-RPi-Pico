# Raspberry Pi Pico - I2C LCD
# Datei: buch-rpi-pico-kap6-i2c-lcd.py

# Bibliothek
from machine import I2C, Pin
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd
import utime

# Variablen/Objekte
I2C_ADDR     = 0x3F
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16

sda=machine.Pin(8)
scl=machine.Pin(9)   
i2c = I2C(0, sda=sda, scl=scl, freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)    

# Hauptprogramm
while True:
    lcd.clear()
    lcd.backlight_on()
    lcd.move_to(1,0)
    lcd.putstr("1: Raspberry Pi")
    lcd.move_to(2,1)
    lcd.putstr("2: Pico")
    utime.sleep(2)