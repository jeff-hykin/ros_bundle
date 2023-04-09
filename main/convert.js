const messageTypes = {}

// http://wiki.ros.org/msg
const builtInDataTypePattern = /bool|byte|char|duration|time|float32|float64|int8|int16|int32|int64|string|uint8|uint16|uint32|uint64/
const dataSlotPattern        = /^(?: |\t)*((?:\w|\/)+)(\[\d*\])?(?: |\t)*(\w+)( *=.*)?/

const folderWithMsgFiles = "somewhere"
const defineLater = []
const filePathsForType = {}
for (const eachPath of await FileSystem.recursivelyListPathsIn(folderWithMsgFiles)) {
    if (eachPath.endsWith(".msg")) {
        const dataTypeName = FileSystem.basename(eachPath).slice(0,-4)
        const dataTypeScopedName = `${FileSystem.basename(FileSystem.parentPath(FileSystem.makeAbsolutePath(eachPath)))}/${dataTypeName}`
        if (!filePathsForType[dataTypeName]) {
            filePathsForType[dataTypeName] = []
        }
        if (!filePathsForType[dataTypeScopedName]) {
            filePathsForType[dataTypeScopedName] = []
        }
        filePathsForType[dataTypeName].push(dataTypeName)
        filePathsForType[dataTypeScopedName].push(dataTypeName)
        const actionText = await FileSystem.read(eachPath)
        const actionTextWithoutComments = actionText.replace(/^( |\t)*#.*(\n|$)/g,"")
        const content = actionTextWithoutComments.replace(/^( |\t)*(\n|$)/g,"")
        let dataSlots = content.split("\n").map(each=>each.match(dataSlotPattern))
        for (const [each, index] of dataSlots.map((each, index)=>[each, index])) {
            if (!each) {
                console.error(`Line ${index} inside of ${eachPath} is not correct.\nContent is: ${each}\nIt should match the following regex but doesn't: /^(?: |\\t)*((?:\\w|\\/)+)(\\[\\d*\\])?( |\\t)*(\\w+)( *=.*)?/`)
            }
        }
        dataSlots = dataSlots.filter(each=>each)
        defineLater.push({
            dataTypeName,
            dataTypeScopedName,
            eachPath,
            actionText,
            actionTextWithoutComments,
            content,
            dataSlots,
        })
    }
}

while (defineLater.length > 0) {
    const {
        dataTypeName,
        dataTypeScopedName,
        eachPath,
        actionText,
        actionTextWithoutComments,
        content,
        dataSlots,
    } = defineLater.pop()
    
    // 
    // convert format if possible
    // 
    const dataStructure = {}
    for (const [ line, baseType, attributeName, arrayInfo, constantInfo ] of dataSlots.map(each=>each.match(dataSlotPattern))) {
        // 
        // if unknown type
        // 
        if (!baseType.match(builtInDataTypePattern) && !messageTypes[baseType]) {
            // TODO: add an infinite loop check
            // come back to this one
            defineLater.push({
                dataTypeName,
                dataTypeScopedName,
                eachPath,
                actionText,
                actionTextWithoutComments,
                content,
                dataSlots,
            })
        }
        
        // 
        // handle types
        // 
        const isArrayType = !(arrayInfo == null || arrayInfo == '')
        let arraySize = null
        let constantData = null
        // http://wiki.ros.org/msg
        if (isArrayType) {
            const arraySizeString = arrayInfo.replace(/\[|\]/g, "")
            // if it has a size
            if (arraySizeString.length != 0) {
                arraySize = arraySizeString-0
            }
        }
        if (constantInfo) {
            const dataInfo = constantInfo.replace(/^( |\t)*=( |\t)*/,"").replace(/( |\t)*$/,"")
            if (baseType == 'string') {
                // no trailing comments allowed
                // no escaping
                constantData = dataInfo
            } else {
                const numberString = dataInfo.replace(/#.*/,"").trim()
                constantData = numberString-0
            }
        }
        dataStructure[attributeName] = {
            baseType,
            isArrayType,
            arraySize,
            constantData,
        }
    }
    for (const name of [dataTypeName, dataTypeScopedName,]) {
        // if it already exists
        if (messageTypes[name] && JSON.stringify(messageTypes[name]) != JSON.stringify(dataStructure)) {
            console.error(`${name} is defined twice with conflicting definitions\n    definitions: ${filePathsForType[name]}`,)
        }
        messageTypes[dataTypeName] = dataStructure
    }
}


// import genpy.message
// class Log(genpy.message.Message):
//     _type = 'rosgraph_msgs/Log'
//     _md5sum = 'acffd30cd6b6de30f120938c17c593fb'
//     _has_header = True
//     _full_text = "##\n## Severity level constants\n##\nbyte DEBUG=1 #debug level\nbyte INFO=2  #general level\nbyte WARN=4  #warning level\nbyte ERROR=8 #error level\nbyte FATAL=16 #fatal/critical level\n##\n## Fields\n##\nHeader header\nbyte level\nstring name # name of the node\nstring msg # message \nstring file # file the message came from\nstring function # function the message came from\nuint32 line # line the message came from\nstring[] topics # topic names that the node publishes\n\n================================================================================\nMSG: std_msgs/Header\n# Standard metadata for higher-level stamped data types.\n# This is generally used to communicate timestamped data \n# in a particular coordinate frame.\n# \n# sequence ID: consecutively increasing ID \nuint32 seq\n#Two-integer timestamp that is expressed as:\n# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')\n# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')\n# time-handling sugar is provided by the client library\ntime stamp\n#Frame this data is associated with\nstring frame_id\n"
//     DEBUG=1
//     INFO=2
//     WARN=4
//     ERROR=8
//     FATAL=16
//     __slots__ = [ 'header', 'level', 'name', 'msg', 'file', 'function', 'line', 'topics',  ]
//     def _get_types(self):
//         return ['std_msgs/Header', 'byte', 'string', 'string', 'string', 'string', 'uint32', 'string[]']