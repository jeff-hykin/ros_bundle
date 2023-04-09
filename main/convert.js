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



// from ctypes import *
// class a_struct(Structure):
//     _pack_ = 1
//     _fields_ = [
//         ("p"    , c_void_p  ),
//         ("magic_number"    , c_uint8   ),
//         ("horizontal_angle", c_float   ),
//         ("vertical_angle"  , c_float   ),
//         ("depth"           , c_float   ),
//         ("status"          , c_uint8   ),
//     ]