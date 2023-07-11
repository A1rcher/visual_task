#!/usr/bin/env python3

import rospy
import tf2_ros
from tf2_geometry_msgs import PointStamped

if __name__ == "__main__":
    rospy.init_node("static_sub")
    buffer = tf2_ros.Buffer()
    sub = tf2_ros.TransformListener(buffer)
    ps = PointStamped()
    ps.header.frame_id = "laser"
    ps.header.stamp = rospy.Time.now()
    ps.point.x = 2.0
    ps.point.y = 3.0
    ps.point.z = 5.0

    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        try:
            ps_out = buffer.transform(ps, "base_link")
            rospy.loginfo("坐标：(%.2f, %.2f, %.2f)", ps_out.point.x, ps_out.point.y, ps_out.point.z)
            rate.sleep()
        except Exception as e:
            rospy.logwarn("错误提示：%s", e)
        