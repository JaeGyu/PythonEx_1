
/**
 * 실행하고자 하는 처리를 작성한 함수를 인수로 넘긴다.
 * 그 함수는 res,rej의 인수를 받는다.
 * 
 * res: 함수 안의 처리가 끝났을 때 호출해야 하는 콜백 함수. 어떤 값이라도 넘길 수 있음
 * res는 다음 처리를 실행하는 함수에 전달 된다. 
 * 
 * rej: 함수 안의 처리가 실패했을때 호출해야 하는 콜백 함수, 어떠한 값도 인수로 넘길 수 있음
 * 대부분의 경우 오류 메시지 문자열을 인수로 사용함
 */
var promise = new Promise(function (resolve, reject) {
    setTimeout(() => {
        console.log("A");
        resolve(); //비동기 함수의 끝을 알린다. 콜백 호출
    }, 1000);
});

/**
 * 약속이 성공하면 then안의 콜백을 실행 시켜라
 */
promise.then(() => {
    console.log("B");
});