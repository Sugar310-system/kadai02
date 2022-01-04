import rospy
from std_msgs.msg import Int64

n = 0

def cb(message):
  global n
  n = message.data*2
  
rospy.init_node('twice')
sub = rospy.Subscriber('count_up' , Int64, cb)
pub = rospy.Publisher('twice',Int64, queue_size=2)
rate =rospy.Rate(30)
while not rospy.is_shutdown():
  pub.publish(n)
  rate.sleep()
