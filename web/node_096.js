const sumNumber = (start, end, result) => {
    if (start > end) return result;
    return sumNumber(start + 1, end, result + start);
};

const factorial = (n) => {
    if (n === 0) return 1;
    return factorial(n - 1) * n;
};

console.log('result: ', sumNumber(1, 10, 0));
console.log('factorial: ', factorial(4));

