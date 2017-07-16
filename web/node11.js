function add1(x, y) {
    return x + y;
};

const add2 = (x, y) => {
    return x + y;
};

console.log(add1(1, 2));
console.log(add1(1, 2));

const add3 = (x, y) => x + y;

console.log(add3(1, 2));

const add4 = (x, y) => (x + y);

console.log(add4(1, 2));

function not1(x) {
    return !x;
};

const not2 = x => !x;
const not3 = (x) => { return !x; };

console.log(not3(0));

console.log(function (x) {
    return !x;
}(0));

console.log((x) => {
    return !x;
});