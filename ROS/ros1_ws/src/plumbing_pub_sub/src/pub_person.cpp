#include "ros/ros.h"
#include "plumbing_pub_sub/Person.h"


int main(int argc, char *argv[])
{
    setlocale(LC_ALL, "");
    ros::init(argc, argv, "sent_person");
    ros::NodeHandle nh;
    ros::Publisher pub = nh.advertise<plumbing_pub_sub::Person>("liaotian", 10);
    plumbing_pub_sub::Person person;
    person.name = "张三";
    person.age = 1;
    person.height = 1.73;

    ros::Rate rate(1);

    while (ros::ok()){
        pub.publish(person);
        person.age++;
        ROS_INFO("msg:%s,%d,%.2f", person.name.c_str(), person.age, person.height);
        rate.sleep();
        ros::spinOnce();

    }


    return 0;
}
