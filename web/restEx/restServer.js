const http = require('http');
const fs = require('fs');

const users = {};

http.createServer((req, res) => {
    if (req.method === 'GET') {
        if (req.url === '/') {
            return fs.readFile('./restFront.html', (err, data) => {
                if (err) {
                    throw err;
                }
                res.end(data);
            });
        } else if (req.url === '/about') {
            return fs.readFile('./about.html', (err, data) => {
                if (err) {
                    throw err;
                }

                res.end(data);
            });
        } else if (req.url === '/users') {
            res.end(JSON.stringify(users));
        }

        //리턴을 하는거와 안하는거의 차이는?
        return fs.readFile(`.${req.url}`, (err, data) => {
            if (err) {
                res.writeHead(404, 'NOT FOUND');
                res.end('NOT FOUND');
            }

            res.end(data);
        });

    } else if (req.method === 'POST') {
        if (req.url === '/users') {
            let body = '';
            req.on('data', (data) => {
                body += data;
            });

            // return 안해줘도 됨 
            return req.on('end', () => {
                console.log('POST 본문(Body):', body);
                const { name } = JSON.parse(body);
                const id = +new Date();
                users[id] = name;
                res.writeHead(201);
                res.end('등록 성공');
            });
        }
    } else if (req.method === 'PUT') {
        if (req.url.startsWith('/users/')) {
            const key = req.url.split('/')[2];
            let body = '';
            req.on('data', (data) => {
                body += data;
            });

            return req.on('end', () => {
                console.log('PUT 본문(BODY): ', body);
                users[key] = JSON.parse(body).name;
                res.end(JSON.stringify(users));
            });
        }

    } else if (req.method === 'DELETE') {
        if (req.url.startsWith('/users/')) {
            const key = req.url.split('/')[2];
            delete users[key];
            return res.end(JSON.stringify(users));
        }
    }
    res.writeHead(404, 'NOT FOUND');
    return res.end('NOT found');
}).listen(8080, () => {
    console.log("server is running!");
});