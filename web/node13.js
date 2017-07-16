//아래의 실행 순서와 결과를 예측 하시오. 

var a = 1;

function outer() {
    console.log("1" + a);

    function inner() {
        console.log("2" + a);
        var a = 3;
    };

    inner();

    console.log("3" + a);
};

outer();
console.log("4" + a);