#! /usr/bin/env python

import rospy
import actionlib
from demo01_action.msg import *

def done_cb(status, result):
    if status == actionlib.GoalStatus.SUCCEEDED:
        rospy.loginfo("最终响应结果：%d", result.result)
    else:
        rospy.loginfo(" 响应失败！")

def active_cb():
    rospy.loginfo("连接建立...")

def feedback_cb(feedback):
    rospy.loginfo("当前进度：%.2f", feedback.progress)

if __name__ == "__main__":
    rospy.init_node("addint_client_p")
    client = actionlib.SimpleActionClient("addints", addintsAction)
    client.wait_for_server()
    goal = addintsGoal()
    goal.num = 100
    client.send_goal(goal, done_cb, active_cb, feedback_cb)
    rospy.spin()