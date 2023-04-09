// 1. create a database of dependencies, which can be manually added to
//    Why? because there's no reliable way to figure out what a python package depends on without installing the package

// 2. create a scanner using python tree sitter that finds all the import statements for all files in a particular folder

// 3. create $HOME/python/__dependencies__/

// 4. create a function that hashes folders

// 5. 


// const database = {
//     ["name"]: {
//         ["version"]: {
//             canBeDelivered: null, // null == unknown
//             hasBeenDelivered: false,
//             gitUrl: null,
//             modules: {
//                 ["module_name"]: {
//                     path: "source path",
//                 }
//             },
//             dependsOn: {
//                 ["name"]: ["constraints"]
//             }
//         },
//     },
// }