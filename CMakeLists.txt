cmake_minimum_required(VERSION 3.6.9)
project(mypkg)

find_package(catkin REQUIRED COMPONENTS
  rospy
)

catkin_package(

)

include_directories(

  ${catkin_INCLUDE_DIRS}
)
