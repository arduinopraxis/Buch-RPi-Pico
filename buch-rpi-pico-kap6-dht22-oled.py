# Pico - DHT-Sensor
# Datei: buch-rpi-pico-kap6-dht22-oled.py

#Bibliotheken
from machine import Pin
from dht import DTH
from ssd1306 import SSD1306_I2C
import utime

#Variablen/Objekte
gpio_dht = Pin(2, mode=Pin.OPEN_DRAIN)
# DHT(Pin, Sensortyp: 0=DHT11, 1=DHT22)
d = DTH(gpio_dht, 1)
# I2C
sda=machine.Pin(8)
scl=machine.Pin(9)
i2c = machine.I2C(0, scl=scl, sda=sda, freq=100000)
# OLED
oled = SSD1306_I2C(128, 32, i2c)

#Hauptprogramm
while True:
    sensor = d.read()
    if sensor.is_valid():
        temp=str(sensor.temperature/1.0)
        hum=str(sensor.humidity/1.0)
        oled.text('T:'+temp+' C', 0, 0)
        oled.text('H:'+hum+' %', 0, 10)
        oled.show()
        utime.sleep(2)
        oled.fill(0)
    else:
        oled.text('.....', 0, 0)
        oled.text('', 10, 10)
        oled.show()
        utime.sleep(2)
        
