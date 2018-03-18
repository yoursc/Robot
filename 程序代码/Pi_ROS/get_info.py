#!/usr/bin/python3
# -*- coding:utf-8 -*-

# 作者：曹沛文
# 功能：从串口接收消息并打印

import serial

ser=serial.Serial("/dev/ttyUSB0",115200,timeout=1)
print("TTY is already")

while True:
    while True :
        s=b'\xff'
        get = ser.read(1)
        s = s + get
        if get==b'\xff' :
            break
    print(ser.read(8))
