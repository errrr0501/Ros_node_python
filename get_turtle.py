#!/usr/bin/env python
import rospy
import random
import time
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose



def get_fb():
    rospy.init_node('get_turtle', anonymous=True)
    #pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=10)
    rospy.Subscriber("turtle1/pose",Pose ,callback) 
    rospy.spin()

def callback(data): 
    rospy.loginfo("position(%f,%f)", data.x, data.y) 
    rospy.loginfo("direction=%f", data.theta) 
if __name__ == '__main__':
	try:
		get_fb()
	except rospy.ROSInterruptException:
		pass
# not complete yet