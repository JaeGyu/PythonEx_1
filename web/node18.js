const http = require('http');

const server = http.createServer((req, res) => {
    console.log('서버 실행');
    res.writeHead(200, { 'Content-Type': 'text/html' });
    res.write('<head><meta charset="utf-8"/></head>');
    res.write('<h1>Alice Hello!</h1>');
    res.end();
}).listen(8080, () => {
    console.log('서버가 실행 되었습니다.');
});

server.on('listening', ()=>{
    console.log("올라 갔네요!");
});


