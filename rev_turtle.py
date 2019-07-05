#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist



def ran_turtle():
    rospy.init_node('rev_turtle', anonymous=True)
    rospy.Subscriber("/turtle1/cmd_vel",Twist ,rev)
    rospy.spin() 
    #rospy.loginfo("linear=%f", rev_cmd.linear.x) 
    #rospy.loginfo("angular=%f", rev_cmd.angular.z) 
   


def rev(data): 
    global rev_cmd
    rev_cmd = Twist()
    rospy.loginfo("position=%f", data.linear.x) 
    rospy.loginfo("direction=%f", data.angular.z) 
    rev_cmd.linear.x = -data.linear.x
    rev_cmd.angular.z = -data.angular.z
    pub = rospy.Publisher('/turtle1/rev_cmd', Twist, queue_size=10)
    pub.publish(rev_cmd)
if __name__ == '__main__':
	try:
		ran_turtle()
	except rospy.ROSInterruptException:
		pass
# not complete yet