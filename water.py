
import RPi.GPIO as GPIO
import datetime
import time

switch = 4 
relay = 21 

GPIO.setmode(GPIO.BCM) 
GPIO.setwarnings(False)
GPIO.setup(switch, GPIO.IN)
GPIO.setup(relay, GPIO.OUT)

GPIO.output(relay, GPIO.LOW)

start = datetime.time(10, 24,0) #start watering here
end = datetime.time(10, 24, 5) #water for 5 seconds

while True:
    timestamp = datetime.datetime.now().time()
    # if switch is pressed or it is at watering time, then water
    if (GPIO.input(switch) == 1) or (start <= timestamp <= end):
        GPIO.output(relay, GPIO.HIGH)
    # if switch is not pressed (also used to turn off watering after watering time has elapsed)      
    elif (GPIO.input(switch) == 0):
        GPIO.output(relay, GPIO.LOW)
            
