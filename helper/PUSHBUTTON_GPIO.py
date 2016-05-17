import sys
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
if len( sys.argv ) <> 2:
    print "Usage: PUSHBUTTON_GPIO.py [pin]!"
    sys.exit()

number = int(sys.argv[1])
if number==23 or number==24:
	GPIO.setup(number, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	while True:
    		input_state = GPIO.input(number)
    		if input_state == False:
        		print('Button Pressed')
        		time.sleep(0.2)
else:
	print "Must use 23,24 as argument"
	sys.exit()
