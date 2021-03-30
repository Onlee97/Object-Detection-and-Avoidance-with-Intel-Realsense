# Object Avoidance and Detection for Blind People
## Objective
The goal of the project is to develop a device that allows visually impaired people navigate around without much dependence on other people or cumbersome tool. It also helps the blind get more insight into the surroundings and locate specific objects with ease. 

We're using [Intel RealSense depth camera D435](https://www.intelrealsense.com/depth-camera-d435/) for object avoidance and detection tasks. The camera sends images and depth details to [Jetson Nano](https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-nano/), a powerful microcomputer developed by Nvidia, for real-time processing. The camera and processor weigh approximately 50 grams in total, making it an extremly small and lightweight device that is comfortable to carry around. 

## Requirements
Hardware
- [Intel RealSense depth camera D435](https://www.intelrealsense.com/depth-camera-d435/)
- [NVIDIA Jetson Nano](https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-nano/)

Software 
- [Intel Realsense SDK 2.0](https://github.com/IntelRealSense/librealsense) (compute real-time depth images)
- [OpenCV 4.1.1 with extra modules](https://github.com/opencv/opencv) (object detection and image captioning)

## Features
There're 3 features:
- [Obstacle Avoidance](#obstacle-avoidance)
- [Find objects](#find-objects )
- [Describe the surrounding environment](#describe-the-surrounding-environment)

### Obstacle Avoidance
As the user moves, the device detects the obstacles in the person view and then signal the user about them by generate the "beep" sounds. The closer the object, the louder and faster the sound is. The system also keeps track of the velocity of the moving objects in order to avoid sudden collision. 

### Find objects 
"Where is my wallet?", "Where is my yellow hat?", "Where are my jeans?"
</br>This project is the answer to these questions. The user can ask questions to .., and the device will analyze the voice and give instructions where to find the objects through the hearing device.  

### Describe the surrounding environment
With a view to providing the users more insight into their surroundings, we implement image captioning feature to describe the front view of the user. 

## Installation
**Software**\
*Prerequisite*\
OpenCV.\
ROS.\
Intel Realsense.

**Flashing the Jetson OS**\
Using NVIDIA L4T32.3.1, JetPack 4.3\
Reference: https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-devkit

**Install OpenCV**\
The JetPack (Jetson OS) comes with a built in OpenCV (installed in /usr/ folder). However, this OpenCV doesn't come with CUDA support. In order to have a more customized OpenCV, we should built it from source. The building process can take about 2.5 hours

*Step 0:*
Supply Jetson with a 5V, 3A power supply. Based on my experience, using a 5V 1.5A may cause the jetson to crash in the building process, which led to me having to reflash the OS and start the process again.

*Step 1:*
Expand Swap memory. Jetson comes with only 4GB of RAM, and therefore can crash during the build process. Swap memory can be used as suppliment for RAM when needed.
```bash
$ sudo apt-get install zram-config
$ sudo gedit /usr/bin/init-zram-swapping
```
Replace this line
```bash
mem=$(((totalmem / 2 / ${NRDEVICES}) * 1024))
```
With this line
```bash
mem=$(((totalmem / ${NRDEVICES}) * 1024))
```
Reboot to apply change

*Step 2:*
```bash
$ git clone https://github.com/JetsonHacksNano/buildOpenCV
$ cd buildOpenCV
$ ./buildOpenCV.sh |& tee openCV_build.log
```
Reference: https://www.jetsonhacks.com/2019/11/22/opencv-4-cuda-on-jetson-nano/

**Install Intel Realsense SDK**\
The SDK are neccessary for the jetson to interact with the Depth Camera. The Depth Camera provide a 3D point cloud data which is very beneficial in multiple application. There are convienient way to install the SDK. However, if we want the library to support **Python**, then we have to build from source.

```bash
$ git clone https://github.com/IntelRealSense/librealsense.git
$ mkdir build
$ cd build
$ cmake ../ -DBUILD_PYTHON_BINDINGS:bool=true -DCMAKE_BUILD_TYPE=Release
$ sudo make uninstall && make clean && make -j4 && sudo make install
```
The library will be installed to */usr/local*, Therefore to use the pyrealsense2 library, run the following line to add to .bashrc file
```bash
$ export PYTHONPATH=$PYTHONPATH:/usr/local/lib
```
*Note 1: the realsense repo suggest to apply kernal patches to install the library, but since I don't want to make change to kernel, I skipped that part and the result is still working fine*\
*Note 2: the instructions from jetsonHacks is convienient, however after installing using his build script, the jetson automatically log off, so I ended up having to re-flash the OS and start over*\

Reference: 
https://github.com/IntelRealSense/librealsense/blob/master/doc/installation.md
https://github.com/IntelRealSense/librealsense/tree/master/wrappers/python




