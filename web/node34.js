function get(callback) {
    setTimeout(() => {
        console.log("get을 합니다.");
        callback();
    }, 500);
};
function create(callback) {
    setTimeout(() => {
        console.log("create를 합니다.");
        callback();
    }, 3000);
};
function update(callback) {
    setTimeout(() => {
        console.log("update를 합니다.");
        callback();
    }, 2000);
};


get(function () {
    console.log("get 종료");
    create(function () {
        console.log("create 종료");
        update(function () {
            console.log("update종료");
        });
    });
});

