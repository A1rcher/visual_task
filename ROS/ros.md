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
cd msg
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
```typescript
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
### 2.2服务通信
#### 2.2.1自定义srv
##### 创建srv文件
```shell
cd ros_bag
mkdir srv
cd srv
vim xxx.srv
```
srv文件：
```txt
# request
int32 num1
int32 num2
---
# response
int32 sum
```
##### 编辑package.xml
```xml
<build_depend>message_generation</build_depend>
<exec_depend>message_runtime</exec_depend>
```
##### 编辑CMakeLists.txt
```typescript
find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  message_generation    # 新添加的
)

add_service_files(
  FILES
  xxx.srv    # 新添加的
)

# 解锁
generate_messages(
  DEPENDENCIES
  std_msgs
)

```
#### 2.2.2 源文件模板（C++）
##### 服务端
```cpp
#include "ros/ros.h"
#include "ros_bag/xxx.h"

// 回调函数，bool返回值为是否处理成功
bool deReq(ros_bag::xxx::Request& req,ros_bag::xxx::Response& resp){
    int num1 = req.num1;
    int num2 = req.num2;
    if (输入有误){
        return false;    
    }
    resp.sum = num1 + num2;
    return true
}

int main(int argc, char *argv[])
{
    setlocale(LC_ALL, "");
    // 初始化节点
    ros::init(argc, argv, "server");
    // 创建句柄
    ros::NodeHandle nh;
    // 创建服务对象
    ros::ServiceServer server = nh.advertiseService("chatter", doReq);
    // 循环调用回调函数
    ros::spin();
    return 0;
}
```
##### 客户端
```cpp
#include "ros/ros.h"
#include "ros_bag/xxx.h"

int main(int argc, char *argv[])
{
    setlocale(LC_ALL, "");
    
    // 检查输入是否错误
    if (argc != 3){
        ROS_ERROR("输入错误");
        return 1;
    }

    // 初始化节点
    ros::init(argc, argv, "client");

    //创建句柄
    ros::NodeHandle nh;

    // 创建客户端对象
    ros::ServiceClient client = nh.serviceClient<ros_bag::xxx>("chatter");

    // 等待服务启动
    ros::service::waitForService("chatter");
    // client.waitForService();

    // 定义请求数据
    ros_bag::xxx add_num;
    add_num.request.num1 = atoi(argv[1]);
    add_num.request.num2 = atoi(argv[2]);

    // 发送请求，并返回bool值
    bool flag = client.call(add_num);

    // 处理响应
    if (flag){
        ROS_INFO("sum:%d", add_num.response.sum);
    }
    else{
        ROS_ERROR("err!");
        return 1;
    }
     return 0;
}
```
#### 2.2.3 源文件模板（Python）
##### 服务端
```python
#! /usr/bin/env python

import rospy
from ros_bag.srv import xxx, xxxRequest, xxxResponse

# 回调函数
def doReq(req):
    sum = req.num1 + req.num2
    resp = xxxResponse()
    resp.sum = sum
    return resp

if __name__ == "__main__":
    # 初始化节点
    rospy.init_node("server_p")
    # 创建服务端对象
    server = rospy.Service("chatter", xxx, doReq)
    # 循环调用回调函数
    rospy.spin()
```
##### 客户端
```python
#! /usr/bin/env python

import rospy
from ros_bag.srv import *
import sys

if __name__ == "__main__":
    # 判断输入是否有误
    if len(sys.argv) != 3:
        rospy.logerr("输入错误")
        sys.exit(1)

    # 初始化节点
    rospy.init_node("client_p")

    # 创建请求对象
    client = rospy.ServiceProxy("chatter", xxx)

    # 等待服务器
    rospy.wait_for_service("chatter")
    # client.wait_for_service()

    # 定义数据
    req = xxxRequest()
    req.num1 = int(sys.argv[1])
    req.num2 = int(sys.argv[2])

    # 发送请求
    resp = client.call(req)

    # 输出信息
    rospy.loginfo("sum:%d", resp.sum)
    
```
### 2.3 参数服务器
#### 2.3.1 新增（修改）参数
##### C++
```cpp
// 使用NodeHandle
ros::NodeHandle nh;
nh.setParam("nh_int", 10);
nh.setParam("nh_double", 10.0);
nh.setParam("nh_bool", true);
nh.setParam("nh_string", "hello");
nh.setParam("nh_vector", _vector);
nh.setParam("nh_map", _map);
// 修改（相同的键，不同的值）

// 使用param
ros::param::set("param_int", 10);
...

```
##### python
```python
rospy.set_param("p_int", 10)
rospy.set_param("p_double", 10.0)
rospy.set_param("p_bool", True)
rospy.set_param("p_string", "hello")
rospy.set_param("p_list", _list)
rospy.set_param("p_dict", _dict)
```
#### 2.3.2 获取参数
##### C++
```cpp
// 使用NodeHandle
ros::NodeHandle nh;
nh.param(键, 默认值);    //存在，返回对应结果，否则返回默认值
nh.getParam(键, 存储结果的变量);    // 存在，返回true
nh.getParamCached(键, 存储结果的变量);    // 与getParam类似，提高了变量获取效率
nh.getParamNames(std::vector<std::string>);    // 获取所有的键，存储在vector变量中
nh.hasParam(键);    // 是否包含键
nh.searchParam(参数1, 参数2);    // 搜索键，参数1是被搜索的键，参数2是存储结果的的变量

// 使用param
ros::param::param(键, 默认值);
ros::param::get(键, 存储结果的变量);
ros::param::getCached(键, 存储结果的变量);
ros::param::getParamNames(std::vector<std::string>);
ros::param::has(键);
ros::param::search(参数1, 参数2);
```
##### python
```python
int_value = rospy.get_param("p_int",10000)
int_cached = rospy.get_param_cached("p_int")
names = rospy.get_param_names()
flag = rospy.has_param("p_int")
key = rospy.search_param("p_int")
```
#### 2.3.3 删除参数
##### C++
```cpp
ros::NodeHandle nh;
bool flag1 = nh.deleteParam("nh_int");

bool flag2 = ros::param::del("param_int");
```
##### python
```python
rospy.delete_param("p_int")
```