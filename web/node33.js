function s(callback, time) {
    setTimeout(() => {
        callback();
    }, time);
}

s(() => {
    console.log("p1");
    s(() => {
        console.log("p2");
    }, 2000);
}, 3000);


function p(time) {
    return new Promise((res, rej) => {
        setTimeout(() => {
            res();
        }, time);
    });
}

p(3000).then(() => {
    console.log("pp1");
    return p(2000);
}).then(() => {
    console.log("pp2");
});