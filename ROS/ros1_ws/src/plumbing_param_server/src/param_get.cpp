#include "ros/ros.h"

int main(int argc, char *argv[])
{
    setlocale(LC_ALL, "");
    ros::init(argc, argv, "get_param_c");
    ros::NodeHandle nh;

    double radius = nh.param("radius", 0.5);
    ROS_INFO("radius = %.2f", radius);

    double radius2;
    // bool result = nh.getParam("radius",radius2);
    bool result = nh.getParamCached("radius", radius2);
    if (result){
        ROS_INFO("radus = %.2f", radius2);
    }else{
        ROS_INFO("err");
    }

    std::vector<std::string> names;
    nh.getParamNames(names);
    for (auto &&name:names)
    {
        ROS_INFO("%s", name.c_str());
    }

    bool flag1 = nh.hasParam("radius");
    bool flag2 = nh.hasParam("radiusxxx");
    ROS_INFO("flag1 = %d", flag1);
    ROS_INFO("flag2 = %d", flag2);

    std::string key;
    nh.searchParam("radius", key);
    ROS_INFO("key = %s", key.c_str());

    
    return 0;
}
