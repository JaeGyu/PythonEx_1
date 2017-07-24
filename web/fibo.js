const nextFiboNum = (num) => {

    /**
     * 함수가 목표로 한 값
     */
    if (num === 1 || num === 0) {
        return 1;
    }

    return nextFiboNum(num - 1) + nextFiboNum(num - 2);
};


console.time('time');
for (let i = 1; i <= 30; i++) {
    console.log(nextFiboNum(i));
}
console.timeEnd('time');
