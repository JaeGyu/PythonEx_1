
var sayNode = function () {
    console.log('Node');
};

var es = 'ES';
var oldObject = {
    sayJS: function () {
        console.log('JS');
    },
    sayNode: sayNode
};

oldObject[es + 6] = 'Fantastic';

oldObject.sayNode();
oldObject.sayJS();
console.log(oldObject.ES6);
console.log(oldObject);

console.log("=====");

const newObject = {
    sayJS() {
        console.log('JS');
    },
    sayNode,
    [es + 6]: 'FantasticNew'
};

newObject.sayNode();
newObject.sayJS();
console.log(newObject.ES6);
