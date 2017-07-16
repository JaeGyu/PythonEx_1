const cond = true;

const promise = new Promise((res, rej) => {
    if (cond) {
        res('성공');
    } else {
        rej('실패');
    }
});

promise
    .then((message) => {
        console.log(message);
    })
    .catch((err) => {
        console.error(err);
    });


promise
    .then((msg) => {
        console.log("1:", msg);
        return new Promise((res, rej) => {
            res(msg);
        });
    }).then((msg) => {
        console.log("2: ", msg);
        return new Promise((res, rej) => {
            res(msg);
        });
    }).then((msg) => {
        console.log("3: ", msg);
    });