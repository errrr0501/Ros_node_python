#!/usr/bin/env python
import rospy
from std_msgs.msg import String
    
def talker():
    rospy.init_node('talker', anonymous=True)
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.Subscriber("chatter", String, callback) 
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        hello_str = "hello world %s" % rospy.get_time()
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()
   
def callback(msg): 
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", msg.data) 


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass