#!/usr/bin/env python
import rospy
from geometry_msgs.msg import PoseWithCovarianceStamped,PoseStamped
from tf.transformations import quaternion_from_euler
import argparse
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
import actionlib
from actionlib_msgs.msg import *
 
class NavController():
  	def initialize(self,x,y):
                rospy.init_node('navigate')
                pub = rospy.Publisher('/initialpose', PoseWithCovarianceStamped, queue_size = 1)
                rospy.sleep(2)
                checkpoint = PoseWithCovarianceStamped()
                checkpoint.header.frame_id = "base_link"
                checkpoint.pose.pose.position.x = x
                checkpoint.pose.pose.position.y = y
                checkpoint.pose.pose.position.z = 0

                [x,y,z,w]=quaternion_from_euler(0,0.0,0.0)
                checkpoint.pose.pose.orientation.x = x
                checkpoint.pose.pose.orientation.y = y
                checkpoint.pose.pose.orientation.z = -0.691
                checkpoint.pose.pose.orientation.w = 0.723

                # print checkpoint
#                pub.publish(checkpoint)
                rospy.sleep(10)

	def initialize(self,x,y):
		rospy.init_node('navigate')
		rospy.sleep(2)

	def move(self,goals):
		pub = rospy.Publisher('/move_base_simple/goal', PoseStamped, queue_size = 100)
		for g in goals:
			#we'll send a goal to the robot
			rospy.sleep(2)
			checkpoint = PoseStamped()
			checkpoint.header.frame_id = 'base_link'
			checkpoint.pose.position.x = g[0]
			checkpoint.pose.position.y = g[1]
			checkpoint.pose.position.z = g[2]
		
			[x,y,z,w]=quaternion_from_euler(0,0.0,0.0)
			checkpoint.pose.orientation.x = x
			checkpoint.pose.orientation.y = y
			
			checkpoint.pose.orientation.z = -0.691
			checkpoint.pose.orientation.w = 0.723
		
			print checkpoint
			pub.publish(checkpoint)

			if(len(goals) >  1):
				if(g == goals[-2]):
					rospy.sleep(8)
				else:
					rospy.sleep(11)
				
		
def main():
	parser = argparse.ArgumentParser(description='Turtlebot Navigation Controller.')
	parser.add_argument('--org','--list', help='delimited list input', type=str,nargs="*")
	parser.add_argument('--dest','--list2', help='delimited list input', type=str,nargs="*")
	args = parser.parse_args()

	if(args.org):
		args.org = args.org[0].split(',')
		iniX = float(args.org[0])
		iniY = float(args.org[1])
	else:
		iniX = -2
		iniY = -1

	if(args.dest):
		all_goals = []
		for dest in args.dest:
			coords = []
			goals = dest.split(',')
			# for g in goals:
			x = float(goals[0])
			y = float(goals[1])
			if(len(goals) > 2):
				z = goals[2]
			else:
				z = 0
			
			coords.append(x)
			coords.append(y)
			coords.append(z)
			all_goals.append(coords)
	else:
		all_goals = [[-2.12,0.372]]

	print(all_goals)
	# goals = [[-3.7,0.087],[-2.7,0.17]]

	nav = NavController()
	nav.initialize(iniX,iniY)
	nav.move(all_goals)
	
if __name__== "__main__":
  main()
