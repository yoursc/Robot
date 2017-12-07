#!/usr/bin/python
# -*- coding:utf-8 -*-
import RPi.GPIO as GPIO
import time
import sys

# 定义连线端口
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
Frequency = 200
#PWM = int(sys.argv[1])
PWM = 50
#delay = int(sys.argv[2])

class motor(object):
    def GPIO_INIT(self):
        # 初始化PIN口
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
        # 初始化PWM
        self.RA = GPIO.PWM(PWMRA,Frequency)
        self.RA.start('0')
        self.RB = GPIO.PWM(PWMRB,Frequency)
        self.RB.start(0)
        self.LA = GPIO.PWM(PWMLA,Frequency)
        self.LA.start(0)
        self.LB = GPIO.PWM(PWMLB,Frequency)
        self.LB.start(0)
    def WHEEL(wheel,pwm):
        if pwm==0:
            self.motor1=GPIO.LOW
            self.motor2=GPIO.LOW
            self.motorp=0
        elif pwm>=0:
            self.motor1=GPIO.HIGH
            self.motor2=GPIO.LOW
            self.motorp=pwm
        else:
            self.motor1=GPIO.LOW
            self.motor2=GPIO.HIGH
            self.motorp=-pwm
        if wheel=='RA':
            GPIO.output(RA1,self.motor1)
            GPIO.output(RA2,self.motor2)
            self.RA.ChangeDutyCycle(self.motorp)
        elif wheel=='RB':
            GPIO.output(RA1,self.motor1)
            GPIO.output(RA2,self.motor2)
            self.RB.ChangeDutyCycle(self.motorp)
        elif wheel=='LA':
            GPIO.output(RA1,self.motor1)
            GPIO.output(RA2,self.motor2)
            self.LA.ChangeDutyCycle(self.motorp)
        elif wheel=='LB':
            GPIO.output(RA1,self.motor1)
            GPIO.output(RA2,self.motor2)
            self.LB.ChangeDutyCycle(self.motorp)
    def UP(self):
        self.WHEEL('RA',PWM)
        self.WHEEL('RB',PWM)
        self.WHEEL('LA',PWM)
        self.WHEEL('LB',PWM)
        print('up')
    def DOWN(self):
        self.WHEEL('RA',-PWM)
        self.WHEEL('RB',-PWM)
        self.WHEEL('LA',-PWM)
        self.WHEEL('LB',-PWM)
        print('down')
    def LEFT(self):
        self.WHEEL('RA',PWM)
        self.WHEEL('RB',-PWM)
        self.WHEEL('LA',-PWM)
        self.WHEEL('LB',PWM)
        print('left')
    def RIGHT(self):
        self.WHEEL('RA',-PWM)
        self.WHEEL('RB',PWM)
        self.WHEEL('LA',PWM)
        self.WHEEL('LB',-PWM)
        print('right')
    def SHUN(self):
        self.WHEEL('RA',-PWM)
        self.WHEEL('RB',-PWM)
        self.WHEEL('LA',PWM)
        self.WHEEL('LB',PWM)
        print('shun')
    def NI(self):
        self.WHEEL('RA',PWM)
        self.WHEEL('RB',PWM)
        self.WHEEL('LA',-PWM)
        self.WHEEL('LB',-PWM)
        print('ni')
    def STOP(self):
        self.WHEEL('RA',0)
        self.WHEEL('RB',0)
        self.WHEEL('LA',0)
        self.WHEEL('LB',0)
        print('stop')
    def END(self):
        GPIO.cleanup
        print('end')

        


