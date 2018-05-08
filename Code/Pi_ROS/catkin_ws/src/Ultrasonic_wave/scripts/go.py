#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 超声波避障程序
# 从超声波订阅中获取障碍物距离
# 计算生成左右轮转速控制信号，直接从串口发送

import rospy
import serial
from  ultrasound_wave.msg import Distance

# 变量设置
VG = 16 #前进速度
VT = 8  #转向速度
F_Stop = 5  # cm 前方停车阈值
S_Stop = 8  # cm 侧方停车阈值
F_Slow = 30 # cm 前方减速阈值
S_Slow = 30 # cm 侧方加速阈值

def tranhex(num):
    a = hex(num)
    a = a.strip('0x')
    if len(a)==1:
        a = '0' + a
        return a
def callback(data):
    #rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data.front)
    #rospy.loginfo('Left:%3s cm   Front:%3s cm   Right:%3s cm',data.left,data.front,data.right)
    V = VG
    TL,TR,T = 0,0,0
    if data.front<=F_Stop:
        V = 0
    elif data.front<=F_Slow:
        V = V * (data.front - F_Stop)/(F_Slow - F_Stop)

    if data.left<=S_Stop:
         TL = VT
    elif data.front<=S_Slow:
        TL = VT * (S_Slow - data.left)/(S_Slow - S_Stop)

    if data.right<=S_Stop:
         TR = VT
    elif data.right<=S_Slow:
        TR = VT * (S_Slow - data.right)/(S_Slow - S_Stop)
    T = TL - TR
    VL = VG - T
    VR = VG + T
    rospy.loginfo("VL:%3s  VR:%3s ",VL,VR)

def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber('chatter', Distance, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()

