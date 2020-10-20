#! /usr/bin/env python

import rospy
import time
from geometry_msgs.msg import Twist, Pose
from sensor_msgs.msg import LaserScan
from maze_solver_position_tracker.msg import location

#Thought process revolves around moving the robot
#in short bursts. Using this can allow for the addition
#of x and y values to a custom message to calculate the
#position without using the pose function

def callback(msg): 

  #This will be the loop for movement. This should also update the distance
  #the robot has moved from its last position    
  
  #The first set of variables obtains the middle and end sensors from the 
  #environment surrounding the robot. This can determine wether or not there
  #is a wall in front of or on the sides of the robot  
  angles = msg.ranges
  forward = angles[360]
  right = angles[0]
  left = angles[719]
  print(forward)
  
  #Begin Movement of the robot 

  

  if (forward > .8):
    cmd_vel.linear.x = .2
  else:
    cmd_vel.linear.x = 0

    if (left > right):
        cmd_vel.angular.z = .25
        time.sleep(.15)
        cmd_vel.angular.z = 0
    else:
        cmd_vel.angular.z = -.25
        time.sleep(.15)
        cmd_vel.angular.z = 0

    if ((forward == infinity) and (left == infinity) and (right == infinity)):
      cmd_vel.linear.x = 0
      cmd_vel.angular.z = 0
        

  



angles = [] #Used to hold the values of the angles from the laser scanner 0-719
forward = 0.0 #Holds the value of the middle sensor 360
right = 0.0 #Holds the value of the right sensor 0
left = 0.0 #Holds the value of the left sensor 719
cmd_vel = Twist()
infinity = float('inf')


#This sets the initial velocity. The intent behind this is to keep the 
#Velocity relatively uniform to help with calculations
cmd_vel.linear.x = 0.0 

#This value will be used to determine how the robot turns. This robot
#experience drift when driving forward for long periods of time. Using a
#value of .01 in the angular z when moving in a linear direction can help
#to mitigate this drift
cmd_vel.angular.z = 0.00

#Creates a publisher aiding in moving the robot by publishing to cmd_vel
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)

#Reads from laserscan to get an idea of the robots environment
sub = rospy.Subscriber('/kobuki/laser/scan', LaserScan, callback)

rospy.init_node('Maze_Navigation_with_Orientaion_Prediction')

rate = rospy.Rate(5)

#rospy.spin()

while not rospy.is_shutdown(): 
  pub.publish(cmd_vel)
  rate.sleep()

