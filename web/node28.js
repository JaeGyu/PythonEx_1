function buyAsync(mymoney) {
    return new Promise((res, rej) => {
        setTimeout(() => {
            const payment = 40;
            const balance = mymoney - payment;
            if (balance > 0) {
                console.log(`${payment}원을 지불했습니다.`);
                res(balance);
            } else {
                rej(`잔액은 ${mymoney}원입니다. 구매할 수 없습니다.`);
            }
        }, 1000);
    });
}

buyAsync(500)  //값을 넘길 수 있다. 넘긴 인수를 Promise객체가 실행하는 익명 함수 안에서 사용할 수 있다.
    .then((balance) => {
        console.log(`잔액은 ${balance}원입니다.`);
    }).catch((e) => {
        console.error(e);
    });