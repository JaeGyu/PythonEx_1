/**
 * promise를 async await로 변환
 */
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

async function process() {
    console.log("처리 시작");
    await get();
    console.log("get종료");
    await create();
    console.log("create종료");
    await update();
    console.log("update종료");
}

process();
