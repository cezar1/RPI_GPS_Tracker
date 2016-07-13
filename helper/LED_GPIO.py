import sys
import RPi.GPIO as GPIO
import time
#print 'Number of arguments:', len(sys.argv), 'arguments.'
#print 'Argument List:', str(sys.argv)
if len( sys.argv ) <> 2:
    print "Usage: LED_GPIO.py [led]!"
    sys.exit()
number = int(sys.argv[1])
#print "Parsed number is ["+str(number)+"]"
if number==18 or number==23 or number==24 or number==22 or number==27:
    print "Conditions accepted, switching LED now"    
else:
    print "Must use 18,23,24,22,27 as argument!"
    sys.exit()
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(number,GPIO.OUT)
print "LED on"
GPIO.output(number,GPIO.HIGH)
time.sleep(0.2)
print "LED off"
GPIO.output(number,GPIO.LOW)
