#!/usr/bin/env python3

import rospy

if __name__ == "__main__":
    rospy.init_node("get_param_p")
    radius = rospy.get_param("radius_p", 0.5)
    radius1 = rospy.get_param("radius_p_xxx", 0.5)
    rospy.loginfo("radius = %.2f", radius)
    rospy.loginfo("radius = %.2f", radius1)

    names = rospy.get_param_names()
    for name in names:
        rospy.loginfo("%s", name)

    flag1 = rospy.has_param("radius_p")
    if flag1:
        rospy.loginfo("has")
    else:
        rospy.loginfo("not has")

    key = rospy.search_param("radius_p")
    rospy.loginfo("key = %s", key)
