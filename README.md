# Artificial Intelligence Maritime Maneuver Indiana Collegiate Challenge (AIMM ICC)
This repository is the home to the source code and software documentation for the AIMM ICC course enviroment, which supports simulation of unmanned surface vehicles in marine environment. As requested, the AIMM boat is installed with package 4 sensors.
This is a forked repository from the vrx_classic repository. 
* This project provides arenas and tasks, as well as a description of the AIMM4 platform.


## Environment Information
This was built on VMware Workstation 17 pro.
- Operating System: Ubuntu 20.04 LTS
- ROS Version: ROS 1 Noetic

## Install Prereqs
1. Install ROS 1 Noetic (one-liner install)
```
wget -c https://raw.githubusercontent.com/qboticslabs/ros_install_noetic/master/ros_install_noetic.sh && chmod +x ./ros_install_noetic.sh && ./ros_install_noetic.sh
```
2. Upgrade the packages installed on your system
```
sudo apt update
sudo apt full-upgrade
```
3. Setup relevant repo and install dependencies
```
sudo apt install -y build-essential cmake cppcheck curl git gnupg libeigen3-dev libgles2-mesa-dev lsb-release pkg-config protobuf-compiler qtbase5-dev python3-dbg python3-pip python3-venv ruby software-properties-common wget 
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654
sudo sh -c 'echo "deb http://packages.osrfoundation.org/gazebo/ubuntu-stable `lsb_release -cs` main" > /etc/apt/sources.list.d/gazebo-stable.list'
wget http://packages.osrfoundation.org/gazebo.key -O - | sudo apt-key add -
sudo apt update
DIST=noetic
GAZ=gazebo11
sudo apt install ${GAZ} lib${GAZ}-dev ros-${DIST}-gazebo-plugins ros-${DIST}-gazebo-ros ros-${DIST}-hector-gazebo-plugins ros-${DIST}-joy ros-${DIST}-joy-teleop ros-${DIST}-key-teleop ros-${DIST}-robot-localization ros-${DIST}-robot-state-publisher ros-${DIST}-joint-state-publisher ros-${DIST}-rviz ros-${DIST}-ros-base ros-${DIST}-teleop-tools ros-${DIST}-teleop-twist-keyboard ros-${DIST}-velodyne-simulator ros-${DIST}-xacro ros-${DIST}-rqt ros-${DIST}-rqt-common-plugins
```

## Instructions to Setup
1. Create a new workspace:
```
mkdir -p ~/aimm_ws/src
cd ~/aimm_ws/src
```
2. Clone the repository into your workspace:
```
git clone git@github.com:likevin9911/RAITE_autonomy_boat.git
```
3. Build your workspace
```
cd ~/aimm_ws
catkin_make
```
4. In your home directory, source the setup file by placing this line of code into your .bashrc file and open new terminal.
```
source ~/aimm_ws/devel/setup.bash
```

## Customize
If you want to customize some of components like worlds, wave, wind speeds, models, etc. Take a look at the vrx wiki page: https://github.com/osrf/vrx/wiki/VRX-Classic-Home

## Run the simulation
1. After sourcing the simulation, lets try first launching the simulation. Gazebo should be launching the Syndey Regatta with a simple environemnt. Close out once it is running. 
```
roslaunch aimm_gazebo aimm.launch
```

2. Run the rviz
```
roslaunch lpv_gazebo rviz_aimm.launch
roslaunch aimm_gazebo usv_keydrive.launch
```
* If you want to move the boat via keyboard.

3. To run localization
```
roslaunch lpv_gazebo localization_example.launch
```


# Contributing
This project is under active development to support the AIMM teams. We are adding and improving things all the time. Our primary focus is to provide the fundamental aspects of the robot and environment, but we rely on the community to develop additional functionality around their particular use cases.

If you have any questions about these topics, or would like to work on other aspects, please contribute.  You can contact us directly (see below), submit an [issue](https://github.com/osrf/vrx/issues) or, better yet, submit a [pull request](https://github.com/osrf/vrx/pulls/)!

## Contributor Contacts

 * Kevin Li (He/Him/His) <kgli@mtu.edu>
 * Reyna Ryynanen (She/Her/Hers) <ttryynan@mtu.edu>


