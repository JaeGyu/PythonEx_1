const http = require('http');
const hostname = '127.0.0.1';
const port = 3000;

const users = [{
    name: 'alice',
    age: 33
}, {
    name: '홍길동',
    age: 34
}];

const server = http.createServer((req, res) => {
    console.log(req.url);

    if (req.url === '/') {
        res.statusCode = 200;
        res.setHeader('Content-Type', 'text/plain');
        res.end("Hello World\n");
    } else if (req.url === '/users') {
        res.statusCode = 200;
        res.setHeader('Content-Type', 'application/json');
        res.end(JSON.stringify(users, null, 4));
    } else {
        res.statusCode = 404;
        res.end('Not Found');
    }

});

server.listen(8080, () => {
    console.log(`Server is Running : http://${hostname}:${port}/`);
});


