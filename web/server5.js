const http = require('http');
const fs = require('fs');
const url = require('url');
const qs = require('querystring');
const pc = require('./parsedCookies.js');

const session = {};

http.createServer((req, res) => {
    const cookies = pc(req.headers.cookie);
    console.log(cookies);

    if (req.url.startsWith('/login')) {
        const { query } = url.parse(req.url);
        console.log(url.parse(req.url), query);
        const { name } = qs.parse(query);
        const expires = new Date();

        expires.setMinutes(expires.getMinutes() + 1);

        const sessionId = +new Date();
        session[sessionId] = {
            name,
            expires
        };
        res.writeHead(302, {
            Location: "/",
            'Set-Cookie': `session=${sessionId}; Expires=${expires.toGMTString()}; HttpOnly; Path=/`,
        });
        res.end();
    } else if (cookies.session && session[cookies.session].expires > new Date()) {
        res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8' });
        res.end(`${session[cookies.session].name}님 안녕하세요`);
    } else {
        fs.readFile('./server4.html', (err, data) => {
            if (err) {
                throw err;
            }
            res.end(data);
        });
    }
}).listen(8080, () => {
    console.log("Server is running");
});

