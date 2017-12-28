#!/usr/bin/python
# -*- coding:utf-8 -*-
import RPi.GPIO as GPIO
import time
import sys

#管脚设置
RA1 = 22
RA2 = 27
RB1 = 24
RB2 = 23
LA1 = 6
LA2 = 5
LB1 = 21
LB2 = 20
PWMRA = 17
PWMRB = 18
PWMLA = 13
PWMLB = 12
#传递参数
DIRE = int(sys.argv[1])
PWM = int(sys.argv[2])
delay = int(sys.argv[3])

def GPIO_INIT():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(RA1,GPIO.OUT)
    GPIO.setup(RA2,GPIO.OUT)
    GPIO.setup(RB1,GPIO.OUT)
    GPIO.setup(RB2,GPIO.OUT)
    GPIO.setup(LA1,GPIO.OUT)
    GPIO.setup(LA2,GPIO.OUT)
    GPIO.setup(LB1,GPIO.OUT)
    GPIO.setup(LB2,GPIO.OUT)
    GPIO.setup(PWMRA,GPIO.OUT)
    GPIO.setup(PWMRB,GPIO.OUT)
    GPIO.setup(PWMLA,GPIO.OUT)
    GPIO.setup(PWMLB,GPIO.OUT)
	return 0

def PWM_INIT(PWM):
    RA = GPIO.PWM(PWMRA,500)
    RA.start(PWM)
    RB = GPIO.PWM(PWMRB,500)
    RB.start(PWM)
    LA = GPIO.PWM(PWMLA,500)
    LA.start(PWM)
    LB = GPIO.PWM(PWMLB,500)
    LB.start(PWM)
	return 0

def PWM_STOP():
    RA.stop()
    RB.stop()
    LA.stop()
    LB.stop()
	return 0

def main():
    #初始化GPIO口
    GPIO_INIT()  
    #设置控制口
    GPIO.output(RA1,GPIO.HIGH)
    GPIO.output(RA2,GPIO.LOW)
    GPIO.output(RB1,GPIO.HIGH)
    GPIO.output(RB2,GPIO.LOW)
    GPIO.output(LA1,GPIO.HIGH)
    GPIO.output(LA2,GPIO.LOW)
    GPIO.output(LB1,GPIO.HIGH)
    GPIO.output(LB2,GPIO.LOW)
    #设置PWM使能端口
    PWM_INIT(PWM)
    time.sleep(delay)
	#关闭使能端
    PWM_STOP()
	GPIO.cleanup()
    return 0



if __name__ == '__name__':
main()

