#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 串口发送节点程序
# 从速度订阅等中获取发送命令
# 转化成HEX码，从串口发送

import rospy
import serial
from pi_robot.msg import Serial_Send

    #data = "fffe"+hexs(wheel_l)+LL+hexs(wheel_r)+RR
    #data = data.decode("hex")
    #ser.write(data)
def ctrl(bytehex):
    ser.write(bytehex.decode("hex"))

def callback(data):
    ctrl(data.info)

def listener():
    rospy.init_node('serial_send', anonymous=True)
    rospy.Subscriber('serial_send', Serial_Send, callback)
    rospy.spin()
    ctrl("fffe00ff00ff")

if __name__ == '__main__':
    ser = serial.Serial("/dev/ttyUSB0",115200,timeout=1)
    listener()

