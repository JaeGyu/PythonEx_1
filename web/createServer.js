const http = require('http');

//요청이 들어 오면 매번 콜백 함수가 실행이된다. 
http.createServer((req, res) => {
    res.write("Hello world");
    res.end();
}).listen(8080).on('listening', () => {
    console.log("server is on!");
}).on('error', (err) => {
    console.log(err);
});





