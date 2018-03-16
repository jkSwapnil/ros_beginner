import sys
import rospy
import time
from std_msgs.msg import Int32

def talker():
	a=5
	pub=rospy.Publisher('chatter', Int32, queue_size=10)
	rospy.init_node('talker')
	while True:
	  pub.publish(a);
	  time.sleep(1)
talker()