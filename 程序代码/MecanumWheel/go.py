#!/usr/bin/python
# -*- coding:utf-8 -*-
import RPi.GPIO as GPIO
import time
import sys

RA1 = 17
RA2 = 27
RB1 = 23
RB2 = 24
LA1 = 6
LA2 = 13
LB1 = 12
LB2 = 20
PWMRA = 22
PWMRB = 18
PWMLA = 5
PWMLB = 21
PWM = int(sys.argv[1])
delay = int(sys.argv[2])

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

RA = GPIO.PWM(PWMRA,200)
RA.start(PWM)
RB = GPIO.PWM(PWMRB,200)
RB.start(PWM)
LA = GPIO.PWM(PWMLA,200)
LA.start(PWM)
LB = GPIO.PWM(PWMLB,200)
LB.start(PWM)

GPIO.output(RA1,GPIO.HIGH)
GPIO.output(RA2,GPIO.LOW)
GPIO.output(RB1,GPIO.HIGH)
GPIO.output(RB2,GPIO.LOW)
GPIO.output(LA1,GPIO.HIGH)
GPIO.output(LA2,GPIO.LOW)
GPIO.output(LB1,GPIO.HIGH)
GPIO.output(LB2,GPIO.LOW)
time.sleep(delay)
