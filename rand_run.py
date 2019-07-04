#!/usr/bin/env python
import rospy
import random
from geometry_msgs.msg import Twist

def circle_walker():
    rospy.init_node('rand_run', anonymous=True)
    pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=10)
	#rospy.Subscriber("chatter", Twist , callback) 
    rate = rospy.Rate(2)
    while not rospy.is_shutdown():
        rand = random.uniform(0,1)
        cmd = Twist()
        cmd.linear.x = rand
        cmd.angular.z = rand*4 - 2
        rospy.loginfo("linear=%f", cmd.linear.x) 
        rospy.loginfo("angular=%f", cmd.angular.z) 
        pub.publish(cmd)
        rate.sleep()


if __name__ == '__main__':
	try:
		circle_walker()
	except rospy.ROSInterruptException:
		pass
	
	

