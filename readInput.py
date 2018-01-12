#!/usr/bin/python

import RPi.GPIO as GPIO

print("Starting!")
GPIO.setmode(GPIO.BOARD)
GPIO.setup(24, GPIO.IN)

while(True):
	inn = GPIO.input(24)
	print(inn)
	if(inn == 1):
		break
print("The end.")
