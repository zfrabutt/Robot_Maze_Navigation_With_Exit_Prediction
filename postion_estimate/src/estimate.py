#! /usr/bin/env python

import rospy
from nav_msgs.msg import Odometry
from postion_estimate.msg import location
import math

x_out = 0.0
y_out = 0.0

def callback(msg):
    global x_out
    global y_out

    x = msg.pose.pose.position.x
    y = msg.pose.pose.position.y
    
    x2 = x - x_out
    y2 = y - y_out

    x_out = x2 + x_out
    y_out = y2 + y_out

    currentLocation.x = x_out
    currentLocation.y = y_out

    print currentLocation

currentLocation = location()
currentLocation.x = 0
currentLocation.y = 0

rospy.init_node('check_odometry')
odom_sub = rospy.Subscriber('/odom', Odometry, callback)
rospy.spin()