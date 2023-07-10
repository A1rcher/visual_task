#!/usr/bin/env python3

import rospy
from plumbing_server_client.srv import *

def doNum(request:AddintsRequest):
    num1 = request.num1
    num2 = request.num2

    sum = num1 + num2
    response = AddintsResponse()
    response.sum = sum
    rospy.loginfo("num1 = %d, num2 = %d, sum = %d", num1, num2, sum)

    return response


if __name__ == "__main__":
    rospy.init_node("heishui")
    server = rospy.Service("addints", Addints, doNum)
    rospy.loginfo("服务器启动")
    rospy.spin()