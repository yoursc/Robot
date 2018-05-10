#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 超声波避障程序
# 从超声波订阅中获取障碍物距离
# 计算生成左右轮转速控制信号，直接从串口发送

import rospy
import serial
from pi_robot.msg import Distance
from pi_robot.msg import Speed

# 变量设置
VG = 16     # 前进速度
VT = 16     # 转向速度
F_Stop = 8  # cm 前方停车阈值
S_Stop = 8  # cm 侧方停车阈值
F_Slow = 20 # cm 前方减速阈值
S_Slow = 15 # cm 侧方加速阈值

VL_OLD,VR_OLD= 0,0

def hexs(num):
    a = hex(abs(num))
    # 转换为hex值
    # 输入绝对值范围：0-255
    # 输出：00-ff
    if len(a)==4:
        b = a[2]+ a[3]
    else:
        b = "0" + a[2]
    return b

def ctrl(wheel_l,wheel_r):
    LL,RR="ff","ff"
    if wheel_l<0:
        LL = "00"
    if wheel_r<0:
        RR = "00"
    data = "fffe"+hexs(wheel_l)+LL+hexs(wheel_r)+RR
    data = data.decode("hex")
    ser.write(data)

def callback(data):
    global VL_OLD,VR_OLD
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
    T = TR - TL
    VL = int(V - T)
    VR = int(V + T)
    if (VL != VL_OLD)or(VR != VR_OLD):
        motor_speed = Speed()
        motor_speed.left  = VL
        motor_speed.right = VR
        VL_OLD = VL
        VR_OLD = VR
        # 输出
        pub.publish(motor_speed)
        ctrl(VL,VR)
        # 显示计算后原始信息

        #rospy.loginfo("V:%2s  T:%2s  VL:%2.3f  VR:%2.3f ",V,T,TL,TR)
        # 显示两电机设定值
        rospy.loginfo("VL:%2s  VR:%2s",VL,VR)

def listener():
    rospy.init_node('speed_nav', anonymous=True)
    rospy.Subscriber('distance', Distance, callback)
    rospy.spin()
    ctrl(0,0)

if __name__ == '__main__':
    ser = serial.Serial("/dev/ttyUSB0",115200,timeout=1)
    pub = rospy.Publisher('speed', Speed, queue_size=10)
    listener()

