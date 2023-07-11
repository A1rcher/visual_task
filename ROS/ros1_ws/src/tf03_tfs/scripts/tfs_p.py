#! /usr/bin/env python

import rospy
import tf2_ros
from tf2_geometry_msgs import PointStamped
from geometry_msgs.msg import TransformStamped

if __name__ == "__main__":
    rospy.init_node("static_sub")
    buffer = tf2_ros.Buffer()
    sub = tf2_ros.TransformListener(buffer)
    ps = PointStamped()
    ps.header.frame_id = "son1"
    ps.header.stamp = rospy.Time()
    ps.point.x = 1.0
    ps.point.y = 2.0
    ps.point.z = 3.0

    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        try:
            ts = buffer.lookup_transform("son2", "son1", rospy.Time(0))
            rospy.loginfo("偏移量：(%.2f, %.2f, %.2f)", 
                          ts.transform.translation.x,
                          ts.transform.translation.y,
                          ts.transform.translation.z)

            ps_out = buffer.transform(ps, "son2")
            rospy.loginfo("坐标：(%.2f, %.2f, %.2f)", ps_out.point.x, ps_out.point.y, ps_out.point.z)
            rate.sleep()
        except Exception as e:
            rospy.logwarn("错误提示：%s", e)
        