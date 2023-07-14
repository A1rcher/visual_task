#!/usr/bin/env python3

import rospy
from turtlesim.msg import Pose
import tf2_ros
from geometry_msgs.msg import TransformStamped
from tf import transformations
import sys

turtle_name = ""

def doPose(pose:Pose):
    pub = tf2_ros.TransformBroadcaster()
    ts = TransformStamped()
    ts.header.frame_id = "world"
    ts.header.stamp = rospy.Time.now()
    ts.child_frame_id = turtle_name

    ts.transform.translation.x = pose.x
    ts.transform.translation.y = pose.y
    ts.transform.translation.z = 0

    qtn = transformations.quaternion_from_euler(0, 0, pose.theta)
    ts.transform.rotation.x = qtn[0]
    ts.transform.rotation.y = qtn[1]
    ts.transform.rotation.z = qtn[2]
    ts.transform.rotation.w = qtn[3]

    pub.sendTransform(ts)

if __name__ == "__main__":
    rospy.init_node("dynamic_pub_p")
    turtle_name = sys.argv[1]
    sub = rospy.Subscriber(f"/{turtle_name}/pose", Pose, doPose, queue_size=100)
    rospy.spin()
