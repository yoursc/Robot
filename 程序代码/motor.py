#!/usr/bin/python
# -*- coding:utf-8 -*-
import RPi.GPIO as GPIO
import time
import sys

class car(object):
    def __init__(self):
        # 定义连线端口
        self.RA1 = 22
        self.RA2 = 27
        self.RB1 = 24
        self.RB2 = 23
        self.LA1 = 6
        self.LA2 = 5
        self.LB1 = 21
        self.LB2 = 20
        self.PWMRA = 17
        self.PWMRB = 18
        self.PWMLA = 13
        self.PWMLB = 12
        self.Frequency = 200
        self.PWM = 50
    def GPIO_INIT(self):
        # 初始化PIN口
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.RA1,GPIO.OUT)
        GPIO.setup(self.RA2,GPIO.OUT)
        GPIO.setup(self.RB1,GPIO.OUT)
        GPIO.setup(self.RB2,GPIO.OUT)
        GPIO.setup(self.LA1,GPIO.OUT)
        GPIO.setup(self.LA2,GPIO.OUT)
        GPIO.setup(self.LB1,GPIO.OUT)
        GPIO.setup(self.LB2,GPIO.OUT)
        GPIO.setup(self.PWMRA,GPIO.OUT)
        GPIO.setup(self.PWMRB,GPIO.OUT)
        GPIO.setup(self.PWMLA,GPIO.OUT)
        GPIO.setup(self.PWMLB,GPIO.OUT)
        # 初始化PWM
        self.RA = GPIO.PWM(self.PWMRA,self.Frequency)
        self.RA.start(0)
        self.RB = GPIO.PWM(self.PWMRB,self.Frequency)
        self.RB.start(0)
        self.LA = GPIO.PWM(self.PWMLA,self.Frequency)
        self.LA.start(0)
        self.LB = GPIO.PWM(self.PWMLB,self.Frequency)
        self.LB.start(0)
    def WHEEL(self,wheel,pwm):
        # 选择控制口
        if abs(pwm)>=100:
            pwm = int(100*(pwm/abs(pwm)))
        motorp = abs(pwm)
        if wheel=='RA':
            motor1=self.RA1
            motor2=self.RA2
            self.RA.ChangeDutyCycle(motorp)
        elif wheel=='RB':
            motor1=self.RB1
            motor2=self.RB2
            self.RA.ChangeDutyCycle(motorp)
        elif wheel=='LA':
            motor1=self.LA1
            motor2=self.LA2
            self.RA.ChangeDutyCycle(motorp)
        elif wheel=='LB':
            motor1=self.LB1
            motor2=self.LB2
            self.RA.ChangeDutyCycle(motorp)
        # 控制字输出
        if pwm==0:
            GPIO.output(motor1,GPIO.LOW)
            GPIO.output(motor2,GPIO.LOW)
        elif pwm>=0:
            GPIO.output(motor1,GPIO.HIGH)
            GPIO.output(motor2,GPIO.LOW)
        else:
            GPIO.output(motor1,GPIO.LOW)
            GPIO.output(motor2,GPIO.HIGH)
    def UP(self):
        self.WHEEL('RA',self.PWM)
        self.WHEEL('RB',self.PWM)
        self.WHEEL('LA',self.PWM)
        self.WHEEL('LB',self.PWM)
        print('up')
    def DOWN(self):
        self.WHEEL('RA',-self.PWM)
        self.WHEEL('RB',-self.PWM)
        self.WHEEL('LA',-self.PWM)
        self.WHEEL('LB',-self.PWM)
        print('down')
    def RIGHT(self):
        self.WHEEL('RA',-self.PWM)
        self.WHEEL('RB',self.PWM)
        self.WHEEL('LA',self.PWM)
        self.WHEEL('LB',-self.PWM)
        print('right')
    def LEFT(self):
        self.WHEEL('RA',self.PWM)
        self.WHEEL('RB',-self.PWM)
        self.WHEEL('LA',-self.PWM)
        self.WHEEL('LB',self.PWM)
        print('left')
    def SHUN(self):
        self.WHEEL('RA',-self.PWM)
        self.WHEEL('RB',-self.PWM)
        self.WHEEL('LA',self.PWM)
        self.WHEEL('LB',self.PWM)
        print('shun')
    def NI(self):
        self.WHEEL('RA',self.PWM)
        self.WHEEL('RB',self.PWM)
        self.WHEEL('LA',-self.PWM)
        self.WHEEL('LB',-self.PWM)
        print('ni')
    def STOP(self):
        self.WHEEL('RA',0)
        self.WHEEL('RB',0)
        self.WHEEL('LA',0)
        self.WHEEL('LB',0)
        print('stop')
#    def END(self):
#        GPIO.cleanup
#		print('end')
