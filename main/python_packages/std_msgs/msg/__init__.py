import genpy.message

# def compute(message_class):
#     print(f'''
# class {message_class.__name__}(genpy.message.Message):
#     _type = {repr(message_class._type)}
#     _md5sum = {repr(message_class._md5sum)}
#     _has_header = {repr(message_class._has_header)}
#     _full_text = {repr(message_class._full_text)}
#     __slots__ = {repr(message_class.__slots__)}
#     def _get_types(self):
#         return {repr(message_class()._get_types())}
# ''')
# 
# for message_type in [
#     std_msgs.msg.Empty,
#     std_msgs.msg.Bool,
#     std_msgs.msg.Byte,
#     std_msgs.msg.ByteMultiArray,
#     std_msgs.msg.Char,
#     std_msgs.msg.ColorRGBA,
#     std_msgs.msg.String,
#     std_msgs.msg.Time,
#     std_msgs.msg.Duration,
#     std_msgs.msg.UInt8,
#     std_msgs.msg.UInt16,
#     std_msgs.msg.UInt32,
#     std_msgs.msg.UInt64,
#     std_msgs.msg.Float32,
#     std_msgs.msg.Float64,
#     std_msgs.msg.Header,
#     std_msgs.msg.Int8,
#     std_msgs.msg.Int16,
#     std_msgs.msg.Int32,
#     std_msgs.msg.Int64,
#     std_msgs.msg.MultiArrayDimension,
#     std_msgs.msg.MultiArrayLayout,
#     std_msgs.msg.Int8MultiArray,
#     std_msgs.msg.Int16MultiArray,
#     std_msgs.msg.Int32MultiArray,
#     std_msgs.msg.Int64MultiArray,
#     std_msgs.msg.Float32MultiArray,
#     std_msgs.msg.Float64MultiArray,
#     std_msgs.msg.UInt8MultiArray,
#     std_msgs.msg.UInt16MultiArray,
#     std_msgs.msg.UInt32MultiArray,
#     std_msgs.msg.UInt64MultiArray,
# ]:
#     compute(message_type)

class Empty(genpy.message.Message):
    _type = 'std_msgs/Empty'
    _md5sum = 'd41d8cd98f00b204e9800998ecf8427e'
    _has_header = False
    _full_text = ''
    __slots__ = []
    def _get_types(self):
        return []


class Bool(genpy.message.Message):
    _type = 'std_msgs/Bool'
    _md5sum = '8b94c1b53db61fb6aed406028ad6332a'
    _has_header = False
    _full_text = 'bool data'
    __slots__ = ['data']
    def _get_types(self):
        return ['bool']


class Byte(genpy.message.Message):
    _type = 'std_msgs/Byte'
    _md5sum = 'ad736a2e8818154c487bb80fe42ce43b'
    _has_header = False
    _full_text = 'byte data\n'
    __slots__ = ['data']
    def _get_types(self):
        return ['byte']


class ByteMultiArray(genpy.message.Message):
    _type = 'std_msgs/ByteMultiArray'
    _md5sum = '70ea476cbcfd65ac2f68f3cda1e891fe'
    _has_header = False
    _full_text = '# Please look at the MultiArrayLayout message definition for\n# documentation on all multiarrays.\n\nMultiArrayLayout  layout        # specification of data layout\nbyte[]            data          # array of data\n\n\n================================================================================\nMSG: std_msgs/MultiArrayLayout\n# The multiarray declares a generic multi-dimensional array of a\n# particular data type.  Dimensions are ordered from outer most\n# to inner most.\n\nMultiArrayDimension[] dim # Array of dimension properties\nuint32 data_offset        # padding elements at front of data\n\n# Accessors should ALWAYS be written in terms of dimension stride\n# and specified outer-most dimension first.\n# \n# multiarray(i,j,k) = data[data_offset + dim_stride[1]*i + dim_stride[2]*j + k]\n#\n# A standard, 3-channel 640x480 image with interleaved color channels\n# would be specified as:\n#\n# dim[0].label  = "height"\n# dim[0].size   = 480\n# dim[0].stride = 3*640*480 = 921600  (note dim[0] stride is just size of image)\n# dim[1].label  = "width"\n# dim[1].size   = 640\n# dim[1].stride = 3*640 = 1920\n# dim[2].label  = "channel"\n# dim[2].size   = 3\n# dim[2].stride = 3\n#\n# multiarray(i,j,k) refers to the ith row, jth column, and kth channel.\n\n================================================================================\nMSG: std_msgs/MultiArrayDimension\nstring label   # label of given dimension\nuint32 size    # size of given dimension (in type units)\nuint32 stride  # stride of given dimension'
    __slots__ = ['layout', 'data']
    def _get_types(self):
        return ['std_msgs/MultiArrayLayout', 'byte[]']


class Char(genpy.message.Message):
    _type = 'std_msgs/Char'
    _md5sum = '1bf77f25acecdedba0e224b162199717'
    _has_header = False
    _full_text = 'char data'
    __slots__ = ['data']
    def _get_types(self):
        return ['char']


class ColorRGBA(genpy.message.Message):
    _type = 'std_msgs/ColorRGBA'
    _md5sum = 'a29a96539573343b1310c73607334b00'
    _has_header = False
    _full_text = 'float32 r\nfloat32 g\nfloat32 b\nfloat32 a\n'
    __slots__ = ['r', 'g', 'b', 'a']
    def _get_types(self):
        return ['float32', 'float32', 'float32', 'float32']


class String(genpy.message.Message):
    _type = 'std_msgs/String'
    _md5sum = '992ce8a1687cec8c8bd883ec73ca41d1'
    _has_header = False
    _full_text = 'string data\n'
    __slots__ = ['data']
    def _get_types(self):
        return ['string']


class Time(genpy.message.Message):
    _type = 'std_msgs/Time'
    _md5sum = 'cd7166c74c552c311fbcc2fe5a7bc289'
    _has_header = False
    _full_text = 'time data\n'
    __slots__ = ['data']
    def _get_types(self):
        return ['time']


class Duration(genpy.message.Message):
    _type = 'std_msgs/Duration'
    _md5sum = '3e286caf4241d664e55f3ad380e2ae46'
    _has_header = False
    _full_text = 'duration data\n'
    __slots__ = ['data']
    def _get_types(self):
        return ['duration']


class UInt8(genpy.message.Message):
    _type = 'std_msgs/UInt8'
    _md5sum = '7c8164229e7d2c17eb95e9231617fdee'
    _has_header = False
    _full_text = 'uint8 data\n'
    __slots__ = ['data']
    def _get_types(self):
        return ['uint8']


class UInt16(genpy.message.Message):
    _type = 'std_msgs/UInt16'
    _md5sum = '1df79edf208b629fe6b81923a544552d'
    _has_header = False
    _full_text = 'uint16 data\n'
    __slots__ = ['data']
    def _get_types(self):
        return ['uint16']


class UInt32(genpy.message.Message):
    _type = 'std_msgs/UInt32'
    _md5sum = '304a39449588c7f8ce2df6e8001c5fce'
    _has_header = False
    _full_text = 'uint32 data'
    __slots__ = ['data']
    def _get_types(self):
        return ['uint32']


class UInt64(genpy.message.Message):
    _type = 'std_msgs/UInt64'
    _md5sum = '1b2a79973e8bf53d7b53acb71299cb57'
    _has_header = False
    _full_text = 'uint64 data'
    __slots__ = ['data']
    def _get_types(self):
        return ['uint64']


class Float32(genpy.message.Message):
    _type = 'std_msgs/Float32'
    _md5sum = '73fcbf46b49191e672908e50842a83d4'
    _has_header = False
    _full_text = 'float32 data'
    __slots__ = ['data']
    def _get_types(self):
        return ['float32']


class Float64(genpy.message.Message):
    _type = 'std_msgs/Float64'
    _md5sum = 'fdb28210bfa9d7c91146260178d9a584'
    _has_header = False
    _full_text = 'float64 data'
    __slots__ = ['data']
    def _get_types(self):
        return ['float64']


class Header(genpy.message.Message):
    _type = 'std_msgs/Header'
    _md5sum = '2176decaecbce78abc3b96ef049fabed'
    _has_header = False
    _full_text = "# Standard metadata for higher-level stamped data types.\n# This is generally used to communicate timestamped data \n# in a particular coordinate frame.\n# \n# sequence ID: consecutively increasing ID \nuint32 seq\n#Two-integer timestamp that is expressed as:\n# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')\n# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')\n# time-handling sugar is provided by the client library\ntime stamp\n#Frame this data is associated with\nstring frame_id\n"
    __slots__ = ['seq', 'stamp', 'frame_id']
    def _get_types(self):
        return ['uint32', 'time', 'string']


class Int8(genpy.message.Message):
    _type = 'std_msgs/Int8'
    _md5sum = '27ffa0c9c4b8fb8492252bcad9e5c57b'
    _has_header = False
    _full_text = 'int8 data\n'
    __slots__ = ['data']
    def _get_types(self):
        return ['int8']


class Int16(genpy.message.Message):
    _type = 'std_msgs/Int16'
    _md5sum = '8524586e34fbd7cb1c08c5f5f1ca0e57'
    _has_header = False
    _full_text = 'int16 data\n'
    __slots__ = ['data']
    def _get_types(self):
        return ['int16']


class Int32(genpy.message.Message):
    _type = 'std_msgs/Int32'
    _md5sum = 'da5909fbe378aeaf85e547e830cc1bb7'
    _has_header = False
    _full_text = 'int32 data'
    __slots__ = ['data']
    def _get_types(self):
        return ['int32']


class Int64(genpy.message.Message):
    _type = 'std_msgs/Int64'
    _md5sum = '34add168574510e6e17f5d23ecc077ef'
    _has_header = False
    _full_text = 'int64 data'
    __slots__ = ['data']
    def _get_types(self):
        return ['int64']


class MultiArrayDimension(genpy.message.Message):
    _type = 'std_msgs/MultiArrayDimension'
    _md5sum = '4cd0c83a8683deae40ecdac60e53bfa8'
    _has_header = False
    _full_text = 'string label   # label of given dimension\nuint32 size    # size of given dimension (in type units)\nuint32 stride  # stride of given dimension'
    __slots__ = ['label', 'size', 'stride']
    def _get_types(self):
        return ['string', 'uint32', 'uint32']


class MultiArrayLayout(genpy.message.Message):
    _type = 'std_msgs/MultiArrayLayout'
    _md5sum = '0fed2a11c13e11c5571b4e2a995a91a3'
    _has_header = False
    _full_text = '# The multiarray declares a generic multi-dimensional array of a\n# particular data type.  Dimensions are ordered from outer most\n# to inner most.\n\nMultiArrayDimension[] dim # Array of dimension properties\nuint32 data_offset        # padding elements at front of data\n\n# Accessors should ALWAYS be written in terms of dimension stride\n# and specified outer-most dimension first.\n# \n# multiarray(i,j,k) = data[data_offset + dim_stride[1]*i + dim_stride[2]*j + k]\n#\n# A standard, 3-channel 640x480 image with interleaved color channels\n# would be specified as:\n#\n# dim[0].label  = "height"\n# dim[0].size   = 480\n# dim[0].stride = 3*640*480 = 921600  (note dim[0] stride is just size of image)\n# dim[1].label  = "width"\n# dim[1].size   = 640\n# dim[1].stride = 3*640 = 1920\n# dim[2].label  = "channel"\n# dim[2].size   = 3\n# dim[2].stride = 3\n#\n# multiarray(i,j,k) refers to the ith row, jth column, and kth channel.\n\n================================================================================\nMSG: std_msgs/MultiArrayDimension\nstring label   # label of given dimension\nuint32 size    # size of given dimension (in type units)\nuint32 stride  # stride of given dimension'
    __slots__ = ['dim', 'data_offset']
    def _get_types(self):
        return ['std_msgs/MultiArrayDimension[]', 'uint32']


class Int8MultiArray(genpy.message.Message):
    _type = 'std_msgs/Int8MultiArray'
    _md5sum = 'd7c1af35a1b4781bbe79e03dd94b7c13'
    _has_header = False
    _full_text = '# Please look at the MultiArrayLayout message definition for\n# documentation on all multiarrays.\n\nMultiArrayLayout  layout        # specification of data layout\nint8[]            data          # array of data\n\n\n================================================================================\nMSG: std_msgs/MultiArrayLayout\n# The multiarray declares a generic multi-dimensional array of a\n# particular data type.  Dimensions are ordered from outer most\n# to inner most.\n\nMultiArrayDimension[] dim # Array of dimension properties\nuint32 data_offset        # padding elements at front of data\n\n# Accessors should ALWAYS be written in terms of dimension stride\n# and specified outer-most dimension first.\n# \n# multiarray(i,j,k) = data[data_offset + dim_stride[1]*i + dim_stride[2]*j + k]\n#\n# A standard, 3-channel 640x480 image with interleaved color channels\n# would be specified as:\n#\n# dim[0].label  = "height"\n# dim[0].size   = 480\n# dim[0].stride = 3*640*480 = 921600  (note dim[0] stride is just size of image)\n# dim[1].label  = "width"\n# dim[1].size   = 640\n# dim[1].stride = 3*640 = 1920\n# dim[2].label  = "channel"\n# dim[2].size   = 3\n# dim[2].stride = 3\n#\n# multiarray(i,j,k) refers to the ith row, jth column, and kth channel.\n\n================================================================================\nMSG: std_msgs/MultiArrayDimension\nstring label   # label of given dimension\nuint32 size    # size of given dimension (in type units)\nuint32 stride  # stride of given dimension'
    __slots__ = ['layout', 'data']
    def _get_types(self):
        return ['std_msgs/MultiArrayLayout', 'int8[]']


class Int16MultiArray(genpy.message.Message):
    _type = 'std_msgs/Int16MultiArray'
    _md5sum = 'd9338d7f523fcb692fae9d0a0e9f067c'
    _has_header = False
    _full_text = '# Please look at the MultiArrayLayout message definition for\n# documentation on all multiarrays.\n\nMultiArrayLayout  layout        # specification of data layout\nint16[]           data          # array of data\n\n\n================================================================================\nMSG: std_msgs/MultiArrayLayout\n# The multiarray declares a generic multi-dimensional array of a\n# particular data type.  Dimensions are ordered from outer most\n# to inner most.\n\nMultiArrayDimension[] dim # Array of dimension properties\nuint32 data_offset        # padding elements at front of data\n\n# Accessors should ALWAYS be written in terms of dimension stride\n# and specified outer-most dimension first.\n# \n# multiarray(i,j,k) = data[data_offset + dim_stride[1]*i + dim_stride[2]*j + k]\n#\n# A standard, 3-channel 640x480 image with interleaved color channels\n# would be specified as:\n#\n# dim[0].label  = "height"\n# dim[0].size   = 480\n# dim[0].stride = 3*640*480 = 921600  (note dim[0] stride is just size of image)\n# dim[1].label  = "width"\n# dim[1].size   = 640\n# dim[1].stride = 3*640 = 1920\n# dim[2].label  = "channel"\n# dim[2].size   = 3\n# dim[2].stride = 3\n#\n# multiarray(i,j,k) refers to the ith row, jth column, and kth channel.\n\n================================================================================\nMSG: std_msgs/MultiArrayDimension\nstring label   # label of given dimension\nuint32 size    # size of given dimension (in type units)\nuint32 stride  # stride of given dimension'
    __slots__ = ['layout', 'data']
    def _get_types(self):
        return ['std_msgs/MultiArrayLayout', 'int16[]']


class Int32MultiArray(genpy.message.Message):
    _type = 'std_msgs/Int32MultiArray'
    _md5sum = '1d99f79f8b325b44fee908053e9c945b'
    _has_header = False
    _full_text = '# Please look at the MultiArrayLayout message definition for\n# documentation on all multiarrays.\n\nMultiArrayLayout  layout        # specification of data layout\nint32[]           data          # array of data\n\n\n================================================================================\nMSG: std_msgs/MultiArrayLayout\n# The multiarray declares a generic multi-dimensional array of a\n# particular data type.  Dimensions are ordered from outer most\n# to inner most.\n\nMultiArrayDimension[] dim # Array of dimension properties\nuint32 data_offset        # padding elements at front of data\n\n# Accessors should ALWAYS be written in terms of dimension stride\n# and specified outer-most dimension first.\n# \n# multiarray(i,j,k) = data[data_offset + dim_stride[1]*i + dim_stride[2]*j + k]\n#\n# A standard, 3-channel 640x480 image with interleaved color channels\n# would be specified as:\n#\n# dim[0].label  = "height"\n# dim[0].size   = 480\n# dim[0].stride = 3*640*480 = 921600  (note dim[0] stride is just size of image)\n# dim[1].label  = "width"\n# dim[1].size   = 640\n# dim[1].stride = 3*640 = 1920\n# dim[2].label  = "channel"\n# dim[2].size   = 3\n# dim[2].stride = 3\n#\n# multiarray(i,j,k) refers to the ith row, jth column, and kth channel.\n\n================================================================================\nMSG: std_msgs/MultiArrayDimension\nstring label   # label of given dimension\nuint32 size    # size of given dimension (in type units)\nuint32 stride  # stride of given dimension'
    __slots__ = ['layout', 'data']
    def _get_types(self):
        return ['std_msgs/MultiArrayLayout', 'int32[]']


class Int64MultiArray(genpy.message.Message):
    _type = 'std_msgs/Int64MultiArray'
    _md5sum = '54865aa6c65be0448113a2afc6a49270'
    _has_header = False
    _full_text = '# Please look at the MultiArrayLayout message definition for\n# documentation on all multiarrays.\n\nMultiArrayLayout  layout        # specification of data layout\nint64[]           data          # array of data\n\n\n================================================================================\nMSG: std_msgs/MultiArrayLayout\n# The multiarray declares a generic multi-dimensional array of a\n# particular data type.  Dimensions are ordered from outer most\n# to inner most.\n\nMultiArrayDimension[] dim # Array of dimension properties\nuint32 data_offset        # padding elements at front of data\n\n# Accessors should ALWAYS be written in terms of dimension stride\n# and specified outer-most dimension first.\n# \n# multiarray(i,j,k) = data[data_offset + dim_stride[1]*i + dim_stride[2]*j + k]\n#\n# A standard, 3-channel 640x480 image with interleaved color channels\n# would be specified as:\n#\n# dim[0].label  = "height"\n# dim[0].size   = 480\n# dim[0].stride = 3*640*480 = 921600  (note dim[0] stride is just size of image)\n# dim[1].label  = "width"\n# dim[1].size   = 640\n# dim[1].stride = 3*640 = 1920\n# dim[2].label  = "channel"\n# dim[2].size   = 3\n# dim[2].stride = 3\n#\n# multiarray(i,j,k) refers to the ith row, jth column, and kth channel.\n\n================================================================================\nMSG: std_msgs/MultiArrayDimension\nstring label   # label of given dimension\nuint32 size    # size of given dimension (in type units)\nuint32 stride  # stride of given dimension'
    __slots__ = ['layout', 'data']
    def _get_types(self):
        return ['std_msgs/MultiArrayLayout', 'int64[]']


class Float32MultiArray(genpy.message.Message):
    _type = 'std_msgs/Float32MultiArray'
    _md5sum = '6a40e0ffa6a17a503ac3f8616991b1f6'
    _has_header = False
    _full_text = '# Please look at the MultiArrayLayout message definition for\n# documentation on all multiarrays.\n\nMultiArrayLayout  layout        # specification of data layout\nfloat32[]         data          # array of data\n\n\n================================================================================\nMSG: std_msgs/MultiArrayLayout\n# The multiarray declares a generic multi-dimensional array of a\n# particular data type.  Dimensions are ordered from outer most\n# to inner most.\n\nMultiArrayDimension[] dim # Array of dimension properties\nuint32 data_offset        # padding elements at front of data\n\n# Accessors should ALWAYS be written in terms of dimension stride\n# and specified outer-most dimension first.\n# \n# multiarray(i,j,k) = data[data_offset + dim_stride[1]*i + dim_stride[2]*j + k]\n#\n# A standard, 3-channel 640x480 image with interleaved color channels\n# would be specified as:\n#\n# dim[0].label  = "height"\n# dim[0].size   = 480\n# dim[0].stride = 3*640*480 = 921600  (note dim[0] stride is just size of image)\n# dim[1].label  = "width"\n# dim[1].size   = 640\n# dim[1].stride = 3*640 = 1920\n# dim[2].label  = "channel"\n# dim[2].size   = 3\n# dim[2].stride = 3\n#\n# multiarray(i,j,k) refers to the ith row, jth column, and kth channel.\n\n================================================================================\nMSG: std_msgs/MultiArrayDimension\nstring label   # label of given dimension\nuint32 size    # size of given dimension (in type units)\nuint32 stride  # stride of given dimension'
    __slots__ = ['layout', 'data']
    def _get_types(self):
        return ['std_msgs/MultiArrayLayout', 'float32[]']


class Float64MultiArray(genpy.message.Message):
    _type = 'std_msgs/Float64MultiArray'
    _md5sum = '4b7d974086d4060e7db4613a7e6c3ba4'
    _has_header = False
    _full_text = '# Please look at the MultiArrayLayout message definition for\n# documentation on all multiarrays.\n\nMultiArrayLayout  layout        # specification of data layout\nfloat64[]         data          # array of data\n\n\n================================================================================\nMSG: std_msgs/MultiArrayLayout\n# The multiarray declares a generic multi-dimensional array of a\n# particular data type.  Dimensions are ordered from outer most\n# to inner most.\n\nMultiArrayDimension[] dim # Array of dimension properties\nuint32 data_offset        # padding elements at front of data\n\n# Accessors should ALWAYS be written in terms of dimension stride\n# and specified outer-most dimension first.\n# \n# multiarray(i,j,k) = data[data_offset + dim_stride[1]*i + dim_stride[2]*j + k]\n#\n# A standard, 3-channel 640x480 image with interleaved color channels\n# would be specified as:\n#\n# dim[0].label  = "height"\n# dim[0].size   = 480\n# dim[0].stride = 3*640*480 = 921600  (note dim[0] stride is just size of image)\n# dim[1].label  = "width"\n# dim[1].size   = 640\n# dim[1].stride = 3*640 = 1920\n# dim[2].label  = "channel"\n# dim[2].size   = 3\n# dim[2].stride = 3\n#\n# multiarray(i,j,k) refers to the ith row, jth column, and kth channel.\n\n================================================================================\nMSG: std_msgs/MultiArrayDimension\nstring label   # label of given dimension\nuint32 size    # size of given dimension (in type units)\nuint32 stride  # stride of given dimension'
    __slots__ = ['layout', 'data']
    def _get_types(self):
        return ['std_msgs/MultiArrayLayout', 'float64[]']


class UInt8MultiArray(genpy.message.Message):
    _type = 'std_msgs/UInt8MultiArray'
    _md5sum = '82373f1612381bb6ee473b5cd6f5d89c'
    _has_header = False
    _full_text = '# Please look at the MultiArrayLayout message definition for\n# documentation on all multiarrays.\n\nMultiArrayLayout  layout        # specification of data layout\nuint8[]           data          # array of data\n\n\n================================================================================\nMSG: std_msgs/MultiArrayLayout\n# The multiarray declares a generic multi-dimensional array of a\n# particular data type.  Dimensions are ordered from outer most\n# to inner most.\n\nMultiArrayDimension[] dim # Array of dimension properties\nuint32 data_offset        # padding elements at front of data\n\n# Accessors should ALWAYS be written in terms of dimension stride\n# and specified outer-most dimension first.\n# \n# multiarray(i,j,k) = data[data_offset + dim_stride[1]*i + dim_stride[2]*j + k]\n#\n# A standard, 3-channel 640x480 image with interleaved color channels\n# would be specified as:\n#\n# dim[0].label  = "height"\n# dim[0].size   = 480\n# dim[0].stride = 3*640*480 = 921600  (note dim[0] stride is just size of image)\n# dim[1].label  = "width"\n# dim[1].size   = 640\n# dim[1].stride = 3*640 = 1920\n# dim[2].label  = "channel"\n# dim[2].size   = 3\n# dim[2].stride = 3\n#\n# multiarray(i,j,k) refers to the ith row, jth column, and kth channel.\n\n================================================================================\nMSG: std_msgs/MultiArrayDimension\nstring label   # label of given dimension\nuint32 size    # size of given dimension (in type units)\nuint32 stride  # stride of given dimension'
    __slots__ = ['layout', 'data']
    def _get_types(self):
        return ['std_msgs/MultiArrayLayout', 'uint8[]']


class UInt16MultiArray(genpy.message.Message):
    _type = 'std_msgs/UInt16MultiArray'
    _md5sum = '52f264f1c973c4b73790d384c6cb4484'
    _has_header = False
    _full_text = '# Please look at the MultiArrayLayout message definition for\n# documentation on all multiarrays.\n\nMultiArrayLayout  layout        # specification of data layout\nuint16[]            data        # array of data\n\n\n================================================================================\nMSG: std_msgs/MultiArrayLayout\n# The multiarray declares a generic multi-dimensional array of a\n# particular data type.  Dimensions are ordered from outer most\n# to inner most.\n\nMultiArrayDimension[] dim # Array of dimension properties\nuint32 data_offset        # padding elements at front of data\n\n# Accessors should ALWAYS be written in terms of dimension stride\n# and specified outer-most dimension first.\n# \n# multiarray(i,j,k) = data[data_offset + dim_stride[1]*i + dim_stride[2]*j + k]\n#\n# A standard, 3-channel 640x480 image with interleaved color channels\n# would be specified as:\n#\n# dim[0].label  = "height"\n# dim[0].size   = 480\n# dim[0].stride = 3*640*480 = 921600  (note dim[0] stride is just size of image)\n# dim[1].label  = "width"\n# dim[1].size   = 640\n# dim[1].stride = 3*640 = 1920\n# dim[2].label  = "channel"\n# dim[2].size   = 3\n# dim[2].stride = 3\n#\n# multiarray(i,j,k) refers to the ith row, jth column, and kth channel.\n\n================================================================================\nMSG: std_msgs/MultiArrayDimension\nstring label   # label of given dimension\nuint32 size    # size of given dimension (in type units)\nuint32 stride  # stride of given dimension'
    __slots__ = ['layout', 'data']
    def _get_types(self):
        return ['std_msgs/MultiArrayLayout', 'uint16[]']


class UInt32MultiArray(genpy.message.Message):
    _type = 'std_msgs/UInt32MultiArray'
    _md5sum = '4d6a180abc9be191b96a7eda6c8a233d'
    _has_header = False
    _full_text = '# Please look at the MultiArrayLayout message definition for\n# documentation on all multiarrays.\n\nMultiArrayLayout  layout        # specification of data layout\nuint32[]          data          # array of data\n\n\n================================================================================\nMSG: std_msgs/MultiArrayLayout\n# The multiarray declares a generic multi-dimensional array of a\n# particular data type.  Dimensions are ordered from outer most\n# to inner most.\n\nMultiArrayDimension[] dim # Array of dimension properties\nuint32 data_offset        # padding elements at front of data\n\n# Accessors should ALWAYS be written in terms of dimension stride\n# and specified outer-most dimension first.\n# \n# multiarray(i,j,k) = data[data_offset + dim_stride[1]*i + dim_stride[2]*j + k]\n#\n# A standard, 3-channel 640x480 image with interleaved color channels\n# would be specified as:\n#\n# dim[0].label  = "height"\n# dim[0].size   = 480\n# dim[0].stride = 3*640*480 = 921600  (note dim[0] stride is just size of image)\n# dim[1].label  = "width"\n# dim[1].size   = 640\n# dim[1].stride = 3*640 = 1920\n# dim[2].label  = "channel"\n# dim[2].size   = 3\n# dim[2].stride = 3\n#\n# multiarray(i,j,k) refers to the ith row, jth column, and kth channel.\n\n================================================================================\nMSG: std_msgs/MultiArrayDimension\nstring label   # label of given dimension\nuint32 size    # size of given dimension (in type units)\nuint32 stride  # stride of given dimension'
    __slots__ = ['layout', 'data']
    def _get_types(self):
        return ['std_msgs/MultiArrayLayout', 'uint32[]']


class UInt64MultiArray(genpy.message.Message):
    _type = 'std_msgs/UInt64MultiArray'
    _md5sum = '6088f127afb1d6c72927aa1247e945af'
    _has_header = False
    _full_text = '# Please look at the MultiArrayLayout message definition for\n# documentation on all multiarrays.\n\nMultiArrayLayout  layout        # specification of data layout\nuint64[]          data          # array of data\n\n\n================================================================================\nMSG: std_msgs/MultiArrayLayout\n# The multiarray declares a generic multi-dimensional array of a\n# particular data type.  Dimensions are ordered from outer most\n# to inner most.\n\nMultiArrayDimension[] dim # Array of dimension properties\nuint32 data_offset        # padding elements at front of data\n\n# Accessors should ALWAYS be written in terms of dimension stride\n# and specified outer-most dimension first.\n# \n# multiarray(i,j,k) = data[data_offset + dim_stride[1]*i + dim_stride[2]*j + k]\n#\n# A standard, 3-channel 640x480 image with interleaved color channels\n# would be specified as:\n#\n# dim[0].label  = "height"\n# dim[0].size   = 480\n# dim[0].stride = 3*640*480 = 921600  (note dim[0] stride is just size of image)\n# dim[1].label  = "width"\n# dim[1].size   = 640\n# dim[1].stride = 3*640 = 1920\n# dim[2].label  = "channel"\n# dim[2].size   = 3\n# dim[2].stride = 3\n#\n# multiarray(i,j,k) refers to the ith row, jth column, and kth channel.\n\n================================================================================\nMSG: std_msgs/MultiArrayDimension\nstring label   # label of given dimension\nuint32 size    # size of given dimension (in type units)\nuint32 stride  # stride of given dimension'
    __slots__ = ['layout', 'data']
    def _get_types(self):
        return ['std_msgs/MultiArrayLayout', 'uint64[]']
