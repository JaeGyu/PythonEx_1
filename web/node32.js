const p1 = new Promise((res, rej) => {
    setTimeout(() => {
        // console.log("p1");
        res();
    }, 3000);
});

const p2 = new Promise((res, rej) => {
    setTimeout(() => {
        // console.log("p2");
        res();
    }, 2000);
});


p1.then(() => {
    console.log("p1");
    return p2;
}).then(() => {
    console.log("p2");
});