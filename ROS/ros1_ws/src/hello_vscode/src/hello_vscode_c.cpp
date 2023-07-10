#include "ros/ros.h"

int main(int argc, char *argv[])
{
    //解决中文乱码问题
    // setlocale(LC_ALL, "");
    setlocale(LC_CTYPE, "zh_CN.utf-8");
    ros::init(argc,argv,"hello_c");
    ROS_INFO("hello vscode, 你好");

    return 0;
}
