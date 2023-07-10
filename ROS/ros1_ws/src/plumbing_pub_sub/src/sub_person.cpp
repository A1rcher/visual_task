#include "ros/ros.h"
#include "plumbing_pub_sub/Person.h"

void doPerson(const plumbing_pub_sub::Person::ConstPtr& p){
    ROS_INFO("person's msg:%s,%d,%.2f", p->name.c_str(), p->age, p->height);
}

int main(int argc, char *argv[])
{
    setlocale(LC_ALL, "");
    ros::init(argc, argv, "xuesheng");
    ros::NodeHandle nh;
    ros::Subscriber sub = nh.subscribe("liaotian",10,doPerson);

    ros::spin();
    return 0;
}
