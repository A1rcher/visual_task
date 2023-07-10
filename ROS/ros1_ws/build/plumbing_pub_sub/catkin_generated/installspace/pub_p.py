#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

if __name__ == "__main__":
    rospy.init_node('sent')
    pub = rospy.Publisher('chatter', String, queue_size=10)
    msg = String()
    rate = rospy.Rate(1)
    count = 0
    while not rospy.is_shutdown():
        count += 1
        msg.data = 'hello' + str(count)
        rospy.loginfo(f"msg:{msg.data}")
        pub.publish(msg)
        rate.sleep()

