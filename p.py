
import RPi.GPIO as GPIO
from time import sleep
from time import time
import matplotlib.pyplot as plt
GPIO.setmode(GPIO.BCM)

dac = [8, 11, 7, 1, 0, 5, 12, 6]
leds = [2, 3, 4, 17, 27, 22, 10, 9]
comp = 14
troyka = 13

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = 1)
GPIO.setup(comp, GPIO.IN)

def desimal2binary(value):
    return[int(elem) for elem in bin(value)[2:].zfill(8)]
GPIO.output(troyka, 1)
def adc():
    value = 0
    v=[0]*8
    for i in range(7, -1, -1):
        value += 2**i
        dacc = desimal2binary(value)
        GPIO.output(dac, dacc)
        sleep(0.005)
        compvalue = GPIO.input(comp)
        if compvalue == 1:
            value -= 2**i
        else:
            v[i]=1
    return value
a=[]
try:
    c=[]
    s=0
    i=0
    key=0
    start_time = time()
    while True:
        aaa = adc()
        a.append(aaa)
        print(round(aaa*3.3/256, 3))
        GPIO.output(leds, desimal2binary(128))
        c.append(time()-start_time)
        i+=1
        if aaa >= 256*0.95:
            key+=1
            if key == 12:
                GPIO.output(troyka, 0)
                s=1
        if aaa <= 256*0.094 and s==1:
            end_time = time()
            break
finally:
    GPIO.cleanup()
    with open('data.txt', 'w') as d:
        d.write("\n".join([str(i*3.3/256) for i in a]))
    ttime = end_time-start_time
    print('время замера: ' + str(round(ttime, 3)))
    print('период: ' + str(round(ttime/len(a), 3)))
    print('частота: '+str(round(len(a)/ttime,3)))
    print('шаг квантования: ' + str(round(3.3/256,3)))
    plt.xlim([0, 11])
    plt.ylim([0,3.3])
    plt.plot(c, [float(i*3.3/256) for i in a])
    plt.show()