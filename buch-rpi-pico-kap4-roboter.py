# Pico - Ansteuerung Roboter
# Datei: buch-rpi-pico-kap4-roboter.py


#Bibliotheken
import machine
import utime

#Variablen
motStby=machine.Pin(9, machine.Pin.OUT)
#Motor A
motAPWM = machine.PWM(machine.Pin(6))
motAPWM.freq(1000)
motAIn1=machine.Pin(7, machine.Pin.OUT)
motAIn2=machine.Pin(8, machine.Pin.OUT)

#Motor B
motBPWM = machine.PWM(machine.Pin(10))
motBPWM.freq(1000)
motBIn1=machine.Pin(11, machine.Pin.OUT)
motBIn2=machine.Pin(12, machine.Pin.OUT)

#Funktionen
def RobVor(speed):
	#Vorwärts
    motAPWM.duty_u16(speed)
    motBPWM.duty_u16(speed)
    motAIn1.value(1)
    motAIn2.value(0)
    motBIn1.value(1)
    motBIn2.value(0)
	
def RobRueck(speed):
    #Rückwärts
    motAPWM.duty_u16(speed)
    motBPWM.duty_u16(speed)
    motAIn1.value(0)
    motAIn2.value(1)
    motBIn1.value(0)
    motBIn2.value(1)

def RobRechts(speed):
    #Rechts
    motAPWM.duty_u16(speed)
    motBPWM.duty_u16(0)
    motAIn1.value(1)
    motAIn2.value(0)
    motBIn1.value(0)
    motBIn2.value(0)

def RobLinks(speed):
    #Links
    motAPWM.duty_u16(0)
    motBPWM.duty_u16(speed)
    motAIn1.value(0)
    motAIn2.value(0)
    motBIn1.value(1)
    motBIn2.value(0)

def RobStop():
    #Stopp
    motStby.value(0)	


#Hauptprogramm
while True:
    motStby.value(1)
    #Vorwärts
    RobVor(20000)    
    utime.sleep(2)
    RobVor(40000)    
    utime.sleep(2)
    #Stopp
    RobStop()
    utime.sleep(2)
    #Rückwärts
    motStby.value(1)
    RobRueck(20000)    
    utime.sleep(2)
    #Stop
    RobStop()
    utime.sleep(2)
    #Rechts
    motStby.value(1)
    RobRechts(20000)    
    utime.sleep(2)
    #Stop
    RobStop()
    utime.sleep(2)
    #Links
    motStby.value(1)
    RobLinks(20000)    
    utime.sleep(2)
    #Stop
    RobStop()
    utime.sleep(2)

    

