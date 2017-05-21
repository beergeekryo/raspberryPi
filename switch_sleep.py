import RPi.GPIO as GPIO
import time 

GPIOSW1 = 11
GPIO.setmode(GPIO.BOARD)
GPIO.setup(GPIOSW1,GPIO.IN)

try: 
    while True:
        if GPIO.input(GPIOSW1) == GPIO.HIGH:
            print "SW1 ON"
        else:
           print "SW1 OFF"
        time.sleep(1)

except KeyboardInterrupt:
    pass 

GPIO.cleanup()


