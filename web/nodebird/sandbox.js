const path = require('path');

console.log(process.env.PORT);
console.log(__dirname);
console.log(path.join(__dirname, 'views'))

const a = (b, c) => (
    b, c
);

const b = (a, c) => {
    return (a, c);
};

const c = (a, b);

console.log(a(1, 3));
console.log(b(1, 3));
console.log(c(1, 3));