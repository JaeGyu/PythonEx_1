function getList() {
    return new Promise((res, rej) => {
        setTimeout(() => {
            res([1, 2, 3, 4, 5]);
        }, 500);
    });
}

function doSomething(value) {
    return new Promise((res, rej) => {
        setTimeout(()=>{
            console.log("db처리를 합니다. 1초가 걸립니다. 다음의 값을 처리 합니다.", value);
            res();
        },1000);
    });
}

function process(){
    getList().then(async (data) => {
        for (let i = 0; i < data.length; i++) {
            await doSomething(data[i]);
        }
    });
}

process();

