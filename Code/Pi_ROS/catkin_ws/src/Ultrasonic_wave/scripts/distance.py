#!/usr/bin/env python

import rospy
from  ultrasound_wave.msg import Distance

def distance():
    pub = rospy.Publisher('chatter', Distance, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        car_distance = Distance()
        car_distance.front  = 1
        car_distance.left = 2
        car_distance.right = 3
        rospy.loginfo(car_distance)
        pub.publish(car_distance)
        rate.sleep()

if __name__ == '__main__':
    try:
        distance()
    except rospy.ROSInterruptException:
        pass
