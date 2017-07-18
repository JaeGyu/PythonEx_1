const pc = require('./parsedCookies.js');
const http = require('http');

http.createServer((req, res) => {
    const cookies = pc(req.headers.cookie);
    console.log(req.url, cookies);
    res.writeHead(200, { 'Set-Cookie': 'mycookie=test' });
    res.end('Hello');
}).listen(8080, () => {
    console.log("server is running!");
});