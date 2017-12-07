#!/usr/bin/python
# -*- coding:utf-8 -*-

from evdev import InputDevice
from select import select

dev = InputDevice('/dev/input/event0')

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
            print(inval)
        elif incode==1:
            print('LG')
            print(inval)
        elif incode==2:
            print('L2')
            print(inval)
        elif incode==3:
            print('RT')
            print(inval)
        elif incode==4:
            print('RG')
            print(inval)
        elif incode==5:
            print('R2')
            print(inval)
        # type int1u
        elif incode==16:
            if inval==1:
                print('Right')
            elif (inval== -1):
                print('Left')
        elif incode==17:
            if inval==-1:
                print('Up')
            elif inval==1:
                print('Down')
        if incode==304:
            print('A')
        elif incode==305:
            print('B')
        elif incode==307:
            print('X')
        elif incode==308:
            print('Y')
        elif incode==314:
            print('SELET')
        elif incode==316:
            print('HOME')
        elif incode==310:
            print('L1')
        elif incode==311:
            print('R1')
        elif incode==317:
            print('L0')
        elif incode==318:
            print('R0')

        else:
            print('UnknowKey')
            print(incode)
            print(inval)
        break
