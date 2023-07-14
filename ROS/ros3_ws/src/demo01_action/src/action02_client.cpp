#include "ros/ros.h"
#include "actionlib/client/simple_action_client.h"
#include "demo01_action/addintsAction.h"

void done_cb(const actionlib::SimpleClientGoalState &state, const demo01_action::addintsResultConstPtr &result){
    if (state.state_ == state.SUCCEEDED){
        ROS_INFO("响应成功，最终结果 = %d", result->result);
    }else{
        ROS_INFO("请求失败！");
    }
}

void active_cb(){
    ROS_INFO("客户端与服务端连接建立...");
}

void feedback_cb(const demo01_action::addintsFeedbackConstPtr &feedback){
    ROS_INFO("当前进度：%.2f", feedback->progress);
}

int main(int argc, char *argv[])
{
    setlocale(LC_ALL, "");
    ros::init(argc, argv, "addints_client");
    ros::NodeHandle nh;
    actionlib::SimpleActionClient<demo01_action::addintsAction> client(nh, "addints");
    client.waitForServer();
    demo01_action::addintsGoal goal;
    goal.num = 100;
    client.sendGoal(goal, &done_cb, &active_cb, &feedback_cb);
    ros::spin();

    return 0;
}
