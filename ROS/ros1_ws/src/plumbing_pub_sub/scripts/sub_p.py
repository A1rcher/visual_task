#! /usr/bin/env python

import rospy
from std_msgs.msg import String

def doMsg(msg):
    rospy.loginfo("sent's msg:%s", msg.data)

if __name__ == "__main__":
    rospy.init_node('wu')
    sub = rospy.Subscriber("chatter", String, doMsg, queue_size=10)
    rospy.spin()

