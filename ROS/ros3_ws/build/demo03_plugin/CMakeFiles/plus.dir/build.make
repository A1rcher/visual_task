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
CMAKE_SOURCE_DIR = /home/archer/visual_task/ROS/ros3_ws/src

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/archer/visual_task/ROS/ros3_ws/build

# Include any dependencies generated for this target.
include demo03_plugin/CMakeFiles/plus.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include demo03_plugin/CMakeFiles/plus.dir/compiler_depend.make

# Include the progress variables for this target.
include demo03_plugin/CMakeFiles/plus.dir/progress.make

# Include the compile flags for this target's objects.
include demo03_plugin/CMakeFiles/plus.dir/flags.make

demo03_plugin/CMakeFiles/plus.dir/src/plus.cpp.o: demo03_plugin/CMakeFiles/plus.dir/flags.make
demo03_plugin/CMakeFiles/plus.dir/src/plus.cpp.o: /home/archer/visual_task/ROS/ros3_ws/src/demo03_plugin/src/plus.cpp
demo03_plugin/CMakeFiles/plus.dir/src/plus.cpp.o: demo03_plugin/CMakeFiles/plus.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/archer/visual_task/ROS/ros3_ws/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object demo03_plugin/CMakeFiles/plus.dir/src/plus.cpp.o"
	cd /home/archer/visual_task/ROS/ros3_ws/build/demo03_plugin && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT demo03_plugin/CMakeFiles/plus.dir/src/plus.cpp.o -MF CMakeFiles/plus.dir/src/plus.cpp.o.d -o CMakeFiles/plus.dir/src/plus.cpp.o -c /home/archer/visual_task/ROS/ros3_ws/src/demo03_plugin/src/plus.cpp

demo03_plugin/CMakeFiles/plus.dir/src/plus.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/plus.dir/src/plus.cpp.i"
	cd /home/archer/visual_task/ROS/ros3_ws/build/demo03_plugin && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/archer/visual_task/ROS/ros3_ws/src/demo03_plugin/src/plus.cpp > CMakeFiles/plus.dir/src/plus.cpp.i

demo03_plugin/CMakeFiles/plus.dir/src/plus.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/plus.dir/src/plus.cpp.s"
	cd /home/archer/visual_task/ROS/ros3_ws/build/demo03_plugin && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/archer/visual_task/ROS/ros3_ws/src/demo03_plugin/src/plus.cpp -o CMakeFiles/plus.dir/src/plus.cpp.s

# Object files for target plus
plus_OBJECTS = \
"CMakeFiles/plus.dir/src/plus.cpp.o"

# External object files for target plus
plus_EXTERNAL_OBJECTS =

/home/archer/visual_task/ROS/ros3_ws/devel/lib/libplus.so: demo03_plugin/CMakeFiles/plus.dir/src/plus.cpp.o
/home/archer/visual_task/ROS/ros3_ws/devel/lib/libplus.so: demo03_plugin/CMakeFiles/plus.dir/build.make
/home/archer/visual_task/ROS/ros3_ws/devel/lib/libplus.so: demo03_plugin/CMakeFiles/plus.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/archer/visual_task/ROS/ros3_ws/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX shared library /home/archer/visual_task/ROS/ros3_ws/devel/lib/libplus.so"
	cd /home/archer/visual_task/ROS/ros3_ws/build/demo03_plugin && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/plus.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
demo03_plugin/CMakeFiles/plus.dir/build: /home/archer/visual_task/ROS/ros3_ws/devel/lib/libplus.so
.PHONY : demo03_plugin/CMakeFiles/plus.dir/build

demo03_plugin/CMakeFiles/plus.dir/clean:
	cd /home/archer/visual_task/ROS/ros3_ws/build/demo03_plugin && $(CMAKE_COMMAND) -P CMakeFiles/plus.dir/cmake_clean.cmake
.PHONY : demo03_plugin/CMakeFiles/plus.dir/clean

demo03_plugin/CMakeFiles/plus.dir/depend:
	cd /home/archer/visual_task/ROS/ros3_ws/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/archer/visual_task/ROS/ros3_ws/src /home/archer/visual_task/ROS/ros3_ws/src/demo03_plugin /home/archer/visual_task/ROS/ros3_ws/build /home/archer/visual_task/ROS/ros3_ws/build/demo03_plugin /home/archer/visual_task/ROS/ros3_ws/build/demo03_plugin/CMakeFiles/plus.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : demo03_plugin/CMakeFiles/plus.dir/depend
