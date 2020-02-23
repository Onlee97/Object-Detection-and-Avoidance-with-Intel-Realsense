cmake_minimum_required(VERSION 3.1)
# Enable C++11
project(capture)
find_package(OpenCV REQUIRED)
find_package(realsense2 REQUIRED)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED TRUE)
#SET(OpenCV_DIR /home/duy/opencv installation/installation/OpenCV-master/lib/cmake/opencv4)

add_executable(capture test.cpp)

target_link_libraries(capture ${OpenCV_LIBS} ${realsense2_LIBS})
