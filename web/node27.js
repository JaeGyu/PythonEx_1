var promise = new Promise((res, rej) => {
    setTimeout(() => {
        const n = 80;
        if (n <= 10) {
            res(n);  //성공을 하면 성공 콜백을 실행 한다.
        } else {
            rej(`오류 : ${n}은 10 이상 입니다.`);  //실패를 하면 실패 콜백을 실행 한다.
        }
    }, 1000);
});


promise.then((data) => {
    console.log(data);
}).catch((e) => {
    console.error(e);
});


//위에처럼 catch를 써서 실패 처리를 해도 되지만 아래처럼 해도 된다.

promise.then((data) => {
    console.log(`성공 : ${data}`);
}, (e) => {
    console.error(`실패 : ${e}`);
});