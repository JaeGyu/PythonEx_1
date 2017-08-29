
/**
 * res : successCallback
 * rej : failCallback
 */
const promise = new Promise((res, rej) => {
    setTimeout(() => {
        const name = "alice";
        res(name);
    }, 1000);
});

promise.then((name) => {
    console.log('안녕하세요, ' + name + '님');
});

