#include "ros/ros.h"

int main(int argc, char *argv[])
{
    ros::init(argc,argv,"change_bgr");
    ros::NodeHandle nh("turtlesim");
    nh.setParam("background_r", 255);
    nh.setParam("background_g", 255);
    nh.setParam("background_b", 255);
    // ros::param::set("/turtlesim/background_r", 100);
    // ros::param::set("/turtlesim/background_g", 255);
    // ros::param::set("/turtlesim/background_b", 100);
    return 0;
}
