#!/usr/bin/env python3
import rospy

if __name__ == "__main__":
    rospy.init_node("change_bgr_p")
    rospy.set_param("/turtlesim/background_r", 100)
    rospy.set_param("/turtlesim/background_g", 50)
    rospy.set_param("/turtlesim/background_r", 150)
    