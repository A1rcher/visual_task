#!/usr/bin/env python3

import rospy
from dynamic_reconfigure.server import Server
from demo02_dr.cfg import drConfig

def cb(drConfig, level):
    rospy.loginfo("修改后的整形数据是：%d, %.2f, %s, %d, %d", 
             drConfig.int_param,
             drConfig.double_param,
             drConfig.str_param,
             drConfig.bool_param,
             drConfig.list_param)
    return drConfig

if __name__ == "__main__":
    rospy.init_node("dr_server_p")
    server = Server(drConfig, cb)

    rospy.spin()