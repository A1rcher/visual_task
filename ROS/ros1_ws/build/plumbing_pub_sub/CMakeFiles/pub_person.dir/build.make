# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.26

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /home/archer/.local/lib/python3.8/site-packages/cmake/data/bin/cmake

# The command to remove a file.
RM = /home/archer/.local/lib/python3.8/site-packages/cmake/data/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/archer/visual_task/ROS/ros1_ws/src

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/archer/visual_task/ROS/ros1_ws/build

# Include any dependencies generated for this target.
include plumbing_pub_sub/CMakeFiles/pub_person.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include plumbing_pub_sub/CMakeFiles/pub_person.dir/compiler_depend.make

# Include the progress variables for this target.
include plumbing_pub_sub/CMakeFiles/pub_person.dir/progress.make

# Include the compile flags for this target's objects.
include plumbing_pub_sub/CMakeFiles/pub_person.dir/flags.make

plumbing_pub_sub/CMakeFiles/pub_person.dir/src/pub_person.cpp.o: plumbing_pub_sub/CMakeFiles/pub_person.dir/flags.make
plumbing_pub_sub/CMakeFiles/pub_person.dir/src/pub_person.cpp.o: /home/archer/visual_task/ROS/ros1_ws/src/plumbing_pub_sub/src/pub_person.cpp
plumbing_pub_sub/CMakeFiles/pub_person.dir/src/pub_person.cpp.o: plumbing_pub_sub/CMakeFiles/pub_person.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/archer/visual_task/ROS/ros1_ws/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object plumbing_pub_sub/CMakeFiles/pub_person.dir/src/pub_person.cpp.o"
	cd /home/archer/visual_task/ROS/ros1_ws/build/plumbing_pub_sub && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT plumbing_pub_sub/CMakeFiles/pub_person.dir/src/pub_person.cpp.o -MF CMakeFiles/pub_person.dir/src/pub_person.cpp.o.d -o CMakeFiles/pub_person.dir/src/pub_person.cpp.o -c /home/archer/visual_task/ROS/ros1_ws/src/plumbing_pub_sub/src/pub_person.cpp

plumbing_pub_sub/CMakeFiles/pub_person.dir/src/pub_person.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/pub_person.dir/src/pub_person.cpp.i"
	cd /home/archer/visual_task/ROS/ros1_ws/build/plumbing_pub_sub && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/archer/visual_task/ROS/ros1_ws/src/plumbing_pub_sub/src/pub_person.cpp > CMakeFiles/pub_person.dir/src/pub_person.cpp.i

plumbing_pub_sub/CMakeFiles/pub_person.dir/src/pub_person.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/pub_person.dir/src/pub_person.cpp.s"
	cd /home/archer/visual_task/ROS/ros1_ws/build/plumbing_pub_sub && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/archer/visual_task/ROS/ros1_ws/src/plumbing_pub_sub/src/pub_person.cpp -o CMakeFiles/pub_person.dir/src/pub_person.cpp.s

# Object files for target pub_person
pub_person_OBJECTS = \
"CMakeFiles/pub_person.dir/src/pub_person.cpp.o"

# External object files for target pub_person
pub_person_EXTERNAL_OBJECTS =

/home/archer/visual_task/ROS/ros1_ws/devel/lib/plumbing_pub_sub/pub_person: plumbing_pub_sub/CMakeFiles/pub_person.dir/src/pub_person.cpp.o
/home/archer/visual_task/ROS/ros1_ws/devel/lib/plumbing_pub_sub/pub_person: plumbing_pub_sub/CMakeFiles/pub_person.dir/build.make
/home/archer/visual_task/ROS/ros1_ws/devel/lib/plumbing_pub_sub/pub_person: /opt/ros/noetic/lib/libroscpp.so
/home/archer/visual_task/ROS/ros1_ws/devel/lib/plumbing_pub_sub/pub_person: /usr/lib/x86_64-linux-gnu/libpthread.so
/home/archer/visual_task/ROS/ros1_ws/devel/lib/plumbing_pub_sub/pub_person: /usr/lib/x86_64-linux-gnu/libboost_chrono.so.1.71.0
/home/archer/visual_task/ROS/ros1_ws/devel/lib/plumbing_pub_sub/pub_person: /usr/lib/x86_64-linux-gnu/libboost_filesystem.so.1.71.0
/home/archer/visual_task/ROS/ros1_ws/devel/lib/plumbing_pub_sub/pub_person: /opt/ros/noetic/lib/librosconsole.so
/home/archer/visual_task/ROS/ros1_ws/devel/lib/plumbing_pub_sub/pub_person: /opt/ros/noetic/lib/librosconsole_log4cxx.so
/home/archer/visual_task/ROS/ros1_ws/devel/lib/plumbing_pub_sub/pub_person: /opt/ros/noetic/lib/librosconsole_backend_interface.so
/home/archer/visual_task/ROS/ros1_ws/devel/lib/plumbing_pub_sub/pub_person: /usr/lib/x86_64-linux-gnu/liblog4cxx.so
/home/archer/visual_task/ROS/ros1_ws/devel/lib/plumbing_pub_sub/pub_person: /usr/lib/x86_64-linux-gnu/libboost_regex.so.1.71.0
/home/archer/visual_task/ROS/ros1_ws/devel/lib/plumbing_pub_sub/pub_person: /opt/ros/noetic/lib/libxmlrpcpp.so
/home/archer/visual_task/ROS/ros1_ws/devel/lib/plumbing_pub_sub/pub_person: /opt/ros/noetic/lib/libroscpp_serialization.so
/home/archer/visual_task/ROS/ros1_ws/devel/lib/plumbing_pub_sub/pub_person: /opt/ros/noetic/lib/librostime.so
/home/archer/visual_task/ROS/ros1_ws/devel/lib/plumbing_pub_sub/pub_person: /usr/lib/x86_64-linux-gnu/libboost_date_time.so.1.71.0
/home/archer/visual_task/ROS/ros1_ws/devel/lib/plumbing_pub_sub/pub_person: /opt/ros/noetic/lib/libcpp_common.so
/home/archer/visual_task/ROS/ros1_ws/devel/lib/plumbing_pub_sub/pub_person: /usr/lib/x86_64-linux-gnu/libboost_system.so.1.71.0
/home/archer/visual_task/ROS/ros1_ws/devel/lib/plumbing_pub_sub/pub_person: /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.71.0
/home/archer/visual_task/ROS/ros1_ws/devel/lib/plumbing_pub_sub/pub_person: /usr/lib/x86_64-linux-gnu/libconsole_bridge.so.0.4
/home/archer/visual_task/ROS/ros1_ws/devel/lib/plumbing_pub_sub/pub_person: plumbing_pub_sub/CMakeFiles/pub_person.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/archer/visual_task/ROS/ros1_ws/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable /home/archer/visual_task/ROS/ros1_ws/devel/lib/plumbing_pub_sub/pub_person"
	cd /home/archer/visual_task/ROS/ros1_ws/build/plumbing_pub_sub && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/pub_person.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
plumbing_pub_sub/CMakeFiles/pub_person.dir/build: /home/archer/visual_task/ROS/ros1_ws/devel/lib/plumbing_pub_sub/pub_person
.PHONY : plumbing_pub_sub/CMakeFiles/pub_person.dir/build

plumbing_pub_sub/CMakeFiles/pub_person.dir/clean:
	cd /home/archer/visual_task/ROS/ros1_ws/build/plumbing_pub_sub && $(CMAKE_COMMAND) -P CMakeFiles/pub_person.dir/cmake_clean.cmake
.PHONY : plumbing_pub_sub/CMakeFiles/pub_person.dir/clean

plumbing_pub_sub/CMakeFiles/pub_person.dir/depend:
	cd /home/archer/visual_task/ROS/ros1_ws/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/archer/visual_task/ROS/ros1_ws/src /home/archer/visual_task/ROS/ros1_ws/src/plumbing_pub_sub /home/archer/visual_task/ROS/ros1_ws/build /home/archer/visual_task/ROS/ros1_ws/build/plumbing_pub_sub /home/archer/visual_task/ROS/ros1_ws/build/plumbing_pub_sub/CMakeFiles/pub_person.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : plumbing_pub_sub/CMakeFiles/pub_person.dir/depend

