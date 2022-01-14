import rospy
from std_msgs.msg import Int32
def cb(message):
  global n
  n = message.data**3
if __name__=='__main__':   
rospy.init_node('cube')
sub = rospy.Subscriber('count_up' , Int32, cb)
rospy.spin()
