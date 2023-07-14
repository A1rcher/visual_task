#include "ros/ros.h"
#include "actionlib/server/simple_action_server.h"
#include "demo01_action/addintsAction.h"

typedef actionlib::SimpleActionServer<demo01_action::addintsAction> Server;

void cd(const demo01_action::addintsGoalConstPtr &goalPtr, Server* server){
    int goal_num = goalPtr->num;
    ROS_INFO("客户端提交的目标值是：%d", goal_num);
    ros::Rate rate(10);
    int result = 0;
    for (int i=1; i<=goal_num; i++)
    {
        result += i;
        demo01_action::addintsFeedback fb;
        fb.progress = i / double(goal_num);
        server->publishFeedback(fb);
        rate.sleep();
    }
    demo01_action::addintsResult r;
    r.result = result;
    server->setSucceeded(r); 
}

int main(int argc, char *argv[])
{
    setlocale(LC_ALL, "");
    ros::init(argc,argv,"addints_server");
    ros::NodeHandle nh;
    Server server(nh, "addints", boost::bind(&cd, _1, &server),false);
    server.start();
    ros::spin();
    return 0;
}
