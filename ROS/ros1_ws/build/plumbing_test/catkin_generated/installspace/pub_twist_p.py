#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

if __name__ == "__main__":
    rospy.init_node("my_control_p")
    pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)
    twist = Twist()
    twist.linear.x = 1.0
    twist.linear.y = 0.0
    twist.linear.z = 0.0
    twist.angular.x = 0.0
    twist.angular.y = 0.0
    twist.angular.z = 1.0
    rate = rospy.Rate(10)
    
    while not rospy.is_shutdown():
        pub.publish(twist)
        rate.sleep()
        