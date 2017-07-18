const http = require('http');
const fs = require('fs');
const url = require('url');
const qs = require('querystring');
const parsedCookies = require('./parsedCookies');

const session = {};

const server = http.createServer((req, res) => {
    const cookies = parsedCookies(req.headers.cookie);

    if (req.url.startsWith('/login')) {
        const { query } = url.parse(req.url);
        const { name } = qs.parse(query);
        const expires = new Date();

        expires.setMinutes(expires.getMinutes() + 5);
        const randomInt = +new Date();

        session[randomInt] = {
            name,   //이건 원래 name : name
            expires  //이건 원래 expires : expires
        };

        res.writeHead(302, {
            'Set-Cookie': `session=${randomInt}; Expires=${expires.toGMTString()}; HttpOnly; Path=/`,
            'Content-Type': 'text/html; charset=utf-8',
            'Location': '/'
        });

        res.write('<meta charset="utf-8"/>');
        res.write(`<h1>${name}</h1>`);
        res.end('<h1>로그인 동작</h1>');
    } else if (cookies.session && session[cookies.session] && session[cookies.session].expires > new Date()) {
        res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8' });
        res.end(`${session[cookies.session].name}님 안녕 하세요.`);
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