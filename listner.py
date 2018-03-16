import sys
import rospy
import time
from std_msgs.msg import Int32

def callback(data):
	print("got DATA")

def listner():
	rospy.init_node('listner')
	rospy.Subscriber('chatter', Int32, callback)
	while True:
	  print("waiting for DATA")
	  time.sleep(1)


listner()