#!/usr/bin/env python2
# -*- coding:utf-8 -*-

#超声波测距程序简易版

import RPi.GPIO as GPIO
import time
Echo = 23
Trig = 24

def checkdist():
    #发出触发信号，并保持10us以上
    GPIO.output(Trig,GPIO.HIGH)
    time.sleep(0.000015)
    GPIO.output(Trig,GPIO.LOW)
    while not GPIO.input(Echo):
        pass
    #发现高电平时开时计时
    t1 = time.time()
    while GPIO.input(Echo):
        pass
    #高电平结束停止计时
    t2 = time.time()
    #返回距离，单位为米
    return (t2-t1)*340/2

GPIO.setmode(GPIO.BCM)
GPIO.setup(Trig,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(Echo,GPIO.IN)

time.sleep(2)

try:
    while True:
        print 'Distance: %0.2f m' %checkdist()
        time.sleep(0.5)
except KeyboardInterrupt:
    GPIO.cleanup()
