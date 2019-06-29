#!/usr/bin/env python
import rospy
from geometry_msgs.msg import PoseWithCovarianceStamped
from tf.transformations import quaternion_from_euler
import argparse
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
import actionlib
from actionlib_msgs.msg import *
 
class NavController():

	def initialize(self,x,y):
		rospy.init_node('navigate')
		pub = rospy.Publisher('/initialpose', PoseWithCovarianceStamped, queue_size = 10)
		rospy.sleep(2)
		checkpoint = PoseWithCovarianceStamped()
		checkpoint.header.frame_id = "map"
		checkpoint.pose.pose.position.x = x
		checkpoint.pose.pose.position.y = y
		checkpoint.pose.pose.position.z = 0.349
		
		[x,y,z,w]=quaternion_from_euler(0,0.0,0.0)
		checkpoint.pose.pose.orientation.x = x
		checkpoint.pose.pose.orientation.y = y
		checkpoint.pose.pose.orientation.z = z
		checkpoint.pose.pose.orientation.w = w
		
		# print checkpoint
		pub.publish(checkpoint)
		rospy.sleep(10)

	def move(self,goals):
		#tell the action client that we want to spin a thread by default
		self.move_base = actionlib.SimpleActionClient("move_base", MoveBaseAction)
		rospy.loginfo("wait for the action server to come up")
		#allow up to 5 seconds for the action server to come up
		self.move_base.wait_for_server(rospy.Duration(2))
		for g in goals:
			#we'll send a goal to the robot
			goal = MoveBaseGoal()
			goal.target_pose.header.frame_id = 'map'
			goal.target_pose.header.stamp = rospy.Time.now()
			goal.target_pose.pose.position.x = g[0]
			goal.target_pose.pose.position.y = g[1]
			goal.target_pose.pose.position.z = 0


			[x,y,z,w]=quaternion_from_euler(0,0.0,0.0)
			goal.target_pose.pose.orientation.x = x
			goal.target_pose.pose.orientation.y = y
			goal.target_pose.pose.orientation.z = z
			goal.target_pose.pose.orientation.w = w

			#start moving
			self.move_base.send_goal(goal)
			print("goal:{}".format(g))

			#allow TurtleBot up to 30 seconds to complete task
			success = self.move_base.wait_for_result(rospy.Duration(30)) 



			if not success:
				self.move_base.cancel_goal()
				rospy.loginfo("What happenned bra")
			else:
				# We made it!
				state = self.move_base.get_state()
				if state == GoalStatus.SUCCEEDED:
					rospy.loginfo("Done moving")
		
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
			print dest
			coords = []
			goals = dest.split(',')
			print goals
			# for g in goals:
			x = float(goals[0])
			y = float(goals[1])
			coords.append(x)
			coords.append(y)
			all_goals.append(coords)
	else:
		all_goals = [[-3.7,0.087]]

	print(all_goals)
	# goals = [[-3.7,0.087],[-2.7,0.17]]

	nav = NavController()
	nav.initialize(iniX,iniY)
	nav.move(all_goals)
	
if __name__== "__main__":
  main()
