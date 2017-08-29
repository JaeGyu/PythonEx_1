/**
 * 프로미스로 바꿔서 해볼 것
 */
function a(callback) {
    setTimeout(function () {
        console.log('aaaa');
        callback();
    }, 300);
}

function b(callback) {
    setTimeout(function () {
        console.log('bbbb');
        callback();
    }, 200);
}

function c(callback) {
    setTimeout(function () {
        console.log('cccc');
        callback();
    }, 100);
}

function main() {
    a(function () {
        console.log('a의 콜백');
        b(function () {
            console.log('b의 콜백');
            c(function(){
                console.log('c의 콜백');
            });
        });
    });
}

main();