#! /usr/bin/env python

import rospy
from plumbing_pub_sub.msg import Person

if __name__ == "__main__":
    rospy.init_node("daMa")
    pub = rospy.Publisher("liaotian", Person, queue_size=10)
    p = Person()
    p.name = "lisi"
    p.age = 8
    p.height = 1.85
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        pub.publish(p)
        rospy.loginfo("msg:%s,%d,%.2f", p.name, p.age, p.height)
        rate.sleep()

