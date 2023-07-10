#! /usr/bin/env python

import rospy
from plumbing_server_client.srv import *
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        rospy.logerr("err")
        sys.exit(1)
    
    rospy.init_node("erhei")
    client = rospy.ServiceProxy("addints", Addints)
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
    client.wait_for_service()
    # rospy.wait_for_service("addints")
    response = client.call(num1,num2)
    rospy.loginfo("响应的数据:%d", response.sum)
