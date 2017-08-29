function get() {
    return new Promise((res, rej) => {
        setTimeout(() => {
            console.log("get을 합니다.");
            res();
        }, 500);
    });
}

function create() {
    return new Promise((res, rej) => {
        setTimeout(() => {
            console.log("create를 합니다.");
            res();
        }, 3000);
    });
}

function update() {
    return new Promise((res, rej) => {
        setTimeout(() => {
            console.log("update를 합니다.");
            res();
        }, 2000);
    });
};

get().then(() => {
    console.log("get종료");
    return create();
}).then(() => {
    console.log("create종료");
    return update();
}).then(() => {
    console.log("update종료");
});