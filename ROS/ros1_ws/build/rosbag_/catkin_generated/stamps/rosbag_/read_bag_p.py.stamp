#! /usr/bin/env python

import rospy
from rosbag import Bag

if __name__ == "__main__":
    rospy.init_node("read_bag_p")
    bag = Bag("hello_p.bag", "r")

    msgs = bag.read_messages("/chatter")
    for topic, msg, time in msgs:
        rospy.loginfo("解析的内容，话题：%s，时间戳：%s，消息：%s", topic, time, msg.data)
    bag.close()


