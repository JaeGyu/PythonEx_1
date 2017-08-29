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

/**
 * 
 * then에 다음 순서의 비동기 promise를 리턴해주면 
 * 체인 방식으로 순차적으로 비동기 처리를 할 수 있다. 
 * 아래는 같은 프로미스를 리턴했지만 각각 다른 프로미스를 리턴해도 된다.
 */
buyAsync(500)
    .then((balance) => {
        console.log(`잔액은 ${balance}원 입니다.`);
        return buyAsync(balance);
    })
    .then((balance) => {
        console.log(`잔액은 ${balance}원 입니다.`);
        return buyAsync(balance);
    })
    .then((balance) => {
        console.log(`잔액은 ${balance}원 입니다.`);
        return buyAsync(balance);
    })
    .catch((e) => {
        console.error(e);
    });