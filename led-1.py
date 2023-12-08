import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(18,GPIO.OUT)
While(True):
    
    print("LED ON")
    GPIO.output(18,GPIO.HIGH)
    time.sleep(2)
    
    print("LED OFF")
    GPIO.output(18,GPIO.LOW)
    time.sleep(2)
