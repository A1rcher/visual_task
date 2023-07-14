#! /usr/bin/env python

import rospy 
import actionlib
from demo01_action.msg import addintsAction,addintsFeedback,addintsResult

class MyAction:
    def __init__(self):
        self.server = actionlib.SimpleActionServer("addints", addintsAction, self.cb,False)
        self.server.start()
        rospy.loginfo("服务端启动...")

    def cb(self, goal):
        goal_num = goal.num
        rospy.loginfo("目标值：%d", goal_num)
        rate = rospy.Rate(10)
        sum = 0
        for i in range(1, goal_num+1):
            sum = sum + i
            fb_obj = addintsFeedback()
            fb_obj.progress = i/ goal_num
            self.server.publish_feedback(fb_obj)
            rate.sleep()

        rospy.loginfo("最终结果：%d", sum)
        result = addintsResult()
        result.result = sum
        self.server.set_succeeded(result)

if __name__ == "__main__":
    rospy.init_node("addints_server_p")
    myAction = MyAction()
    rospy.spin()