#!/usr/buin/env python3

import rospy
from rosbag import Bag
from std_msgs.msg import String

if __name__ == "__main__":
    rospy.init_node("write_bag_p")
    bag = Bag("hello_p.bag", "w")
    msg = String()
    msg.data = "hello xxx"
    bag.write("/chatter", msg)
    bag.write("/chatter", msg)
    bag.write("/chatter", msg)
    bag.write("/chatter", msg)
    bag.write("/chatter", msg)
    bag.close()