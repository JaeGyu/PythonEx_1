const expires = new Date();

//날짜 및 시간을 보여 준다.
console.log(expires);

//분 만 따로 빼낸다. 
console.log(expires.getMinutes());

//5분 뒤를 출력 한다.
console.log(expires.getMinutes() + 5);

//타임 스탬프 형태로 객체를 생성 한다. 
const timestamp = +new Date();
console.log(timestamp);

