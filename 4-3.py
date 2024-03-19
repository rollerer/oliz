import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)
pwmm = GPIO.PWM(24, 100)
pwmm.start(0)
try:
    while 0==0:
        dc = int(input())
        pwmm.start(dc)
        print(3.3*dc/100)
finally:
    GPIO.output(24, 0)
    GPIO.cleanup()