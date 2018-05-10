#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 超声波探测节点 "waves"
# 驱动超声波模块测距
# 将距离信息发布到订阅 "distance"
# 单位：CM

import rospy
import time
import RPi.GPIO as GPIO
from  pi_robot.msg import Distance

# 接口设置
Trig = 23
Echo_L = 5
Echo_F = 6
Echo_R = 13

# 变量设置
Long_Max = 400   # cm  最大输出距离
T_Max = 0.05  # s   最大检测等待时长
V_Sound = 340 # m/s 声速设定值
Fre_Scan = 10    # Hz  扫描频率

def distance():
    pub = rospy.Publisher('distance', Distance, queue_size=10)
    rospy.init_node('waves', anonymous=True)
    rate = rospy.Rate(Fre_Scan)
    # 初始化IO口
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(Trig,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(Echo_L,GPIO.IN)
    GPIO.setup(Echo_F,GPIO.IN)
    GPIO.setup(Echo_R,GPIO.IN)
    # 循环检测
    while not rospy.is_shutdown():
        GPIO.output(Trig,GPIO.HIGH) # 检测使能信号
        time.sleep(0.000015)
        GPIO.output(Trig,GPIO.LOW)
        T0F,T0L,T0R = 0,0,0 # 上升沿时间
        T1F,T1L,T1R = 0,0,0 # 下降沿时间
        T0 = time.time()    # 使能后时间
        while True:
            T = time.time() # 当前的时间
            # 前侧
            Info_F = GPIO.input(Echo_F)
            if Info_F:
                if T0F==0:
                    T0F = T
            else:
                if T0F and (not T1F):
                    T1F = T
            # 左侧
            Info_L = GPIO.input(Echo_L)
            if Info_L:
                if T0L==0:
                    T0L = T
            else:
                if T0L and (not T1L):
                    T1L = T
            # 右侧
            Info_R = GPIO.input(Echo_R)
            if Info_R:
                if T0R==0:
                    T0R = T
            else:
                if T0R and (not T1R):
                    T1R = T
            # 超时检测
            if (T-T0)>=T_Max:
                break
        Long_F = int((T1F-T0F)*34000/2)
        Long_L = int((T1L-T0L)*34000/2)
        Long_R = int((T1R-T0R)*34000/2)
        # 超长修复
        if (Long_F<3) or (Long_F>Long_Max):
            Long_F = Long_Max
        if (Long_L<3) or (Long_L>Long_Max):
            Long_L= Long_Max
        if (Long_R<3) or (Long_R>Long_Max):
            Long_R = Long_Max
        car_distance = Distance()
        car_distance.front = Long_F
        car_distance.left = Long_L
        car_distance.right = Long_R
        rospy.loginfo("Left:%3s  Front:%3s  Right:%3s",Long_L,Long_F,Long_R)
        pub.publish(car_distance)
        rate.sleep()

if __name__ == '__main__':
    try:
        rospy.loginfo("waves begin")
        distance()
    except rospy.ROSInterruptException:
        GPIO.cleanup()
        rospy.loginfo("waves end")
