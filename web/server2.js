const http = require('http');
const fs = require('fs');

http.createServer((req, res) => {
    //data로 버퍼가 들어오는데 이버퍼를 그냥 클라로 보낸다.
    fs.readFile('./server2.html', (err, data) => {
        if (err) {
            throw err;
        }

        res.end(data);
    });
}).listen(8080, () => {
    console.log("8080번 포트에서 서버 대기 중입니다.!");
});


