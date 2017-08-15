const http = require('http');
const fs = require('fs');
const socketio = require('socket.io');

const server = http.createServer((req, res) => {
    fs.readFile('HTMLPage.html', (err, data) => {
        res.writeHead(200, { 'Content-Type': 'text/html' });
        res.end(data);
    });
});

server.listen(52273, () => {
    console.log("Server is running http://localhost:52273");
});

const io = socketio.listen(server);

io.sockets.on('connection', (socket) => { });

