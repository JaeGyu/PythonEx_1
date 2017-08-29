function buyAsync(name, mymoney, payment) {
    return new Promise(function (res, rej) {
        setTimeout(function () {
            const balance = mymoney - payment;
            if (balance > 0) {
                console.log(`${name}: ${payment}원을 지불했습니다.`);
                res(balance);
            } else {
                rej(`${name}: 잔액은 ${balance}원입니다. 구매할 수 없습니다.`);
            }
        }, 1000);
    });
}

Promise.all([
    buyAsync("alice", 500, 200),
    buyAsync("bob", 600, 300),
    buyAsync("peter", 1000, 500)
]).then(function (balance) {
    console.log(balance);
})
    .catch(function (error) {
        console.log(error)
    });

