var arrar = [1, 2, 3];
console.log(Array.isArray(arrar));

var yoosa = {
    0: 'a',
    1: 'b',
    2: 'c',
    length: 3
};

console.log(yoosa.length);
console.log(yoosa[0]);

arrar.forEach(function (element) {
    console.log(element);
});

Array.prototype.forEach.call(yoosa, function (i) {
    console.log(i);
});


