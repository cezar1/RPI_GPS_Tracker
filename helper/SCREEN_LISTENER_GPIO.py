import sys
import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BCM)
APP="SCREEN_LISTENER_GPIO"
mode=True
if len( sys.argv ) <> 2:
    print "Usage: "+APP+".py [pin]!"
    sys.exit()

number = int(sys.argv[1])
if number==23 or number==24:
	GPIO.setup(number, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	while True:
    		input_state = GPIO.input(number)
    		if input_state == False:
        		print('Button Pressed')
			mode = not mode
			print('Mode is now ['+str(mode)+']')
			os.system('bash SWITCH_SCREEN.sh '+str(int(mode==True)))		
        		time.sleep(0.2)
else:
	print "Must use 23,24 as argument"
	sys.exit()
