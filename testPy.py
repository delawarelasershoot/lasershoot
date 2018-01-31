import time
import csv
import RPi.GPIO as GPIO

power = 7
buzzer = 23
ir = 21

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(power,GPIO.OUT)
GPIO.output(power,GPIO.HIGH)

GPIO.setup(buzzer,GPIO.OUT)
GPIO.output(buzzer,GPIO.HIGH)

GPIO.setup(ir,GPIO.IN)



f = open('test.csv', 'w')
<<<<<<< HEAD:testPy.py
f.write('\n')
while(True):
    print(GPIO.input(ir))
    if GPIO.input(ir) == 1:
        print(GPIO.input(ir))
        f.write(str(time.time()) + '\t' + str(GPIO.input(ir)) +'\r')
        #time.sleep(1)
    else:
        print(GPIO.input(ir))
=======

prevTimeStamp = str(time.time())

while(True):
	if(prevTimeStamp != str(time.time())):
		f.write(str(time.time()) + '\t' + str(GPIO.input(ir)) +'\r\n')
		prevTimeStamp = str(time.time())
		
>>>>>>> 0daddc7f23df15dbef146ccd49595905b9d57823:testPi.python
	

