cmake_minimum_required(VERSION 3.1.0)

project(mode1)

# Find librealsense2 installed package
find_package(realsense2 REQUIRED)
find_package(OpenCV REQUIRED)
find_package(Curses REQUIRED)

include_directories(${CURSES_INCLUDE_DIRS})

# Enable C++11
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED TRUE)

# Add the application sources to the target
add_executable(${PROJECT_NAME} rs-hello-realsense.cpp)

# Link librealsense2 to the target;
target_link_libraries(${PROJECT_NAME} ${realsense2_LIBRARY} 
	${OpenCV_LIBS}
	${CURSES_LIBRARIES}
	)


