# Self-driving Turtlebots
## How to Run
### 1. Source environment vars
```
catkin_make
source /opt/ros/kinetic/setup.bash (Depending on where ROS is installed)
source devel/setup.bash
```

### 2. Commands to Run
#### With Gazebo
```
roslaunch turtlebot_gazebo turtlebot_world.launch
roslaunch turtlebot_gazebo amcl_demo.launch map_file:=[MAP_FULL_PATH]
roslaunch turtlebot_rviz_launchers view_navigation.launch --screen
```


#### Without Gazebo
```
roslaunch turtlebot_bringup minimal.launch
roslaunch turtlebot_rviz_launchers view_navigation.launch --screen
roslaunch turtlebot_navigation amcl_demo.launch map_file:=[MAP_FULL_PATH] 
```
e.g [MAP_FULL_PATH] - /home/osboxes/RoboticsProject/robotics_project_2019/src/map/my_map.yaml

### Run Naviagtion
```
python navigate.py --org " 0.234,1.34" --dest " -2.75,1.35" " -2.83,-1.62" " -4.78,-2.66"  " -6.76,-0.459" " -7.85,-2.71"

```
Note the spaces before ```-``` are important. 
### Common error
```
[view_navigation.launch] is neither a launch file in package [turtlebot_rviz_launchers] nor is [turtlebot_rviz_launchers] a launch file name
The traceback for the exception was written to the log file
```

http://wiki.ros.org/turtlebot_rviz_launchers

solution: 
sudo apt-get install ros-kinetic-turtlebot-rviz-launchers 


