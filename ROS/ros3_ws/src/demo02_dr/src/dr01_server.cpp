#include "ros/ros.h"
#include "dynamic_reconfigure/server.h"
#include "demo02_dr/drConfig.h"

void cb(demo02_dr::drConfig &config, uint32_t level){
    ROS_INFO("修改后的整形数据是：%d, %.2f, %s, %d, %d", 
             config.int_param,
             config.double_param,
             config.str_param.c_str(),
             config.bool_param,
             config.list_param);
}

int main(int argc, char *argv[])
{
    setlocale(LC_ALL, "");
    ros::init(argc,argv, "dr_server");
    dynamic_reconfigure::Server<demo02_dr::drConfig> server;
    server.setCallback(boost::bind(&cb, _1, _2));
    ros::spin();
    return 0;
}
