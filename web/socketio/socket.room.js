const fs = require('fs');

const server = require('http').createServer();
const io = require('socket.io').listen(server);

server.listen(8080, function () {
    console.log("Server is Running : http://localhost:8080/");
});

server.on('request', (req, res) => {
    fs.readFile('./HTMLPageRoom.html', (err, data) => {
        // res.writeHead(200, { 'Content-Type': 'text/html' });
        res.end(data);
    });
});

io.sockets.on('connection', (socket) => {
    let roomName = null;

    socket.on('join', (data) => {
        roomName = data;
        socket.join(data);
    });

    socket.on('message', (data) => {
        console.log('클라로부터 : ', data);
        io.sockets.in(roomName).emit('message', 'test');
    });

});