const http = require('http');
const url = require('url');
const queryString = require('querystring');
const fs = require('fs');
const dummyUrl = "http://www.dummy.test/?";

const server = http.createServer((req, res) => {
    // console.log(req.url, req.headers.cookie);

    const parsedUrl = url.parse(dummyUrl + req.headers.cookie);
    const query = queryString.parse(parsedUrl.query);
    console.log(query);

    res.writeHead(200, { 'Set-Cookie': 'mycookie=test' });

    // fs.readFile('./node18.html', (err, data) => {
    //     if (err) {
    //         throw err;
    //     }

    //     res.end(data);
    // });

    res.end('Hello Cookie!');

}).listen(8080, () => {
    console.log('서버가 실행 되었습니다.');
});

server.on('listening', () => {
    console.log("올라 갔네요!");
});

/** 
 * 노드가 에러에 취약해서 에러가 발생하면 항상 죽는다. 그래서 이런 이벤트 리스너를 붙여 준다. 
 * 물론 아래처럼만 한다고 서버가 살아있고 그런건 아니지만 뭔가 조치를 취해 준다.
 */
server.on('error', (err) => {
    console.log(err);
});


