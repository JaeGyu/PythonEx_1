const path = require('path');

const string = __filename;

console.log("path.sep : " + path.sep);
console.log("path.delimiter : " + path.delimiter);
console.log("path.dirname(string) : " + path.dirname(string));
console.log(string);

console.log("path.extname(string) : " + path.extname(string));
console.log("path.basename(string) : " + path.basename(string));
console.log("path.basename(string,'js') : " + path.basename(string, path.extname(string)));
console.dir("path.parse(string) : " + path.parse(string), { colors: true, depth: 2 });
console.log("path.normalize('/users///d//df') : " + path.normalize("/users///d//df"));

console.log("path.isAbsolute('./') : " + path.isAbsolute("./"));
console.log("path.isAbsolute('/') : " + path.isAbsolute("/"));

console.log("path.parse(string) : ", path.parse(string));



