# Install script for directory: /home/archer/visual_task/ROS/ros3_ws/src/demo01_action

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/archer/visual_task/ROS/ros3_ws/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

# Set default install directory permissions.
if(NOT DEFINED CMAKE_OBJDUMP)
  set(CMAKE_OBJDUMP "/usr/bin/objdump")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/demo01_action/action" TYPE FILE FILES "/home/archer/visual_task/ROS/ros3_ws/src/demo01_action/action/addints.action")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/demo01_action/msg" TYPE FILE FILES
    "/home/archer/visual_task/ROS/ros3_ws/devel/share/demo01_action/msg/addintsAction.msg"
    "/home/archer/visual_task/ROS/ros3_ws/devel/share/demo01_action/msg/addintsActionGoal.msg"
    "/home/archer/visual_task/ROS/ros3_ws/devel/share/demo01_action/msg/addintsActionResult.msg"
    "/home/archer/visual_task/ROS/ros3_ws/devel/share/demo01_action/msg/addintsActionFeedback.msg"
    "/home/archer/visual_task/ROS/ros3_ws/devel/share/demo01_action/msg/addintsGoal.msg"
    "/home/archer/visual_task/ROS/ros3_ws/devel/share/demo01_action/msg/addintsResult.msg"
    "/home/archer/visual_task/ROS/ros3_ws/devel/share/demo01_action/msg/addintsFeedback.msg"
    )
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/demo01_action/cmake" TYPE FILE FILES "/home/archer/visual_task/ROS/ros3_ws/build/demo01_action/catkin_generated/installspace/demo01_action-msg-paths.cmake")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE DIRECTORY FILES "/home/archer/visual_task/ROS/ros3_ws/devel/include/demo01_action")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/roseus/ros" TYPE DIRECTORY FILES "/home/archer/visual_task/ROS/ros3_ws/devel/share/roseus/ros/demo01_action")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/common-lisp/ros" TYPE DIRECTORY FILES "/home/archer/visual_task/ROS/ros3_ws/devel/share/common-lisp/ros/demo01_action")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gennodejs/ros" TYPE DIRECTORY FILES "/home/archer/visual_task/ROS/ros3_ws/devel/share/gennodejs/ros/demo01_action")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  execute_process(COMMAND "/usr/bin/python3" -m compileall "/home/archer/visual_task/ROS/ros3_ws/devel/lib/python3/dist-packages/demo01_action")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python3/dist-packages" TYPE DIRECTORY FILES "/home/archer/visual_task/ROS/ros3_ws/devel/lib/python3/dist-packages/demo01_action")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/archer/visual_task/ROS/ros3_ws/build/demo01_action/catkin_generated/installspace/demo01_action.pc")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/demo01_action/cmake" TYPE FILE FILES "/home/archer/visual_task/ROS/ros3_ws/build/demo01_action/catkin_generated/installspace/demo01_action-msg-extras.cmake")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/demo01_action/cmake" TYPE FILE FILES
    "/home/archer/visual_task/ROS/ros3_ws/build/demo01_action/catkin_generated/installspace/demo01_actionConfig.cmake"
    "/home/archer/visual_task/ROS/ros3_ws/build/demo01_action/catkin_generated/installspace/demo01_actionConfig-version.cmake"
    )
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/demo01_action" TYPE FILE FILES "/home/archer/visual_task/ROS/ros3_ws/src/demo01_action/package.xml")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/demo01_action" TYPE PROGRAM FILES "/home/archer/visual_task/ROS/ros3_ws/build/demo01_action/catkin_generated/installspace/action01_server_p.py")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/demo01_action" TYPE PROGRAM FILES "/home/archer/visual_task/ROS/ros3_ws/build/demo01_action/catkin_generated/installspace/action02_client_p.py")
endif()

