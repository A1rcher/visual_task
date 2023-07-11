#include "ros/ros.h"
#include "std_msgs/String.h"
#include <sstream>

int main(int argc, char *argv[])
{
    setlocale(LC_ALL, "");
    // 初始化
    ros::init(argc, argv, "talker");
    // 实例化ros句柄
    ros::NodeHandle nh;
    // 实例化 发布者 对象
    ros::Publisher pub = nh.advertise<std_msgs::String>("/chatter", 10);
    
    std_msgs::String msg;

    ros::Rate rate(1);
    int count = 0;
    ros::Duration(3).sleep();
    while(ros::ok())
    {
        count++;
        // msg.data = "hello";
        std::stringstream ss;
        ss << "hello --->" << count;
        msg.data = ss.str();
        
        pub.publish(msg);
        ROS_INFO("msg:%s", ss.str().c_str());
        rate.sleep();
        ros::spinOnce();
    }

    return 0;
}

