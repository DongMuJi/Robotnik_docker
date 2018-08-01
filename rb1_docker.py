#!/usr/bin/env python
import rospy
import actionlib
from robotnik_navigation_msgs.msg import DockAction, DockGoal

# Create a ROS node
rospy.init_node("dock_the_robot")

# Create an action client
client = actionlib.SimpleActionClient("/docker", DockAction)
client.wait_for_server()

# Create and send a goal
goal = DockGoal()
goal.dock_frame = "docking_station_contact"
goal.robot_dock_frame = "base_docking_contact"
goal.dock_offset.x = 0.0
goal.dock_offset.y = 0.0
goal.dock_offset.theta = 0.0
goal.maximum_velocity.x = 0.0
goal.maximum_velocity.y = 0.0
goal.maximum_velocity.z = 0.0

client.send_goal(goal)
client.wait_for_result()
print "------Finish Docking------"
print client.get_result()
