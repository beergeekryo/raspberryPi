import RPi.GPIO as GPIO
import time 

GPIOSW1 = 11
GPIO.setmode(GPIO.BOARD)
GPIO.setup(GPIOSW1,GPIO.IN)

def sw1_status(channel):
    print "SW1 ON EVENT received"

GPIO.add_event_detect(GPIOSW1, GPIO.RISING, callback=sw1_status, bouncetime=200)

try: 
    while True:
 #      if GPIO.input(GPIOSW1) == GPIO.HIGH:
 #           print "SW1 ON"
 #       else:
 #          print "SW1 OFF"
        time.sleep(1)

except KeyboardInterrupt:
    pass 

GPIO.cleanup()


