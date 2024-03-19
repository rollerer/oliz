import RPi.GPIO as GPIO
def dbin (a):
    return ([int(bin) for bin in bin(a)[2:].zfill(8)])
GPIO.setmode(GPIO.BCM)

dac = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setup(dac, GPIO.OUT)

try:  
    while 0==0: 
        d = float(input())
        if d == int(d):
            d=int(d)
            GPIO.output(dac, dbin(d))
            print(3.3*(d/255))
        else:
            GPIO.output(dac, dbin(d))
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
