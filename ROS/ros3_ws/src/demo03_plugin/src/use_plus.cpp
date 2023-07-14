#include "ros/ros.h"
#include "pluginlib/class_loader.h"
#include "demo03_plugin/dbx_base.h"

int main(int argc, char *argv[])
{
    setlocale(LC_ALL, "");
    pluginlib::ClassLoader<dbx_base_ns::Dbx_Base> loader("demo03_plugin", "dbx_base_ns::Dbx_Base");
    boost::shared_ptr<dbx_base_ns::Dbx_Base> san = loader.createInstance("dbx_plugins_ns::SanBian");
    san->init(10);
    double length = san->getlength();
    ROS_INFO("三角形周长：%.2f", length);
    return 0;
}
