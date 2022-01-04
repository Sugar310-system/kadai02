

import rospy
from std_msgs.msg import Int64
rospy.init_node('count')
pub = rospy.Publisher('count_up' , Int64, queue_size=2)
rate = rospy.Rate(30)
n = 0
while not rospy.is_shutdown():
  n += 1
  pub.publish(n)
  rate.sleep()
