# ROS
## 1 ROS项目一般流程
#### 1.1 创建工作空间
```shell
mkdir -p workspace/src
cd ./workspace
catkin_make    # 初始化
```
#### 1.2 创建ros包并添加依赖
```shell
cd ./src
catkin_create_pkg ros_bag roscpp rospy std_msgs    # ros_bag:自定义ros包名 roscpp,rospy,std_msgs:依赖项
```
#### 1.3 编辑源文件
##### C++
```shell
cd ./ros_bag
vim xxx.cpp
```
```cpp
#include "ros/ros.h"

int main(int argc, char *argv[])
{
    // 节点初始化
    ros::init(argc, argv, "hello");
    // 创建句柄
    ros::NodeHandle nh;
    // 控制台输出日志
    ROS_INFO("hello world!");

    return 0;
}
```
##### Python
```shell
cd ./ros_bag
mkdir scripts
cd ./scripts
vim xxx.py
```
```python
#! /usr/bin/env python

import rospy

if __name__ == "__main__":
    # 节点初始化
    rospy.init_node("hello")
    # 输出日志
    rospy.loginfo("hello world!")
```
ps：记得给python文件添加可执行权限
```shell
chmod +x *.py
```
#### 1.4 编辑ros_bag的CMakeLists.txt文件
##### C++
```typescript
add_executable(源文件名 src/源文件名.cpp)

target_link_libraries(源文件名
    ${catkin_LIBRARIES}
)
```
##### Python
```typescript
catkin_install_python(PROGRAMS
    scripts/源文件名.py
    DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
```
#### 1.5 编译
```shell
cd workspace
catkin_make
```
#### 1.6 执行
命令行1
```shell
roscore
```
命令行2
```shell
cd workspace
source ./devel/setup.bash
rosrun ros_bag 源文件名       # 执行c++文件
rosrun ros_bag 源文件名.py    # 执行python文件
```
## 2 ROS通信机制
### 2.1 话题通信
#### 2.1.1 自定义msg
##### 创建msg文件
```shell
cd ros_bag
mkdir msg
vim xxx.msg
```
xxx.msg:
```txt
string xxx1
uint16 xxx2
float64  xxx3
...
```
##### 编辑package.xml文件
```xml
<build_depend>message_generation</build_depend>
<exec_depend>message_runtime</exec_depend>
```
##### 编辑CMakeLists.txt
```txt
find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  message_generation    #新添加的
)

add_message_files(
  FILES
  xxx.msg    # 新添加的
)

# 生成消息时依赖于 std_msgs
generate_messages(
  DEPENDENCIES
  std_msgs
)

#执行时依赖
catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES demo02_talker_listener
  CATKIN_DEPENDS roscpp rospy std_msgs message_runtime    # 添加message_runtime
#  DEPENDS system_lib
)

```
#### 2.1.2 源文件模板（C++）
##### 发布方
```cpp
#include "ros/ros.h"
#include "std_msgs/String.h"
// #include "ros_bag/xxx.h"    // xxx:自定msg的文件名

int main(int argc, char *argv[])
{
    // 设置编码
    setlocale(LC_ALL, "");

    // 初始化节点
    ros::init(argc, argv, "talker");

    // 创建句柄
    ros::NodeHandle nh;

    // 创建发布者对象
    ros::Publisher pub = nh.advertise<std_msgs::String>("chatter",10);
    // ros::Publisher pub = nh.advertise<ros_bag::xxx>("chatter",10);

    // 定义数据
    std_msgs::String msg;
    msg.data = "hello";
    // ros_bag::xxx msg;
    // msg.xxx1 = "hello";
    // msg.xxx2 = 100;
    // ...

    // 设置循环频率
    ros::Rate rate(1)    //一秒一次

    while (ros::ok())
    {
        // 发布消息
        pub.publish(msg);

        // 打印发送的消息
        ROS_INFO("msg:%s", msg.data.c_str());
        // ROS_INFO("msg:%s,%d", msg.xxx1.c_str(), msg.xxx2);

        // 休眠
        rate.sleep();
        
        // 官方建议
        ros::spinOnce();
    }
    return 0;
}
// 可自行添加计数器等
// 注释的语句为自定义msg的模板
```
##### 订阅方
```cpp
#include "ros/ros.h"
#include "std_msgs/String.h"

// 回调函数
void doMsg(const std_msgs::String::ConstPtr& msg){
    ROS_INFO("msg:%s", msg->data.c_str());
}

int main(int argc, char *argv[])
{
    // 设置编码
    setlocale(LC_ALL, "");

    // 初始化节点
    ros::init(argc, argv, "listener");

    // 创建句柄
    ros::NodeHandle nh;

    // 创建订阅者对象
    ros::Subscriber sub = nh.subscribe<std_msgs::String>("chatter", 10, doMsg);
    
    // 循环调用回调函数
    ros::spin();

    return 0；
}
// 订阅方的自定义msg实现改的地方与发布方类似
```
#### 2.1.3 源文件模板（Python）
##### 发布方
```python
#! /usr/bin/env python

import rospy
from std_msgs.msg import String
# from ros_bag.msg import xxx

if __name__ == "__main__":
    #  初始化节点
    rospy.init_node("talker_p")

    # 创建发布者对象
    pub = rospy.Publisher("chatter", String, queue_size=10)

    # 定义数据
    msg = String()
    msg.data = "hello"
    # msg = xxx()
    # msg.xxx1 = "hello"
    # msg.xxx2 = 100

    # 设置循环频率
    rate = rospy.Rate(1)

    while not rospy.is_shutdown():
        # 发布消息
        pub.publish(msg)

        # 打印发送的消息
        rospy.loginfo("msg:%s", msg.data)
        # rospy.loginfo("msg:%s,%d", msg.xxx1, msg.xxx2)

        # 休眠
        rate.sleep()

# 可自行添加计数器等
# 注释的语句为自定义msg的模板
```
##### 订阅方
```python
#! /usr/bin/env python

import rospy
from std_msgs.msg import String

# 回调函数
def doMsg(msg):
    rospy.loginfo("msg:%s", msg.data)

if __name__ = "__main__":
    # 初始化节点
    rospy.init_node("listener_p")
    # 创建订阅者对象
    sub = rospy.Subscriber("chatter", String, doMsg, queue_size=10)
    # 循环调用回调函数
    rospy.spin()

# 订阅方的自定义msg实现改的地方与发布方类似
```
