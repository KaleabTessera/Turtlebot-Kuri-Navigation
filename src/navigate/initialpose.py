#!/usr/bin/env python
# Adapted from http://www.theconstructsim.com/ros-qa-140-how-to-modify-a-robots-coordinates-when-it-arrives-at-a-checkpoint/ 
import rospy
from geometry_msgs.msg import PoseWithCovarianceStamped
from tf.transformations import quaternion_from_euler
 
rospy.init_node('init_pos')
pub = rospy.Publisher('/initialpose', PoseWithCovarianceStamped, queue_size = 10)
rospy.sleep(3)
checkpoint = PoseWithCovarianceStamped()
 
checkpoint.pose.pose.position.x = 0.0
checkpoint.pose.pose.position.y = 0.0
checkpoint.pose.pose.position.z = 0.0
 
[x,y,z,w]=quaternion_from_euler(0.0,0.0,0.0)
checkpoint.pose.pose.orientation.x = x
checkpoint.pose.pose.orientation.y = y
checkpoint.pose.pose.orientation.z = z
checkpoint.pose.pose.orientation.w = w
 
print checkpoint
pub.publish(checkpoint)