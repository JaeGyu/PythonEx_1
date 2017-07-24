const returnFunction = () => (a, b) => a + b;
const plus = returnFunction();

console.log(plus(10, 20));
const reFun = () => {
    return (a, b) => {
        return a + b;
    };
};

console.log(reFun()(10, 20));