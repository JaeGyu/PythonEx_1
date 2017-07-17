const http = require('http');
const fs = require('fs');

const server = http.createServer((req, res) => {
    if (req.url.startsWith('/login')) {
        
    } else {
        fs.readFile('./node19.html', (err, data) => {
            if (err) {
                throw err;
            }

            res.end(data);
        });
    }

    res.writeHead(200, { 'Content-Type': 'text/plain' });

});

server.listen(8080, () => {
    console.log('서버 올라감!');
})