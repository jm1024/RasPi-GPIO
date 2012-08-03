from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.OUT)
while 1:
	GPIO.output(25, False)
	sleep(1)
	GPIO.output(25,True)
	sleep(1)
