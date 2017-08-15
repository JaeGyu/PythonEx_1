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

let id = 0;

io.sockets.on('connection', (socket) => {
    id = socket.id;

    socket.on('rint', (data) => {
        console.log('Client Send Data: ', data);

        // io.sockets.emit('smart', data);
        // socket.broadcast.emit('smart', data);
        io.sockets.to(id).emit('smart', data);
    });
});

