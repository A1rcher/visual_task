#include "ros/ros.h"

int main(int argc, char *argv[])
{
    ros::init(argc, argv, "set_parame_c");
    ros::NodeHandle nh;
    nh.setParam("type","xiaohuang");
    nh.setParam("radius",0.15);

    ros::param::set("type_param", "xiaobai");
    ros::param::set("radius_param", 0.15);

    nh.setParam("radius", 0.1);
    ros::param::set("radius_param", 0.1);
    return 0;
}
