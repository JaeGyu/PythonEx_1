const http = require('http');

http.createServer((req, res) => {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    console.log(req);

    /*
    write는 우선 버퍼에 차곡차곡 쌓는다. 그리고 버퍼가 차는 족족 클라이언트로 보낸댜.
    그래서 중간중간 보내게 된다. 
    그리고 데이터를 청크 단위로 쪼개서 보낸다. 
    그래서 header에 자동으로 Transfer-Encoding: chunked가 설정 되어 진다.    
    */
    res.write('Alice is good.');

    //end는 실행 즉시 보낸다.
    //어떤데이터던 보낸다음 접속을 종료 한다.
    res.end('Hello world\n');
}).listen(8080, () => {
    console.log("Server listen started", new Date());
});

console.log("Server running", new Date());