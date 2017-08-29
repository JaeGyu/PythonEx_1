const socketio = require('socket.io');
const cors = require('cors');
const express = require('express');

const app = express();

app.set('port', process.env.PORT || 8080);
app.use(cors());

const server = app.listen(app.get('port'), () => {
    console.log(app.get('port'), '번 포트에서 대기 중');
});

const io = socketio.listen(server);

io.sockets.on('connection', (socket) => {
    console.log('connection info:', socket.request.connection._peername);
    socket.remoteAddress = socket.request.connection._peername.address;
    socket.remotePort = socket.request.connection._peername.port;

    socket.on('message', (message) => {
        console.log('message 이벤트를 받았습니다.');
        console.dir(message);

        if (message.recepient === 'ALL') {
            console.dir('나를 포함한 모든 클라이언트에게 message 이벤트를 전송합니다.');
            io.sockets.emit('message', message);
        }
    });
});


