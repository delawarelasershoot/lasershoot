#!/usr/bin/python

import RPi.GPIO as GPIO
import time

print("Starting!")
channel = 18
power = 32

GPIO.setmode(GPIO.BOARD)

GPIO.setup(power, GPIO.OUT)
GPIO.setup(channel, GPIO.IN)

GPIO.output(power, 1)
while(True):
	inn = GPIO.input(channel)
	if(inn != 0):
		print(time.time())
		time.sleep(0.5)
	
print("The end.")
