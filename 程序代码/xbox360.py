#!/usr/bin/python
# -*- coding:utf-8 -*-
# 作者：曹沛文
########################################
## 运行于树莓派，需要第三方库的支持   ##
## sudo apt install joystick xboxdrv  ##
## sudo easy_install evdev            ##
## sudo easy_install select           ##
########################################

from evdev import InputDevice
from select import select
# 小车电机驱动自建库
import motor

car = motor.car()
dev = InputDevice('/dev/input/event0')
lock = 1

while True:
    r,w,x = select([dev], [], [])
    for event in dev.read():
        incode = event.code
        inval  = event.value
        print('==============')
        #print(event)
        # tpye int3
        if incode==0:
            print('LT')
        elif incode==1:
            print('LG')
        elif incode==2:
            print('L2')
        elif incode==3:
            print('RT')
        elif incode==4:
            print('RG')
        elif incode==5:
            print('R2')
        # type int1u
        elif incode==16:
            if inval==1:
                print('Right')
                car.RIGHT()
            elif inval==-1:
                print('Left')
                car.LEFT()
        elif incode==17:
            if inval==-1:
                print('Up')
                car.UP()
            elif inval==1:
                print('Down')
                car.DOWN()
        elif incode==304:
            print('A')
        elif incode==305:
            print('B')
        elif incode==307:
            print('X')
        elif incode==308:
            print('Y')
        elif incode==314:
            print('SELET')
            car.STOP()
        elif incode==315:
            print('START')
            if lock==1:
                car.GPIO_INIT()
                lock=0
        elif incode==316:
            print('HOME')
        elif incode==310:
            print('L1')
            car.NI()
        elif incode==311:
            print('R1')
            car.SHUN()
        elif incode==317:
            print('L0')
        elif incode==318:
            print('R0')
        else:
            print('UnknowKey')
            print(incode)
        print(inval)
        if inval==0:
            pass
            car.STOP()
        break
