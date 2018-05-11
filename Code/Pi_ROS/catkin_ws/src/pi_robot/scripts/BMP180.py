#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 气压检测节点
# 读取BMP180芯片
# 将相关环境信息发布到订阅 "BMP180"

import rospy
import time
import BMP180_Dri
from pi_robot.msg import BMP180

Fre_Scan = 1 # Hz 扫描周期

def main():
    pub = rospy.Publisher('bmp180', BMP180, queue_size=10)
    rospy.init_node('bmp180', anonymous=True)
    rospy.loginfo("Node bmp180 is begin")
    rate = rospy.Rate(Fre_Scan)
    while not rospy.is_shutdown():
        bmp = BMP180_Dri.BMP180()
        data = BMP180()
        data.temperature = bmp.read_temperature()
        data.pressure    = bmp.read_pressure()
        data.altitude    = bmp.read_altitude()
        rospy.loginfo("%.2f C  %.2f h  %.2f m",data.temperature,(data.pressure/100.0),data.altitude)
        pub.publish(data)
        rate.sleep()
    rospy.loginfo("bmp180 node end")

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
