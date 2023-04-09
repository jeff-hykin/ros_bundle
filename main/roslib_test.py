import rospy
from std_msgs.msg import String
pub = rospy.Publisher('/sb_cmd_state', String, queue_size=10)
rospy.init_node('send_sb', anonymous=True)
pub.publish(String("howdy"))