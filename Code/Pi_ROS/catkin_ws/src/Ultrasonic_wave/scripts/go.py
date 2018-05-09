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
F_Stop = 10 # cm 前方停车阈值
S_Stop = 8  # cm 侧方停车阈值
F_Slow = 50 # cm 前方减速阈值
S_Slow = 30 # cm 侧方加速阈值

def tranhex(num):
    a = hex(num)
    a = a.strip('0x')
    if len(a)==1:
        a = '0' + a
        return a
def callback(data):
    V = VG
    TL,TR,T = 0,0,0
    data_f = data.front
    data_l = data.left
    data_r = data.right
    # 前向处理
    if data_f<=F_Stop:
        V = 0
    elif data_f<=F_Slow:
        V = V * (data_f - F_Stop)/float(F_Slow - F_Stop)
    # 左向处理
    if data_l<=S_Stop:
        TL = VT
    elif data_l<=S_Slow:
        TL = VT * (S_Slow - data_l)/float(S_Slow - S_Stop)
    # 右向处理
    if data_r<=S_Stop:
        TR = VT
    elif data_r<=S_Slow:
        TR = VT * (S_Slow - data_r)/float(S_Slow - S_Stop)
    # 汇总处理
    T = TL - TR
    VL = int(V - T)
    VR = int(V + T)
    # 显示计算后原始信息
    #rospy.loginfo("V:%2s  T:%2s  VL:%2.3f  VR:%2.3f ",V,T,TL,TR)
    # 显示两电机设定值
    rospy.loginfo("VL:%2s  VR:%2s",VL,VR)

def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber('chatter', Distance, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()

