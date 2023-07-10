#include "ros/ros.h"
#include "plumbing_server_client/Addints.h"

int main(int argc, char *argv[])
{
    setlocale(LC_ALL, "");
    if (argc != 3){
        ROS_INFO("err");
        return 1;
    }
    ros::init(argc, argv, "dabao");
    ros::NodeHandle nh;
    ros::ServiceClient client = nh.serviceClient<plumbing_server_client::Addints>("addints");
    plumbing_server_client::Addints ai;
    ai.request.num1 = atoi(argv[1]);
    ai.request.num2 = atoi(argv[2]);
    // client.waitForExistence();
    ros::service::waitForService("addints");
    bool flag = client.call(ai);
    if (flag)
    {
        ROS_INFO("响应结果:%d", ai.response.sum);
    }else{
        ROS_INFO("failure...");
    }

    return 0;
}
