import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(3,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(8,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)

While True:
    
    print("LED ON")
    
GPIO.output(3,GPIO.HIGH)
GPIO.output(12,GPIO.HIGH)
Time.sleep(0.4)

GPIO.output(3,GPIO.LOW)
GPIO.output(12,GPIO.LOW)
time.sleep(0.4)

GPIO.output(8,GPIO.HIGH)
GPIO.output(16,GPIO.HIGH)
Time.sleep(0.4)

GPIO.output(8,GPIO.LOW)
GPIO.output(16,GPIO.LOW)
Time.sleep(0.4)

GPIO.output(3,GPIO.HIGH)
GPIO.output(16,GPIO.HIGH)
Time.sleep(0.4)

GPIO.output(3,GPIO.LOW)
GPIO.output(16,GPIO.LOW)
time.sleep(0.4)


