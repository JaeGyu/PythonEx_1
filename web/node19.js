const http = require('http');
const fs = require('fs');
const url = require('url');
const qs = require('querystring');
const parsedCookies = require('./parsedCookies');

const server = http.createServer((req, res) => {

    const cookies = parsedCookies(req.headers.cookie);

    if (req.url.startsWith('/login')) {
        const { query } = url.parse(req.url);
        const { name } = qs.parse(query);
        const expires = new Date();
        expires.setMinutes(expires.getMinutes() + 5);
        res.writeHead(302, {
            'Set-Cookie': `name=${encodeURIComponent(name)}; Expires=${expires.toGMTString()}; HttpOnly; Path=/`,
            'Content-Type': 'text/html',
            'Location': '/'
        });
        res.write('<meta charset="utf-8"/>');
        res.write(`<h1>${name}</h1>`);
        res.end('<h1>로그인 동작</h1>');
    } else if (cookies.name) {
        res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8' });
        res.end(`${cookies.name}님 안녕 하세요.`);
    } else {
        fs.readFile('./node19.html', (err, data) => {
            if (err) {
                throw err;
            }
            res.end(data);
        });
    }
});

server.listen(8080, () => {
    console.log('서버 올라감!');
})