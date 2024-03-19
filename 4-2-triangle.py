import RPi.GPIO as GPIO
import time
def dbin (a):
    return ([int(bin) for bin in bin(a)[2:].zfill(8)])
GPIO.setmode(GPIO.BCM)

dac = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setup(dac, GPIO.OUT)

try:  
    t = float(input())/256/2
    while 0==0: 
        for d in range(0, 256):
            GPIO.output(dac, dbin(d))
            time.sleep(t)
        for d in range(255, -1, -1):
            GPIO.output(dac, dbin(d))
            time.sleep(t)
except :
    if d<0:
        print("Отрицательное значение")
    elif d != int(d) :
        print("Не целое число")
    elif d >255:
        print("Выходит за рамки расчёта")
    elif ValueError:
        print("Введите число")


finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()