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

[].forEach.call(yoosa, (i) => {
    console.log(i);
});

Array.from(yoosa).forEach((i) => {
    console.log(i);
});


function arrayLike() {
    console.log(arguments);
    [].forEach.call(arguments, (i) => {
        console.log(i);
    });
};

arrayLike(1, 2, 3);




