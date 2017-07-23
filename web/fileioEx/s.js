const http = require('http');

http.createServer((req, res) => {
    throw new Error('f');
    res.end('f');
}).listen(8080, () => {
    console.log('f');
}).on('error', (err) => {
    console.log('ff');
});