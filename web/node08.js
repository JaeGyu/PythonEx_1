var obj = {
    "name": "alice",
    age: 32
};

console.log(Object.keys(obj));

for (var i in obj) {
    console.log(i, obj[i]);
}

console.log("===========");

var i = Object.keys(obj);

for (var k = 0; k < i.length; k++) {
    console.log(i[k], obj[i[k]]);
}


