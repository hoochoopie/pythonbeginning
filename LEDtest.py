import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)  # set board mode to Broadcom
GPIO.setup(3, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)

for i in range(0,30):
    print(i)
    GPIO.output(3, i&0x4)
    GPIO.output(5, i&0x2)
    GPIO.output(7, i&0x1)
    i += 1
    time.sleep(0.5)

GPIO.output(3, 0x0)
GPIO.output(5, 0x0)
GPIO.output(7, 0x0)
GPIO.cleanup()
