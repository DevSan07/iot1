import time
import picamera

camera = picamera.PiCamera()
try:
camera.start_preview()
time.sleep(5)
camera.capture('/home/pi/Desktop/test.png')
camera.stop_preview()

finally:
    
camera.close()
