#! /usr/bin/env python

import rospy
import tf2_ros
from tf2_geometry_msgs import PointStamped
from geometry_msgs.msg import TransformStamped, Twist
import math


if __name__ == "__main__":
    rospy.init_node("static_sub")
    buffer = tf2_ros.Buffer()
    sub = tf2_ros.TransformListener(buffer)
    pub = rospy.Publisher("/turtle2/cmd_vel",Twist,queue_size=1000)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        try:
            ts = buffer.lookup_transform("turtle2", "turtle1", rospy.Time(0))
            # rospy.loginfo("偏移量：(%.2f, %.2f, %.2f)", 
            #               ts.transform.translation.x,
            #               ts.transform.translation.y,
            #               ts.transform.translation.z)

            twist = Twist()
            twist.linear.x = 0.5 * math.sqrt(ts.transform.translation.x ** 2 + ts.transform.translation.y ** 2)
            twist.angular.z = 4 * math.atan2(ts.transform.translation.y, ts.transform.translation.x)
            pub.publish(twist)
        except Exception as e:
            rospy.logwarn("错误提示：%s", e)
        
        rate.sleep()
        