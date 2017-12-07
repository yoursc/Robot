#!/usr/bin/python
# -*- coding:utf-8 -*-

########################################
## 运行于树莓派，需要第三方库的支持   ##
## sudo apt install joystick xboxdrv  ##
## sudo easy_install evdev            ##
## sudo easy_install select           ##
########################################

from evdev import InputDevice
from select import select
import motor

dev = InputDevice('/dev/input/event0')
mctrl = motor.motor()

while True:
    r,w,x = select([dev], [], [])
    for event in dev.read():
#        print(event)
        incode = event.code
        inval  = event.value
        print('==============')
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
                mctrl.RIGHT()
            elif inval==-1:
                print('Left')
                mctrl.LEFT()
        elif incode==17:
            if inval==-1:
                print('Up')
                mctrl.UP()
            elif inval==1:
                print('Down')
                mctrl.DOWN()
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
            mctrl.STOP()
        elif incode==315:
            print('START')
            mctrl.GPIO_INIT()
        elif incode==316:
            print('HOME')
        elif incode==310:
            print('L1')
            mctrl.NI()
        elif incode==311:
            print('R1')
            mctrl.SHUN()
        elif incode==317:
            print('L0')
        elif incode==318:
            print('R0')
        else:
            print('UnknowKey')
            print(incode)
        print(inval)
        if inval==0:
            mctrl.STOP
        break
