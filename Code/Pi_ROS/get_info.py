#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# 作者：曹沛文
# 功能：从串口接收消息并打印

import serial

ser=serial.Serial("/dev/ttyUSB0",115200,timeout=1)
print("TTY is already")

data = ''
data = data.encode('utf-8')
flag = b'\xff'

while True:
    temp = ser.read(1)
    if temp == flag:
        print(data)
        data = ''
        data = data.encode('utf-8')
    data = data + temp

