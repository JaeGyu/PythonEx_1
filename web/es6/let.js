var name = "global var";

function home() {
    var homever = "homever";
    for (var i = 0; i < 10; i++) { }  //var로 선언한 변수는 호이스팅이 일어나서 함수 스코프 내의 맨위로 끌어 올려진다. 아래 코드와 같이 변경 된다.
    console.log(i);
}

function home_변경() {
    var homever = "homever";
    var i;  //호이스팅이 일어 났다.
    for (i = 0; i < 10; i++) { }
    console.log(i);
}

function home_let() {
    var homever = "homever_let";
    for (let i = 0; i < 10; i++) {  //let으로 변수를 선언해주면 블록스코프로 적용이 되어서 i는 for문 안에서만 유효 하다.
    }
    console.log(i); //이 부분에서 에러남
}

home();
home_변경();
home_let();