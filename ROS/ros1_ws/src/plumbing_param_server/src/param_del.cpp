#include "ros/ros.h"

int main(int argc, char *argv[])
{
    ros::init(argc, argv, "param_del_c");
    ros::NodeHandle nh;
    bool flag1 = nh.deleteParam("radius");
    if (flag1)
    {
        ROS_INFO("deleted");
    }else{
        ROS_INFO("undeleted");
    }

    bool  flag2 = ros::param::del("radius_param");
    if (flag2)
    {
        ROS_INFO("deleted");
    }else{
        ROS_INFO("undeleted");
    }    return 0;
}
