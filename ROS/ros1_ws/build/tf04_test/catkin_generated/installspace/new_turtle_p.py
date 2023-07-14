#!/usr/bin/env python3

import rospy
from turtlesim.srv import Spawn,SpawnRequest, SpawnResponse

if __name__ == "__main__":
    rospy.init_node("server_call_p")
    client = rospy.ServiceProxy("/spawn", Spawn)
    request = SpawnRequest()
    request.x = 1.0
    request.y = 2.0
    request.theta = -3.0
    request.name = "turtle2"
    client.wait_for_service()
    response = client.call(request)
    rospy.loginfo("name:%s", response.name)
