#!/usr/bin/env python3
import rospy
import math

from std_msgs.msg import Int32
def cb(message):
  global n
  n = message.data**3*math.pi*4/3
if __name__=='__main__':   
rospy.init_node('sphere')
sub = rospy.Subscriber('count_up' , Int32, cb)
rospy.spin()
