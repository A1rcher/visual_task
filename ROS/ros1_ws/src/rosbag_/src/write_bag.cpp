#include "ros/ros.h"
#include "rosbag/bag.h"
#include "std_msgs/String.h"

int main(int argc, char *argv[])
{
    ros::init(argc, argv, "write_bag");
    ros::NodeHandle nh;
    rosbag::Bag bag;
    bag.open("hello01.bag", rosbag::BagMode::Write);
    std_msgs::String msg;
    msg.data = "hello xxx";
    bag.write("/chatter", ros::Time::now(), msg);
    bag.write("/chatter", ros::Time::now(), msg);
    bag.write("/chatter", ros::Time::now(), msg);
    bag.write("/chatter", ros::Time::now(), msg);

    bag.close();
    return 0;
}
