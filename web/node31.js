/**
 * 각각의 잡당 연관성이 벼로 없는 것들
 * 그냥 비동기처리가 끝나는 족족 끝나면 된다.
 */
const p1 = new Promise((res, rej) => {
    setTimeout(() => {
        console.log("p1");
        res();
    }, 3000);
});
const p2 = new Promise((res, rej) => {
    setTimeout(() => {
        console.log("p2");
        res();
    }, 1000);
});
const p3 = new Promise((res, rej) => {
    setTimeout(() => {
        console.log("p3");
        res();
    }, 2000);
});


p1.then();
p2.then();
p3.then();
