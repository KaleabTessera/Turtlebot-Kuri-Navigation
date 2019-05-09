# Self-driving Turtlebots
## How to Run
### 1. Source environment vars
```
source /opt/ros/kinetic/setup.bash (Depending on where ROS is installed)
source devel/setup.bash
```

### 2. Commands to Run
#### Without Gazebo
roslaunch turtlebot_gazebo turtlebot_world.launch
roslaunch turtlebot_rviz_launchers view_navigation.launch --screen
roslaunch turtlebot_navigation amcl_demo.launch map_file:=/home/osboxes/RoboticsProject/robotics_project_2019/src/map/my_map.yaml


#### With Gazebo
```
roslaunch turtlebot_gazebo turtlebot_world.launch
roslaunch turtlebot_gazebo amcl_demo.launch map_file:=/home/osboxes/RoboticsProject/robotics_project_2019/src/map/my_map.yaml
roslaunch turtlebot_rviz_launchers view_navigation.launch --screen
```



