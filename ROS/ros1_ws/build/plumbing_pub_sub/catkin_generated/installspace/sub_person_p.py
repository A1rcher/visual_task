#!/usr/bin/env python3

import rospy
from plumbing_pub_sub.msg import Person

def doPerson(p:Person):
    rospy.loginfo("sub msg:%s, %d, %.2f", p.name, p.age, p.height)

if __name__ == "__main__":
    rospy.init_node('daye')
    sub = rospy.Subscriber("liaotian",Person, doPerson)
    rospy.spin()