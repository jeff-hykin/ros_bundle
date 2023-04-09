import genpy.message
# from ctypes import *
from std_msgs.msg import Header

class Log(genpy.message.Message):
    _type = 'rosgraph_msgs/Log'
    _md5sum = 'acffd30cd6b6de30f120938c17c593fb'
    _has_header = True
    _full_text = "##\n## Severity level constants\n##\nbyte DEBUG=1 #debug level\nbyte INFO=2  #general level\nbyte WARN=4  #warning level\nbyte ERROR=8 #error level\nbyte FATAL=16 #fatal/critical level\n##\n## Fields\n##\nHeader header\nbyte level\nstring name # name of the node\nstring msg # message \nstring file # file the message came from\nstring function # function the message came from\nuint32 line # line the message came from\nstring[] topics # topic names that the node publishes\n\n================================================================================\nMSG: std_msgs/Header\n# Standard metadata for higher-level stamped data types.\n# This is generally used to communicate timestamped data \n# in a particular coordinate frame.\n# \n# sequence ID: consecutively increasing ID \nuint32 seq\n#Two-integer timestamp that is expressed as:\n# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')\n# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')\n# time-handling sugar is provided by the client library\ntime stamp\n#Frame this data is associated with\nstring frame_id\n"
    DEBUG=1
    INFO=2
    WARN=4
    ERROR=8
    FATAL=16
    __slots__ = [ 'header', 'level', 'name', 'msg', 'file', 'function', 'line', 'topics',  ]
    def _get_types(self):
        return ['std_msgs/Header', 'byte', 'string', 'string', 'string', 'string', 'uint32', 'string[]']

class TopicStatistics(genpy.message.Message):
    _type = 'rosgraph_msgs/TopicStatistics'
    _md5sum = '10152ed868c5097a5e2e4a89d7daa710'
    _has_header = False
    _full_text = '# name of the topic\nstring topic\n\n# node id of the publisher\nstring node_pub\n\n# node id of the subscriber\nstring node_sub\n\n# the statistics apply to this time window\ntime window_start\ntime window_stop\n\n# number of messages delivered during the window\nint32 delivered_msgs\n# numbers of messages dropped during the window\nint32 dropped_msgs\n\n# traffic during the window, in bytes\nint32 traffic\n\n# mean/stddev/max period between two messages\nduration period_mean\nduration period_stddev\nduration period_max\n\n# mean/stddev/max age of the message based on the\n# timestamp in the message header. In case the\n# message does not have a header, it will be 0.\nduration stamp_age_mean\nduration stamp_age_stddev\nduration stamp_age_max\n'
    __slots__ = ['topic', 'node_pub', 'node_sub', 'window_start', 'window_stop', 'delivered_msgs', 'dropped_msgs', 'traffic', 'period_mean', 'period_stddev', 'period_max', 'stamp_age_mean', 'stamp_age_stddev', 'stamp_age_max']
    def _get_types(self):
        return ['string', 'string', 'string', 'time', 'time', 'int32', 'int32', 'int32', 'duration', 'duration', 'duration', 'duration', 'duration', 'duration']

class Clock(genpy.message.Message):
    _type = 'rosgraph_msgs/Clock'
    _md5sum = 'a9c97c1d230cfc112e270351a944ee47'
    _has_header = False
    _full_text = '# roslib/Clock is used for publishing simulated time in ROS. \n# This message simply communicates the current time.\n# For more information, see http://www.ros.org/wiki/Clock\ntime clock\n'
    __slots__ = ['clock']
    def _get_types(self):
        return ['time']

# ##
# ## Severity level constants
# ##
# ctypes.c_uint8 DEBUG=1 #debug level
# ctypes.c_uint8 INFO=2  #general level
# ctypes.c_uint8 WARN=4  #warning level
# ctypes.c_uint8 ERROR=8 #error level
# ctypes.c_uint8 FATAL=16 #fatal/critical level
# ##
# ## Fields
# ##
# Header header
# byte level
# string name # name of the node
# string msg # message 
# string file # file the message came from
# string function # function the message came from
# uint32 line # line the message came from
# string[] topics # topic names that the node publishes
