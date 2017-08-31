const SocketIO = require('socket.io');
const axios = require('axios');


module.exports = (server, app, sessionMiddleware) => {
    const io = SocketIO(server, { path: '/socket.io' });

    app.set('io', io); //익스프레스 변수 저장 방법 라우터에서도 io를 사용하기 때문에 전역적인 익스프레스에 변수로 저장을 해 둔다.

    /**
     * 네임스페이스 개념
     * 네임스페이스로 실시간 데이터가 전달된 주소를 구별 할 수 있습니다.
     * 기본 네임스페이스는 /이다.
     */
    const room = io.of('/room');  //room목록 등에 관련된 실시간 정보는 /room네임스페이스로만 송신된다.
    const chat = io.of('/chat');

    /**
     * 익스프레스의 미들웨어를 소켓.io에서 사용하기
     */
    io.use((socket, next) => {
        //아래의 파라미터는 왜 넘기는 것인지? 궁금함
        sessionMiddleware(socket.request, socket.request.res, next);
    });

    /**
     * 각각 네임스페이스에다가 이벤트를 달아 주면 된다. 
     * 방 목록에 관한 이벤트들만 받는다. 
     * 즉 방 목록 새로 생겼고 방 목록 제거되고
     */
    room.on('connection', (socket) => {
        console.log('room 네임스페이스에 접속');

        /**
         * 여기서 아래와 같이 room네임스페이스 connection 안에다가 disconnect라는 이벤트를 등록해야만 하는가?
         */
        socket.on('disconnect', () => {
            console.log('room 네임스페이스 접속 해제');
        });
    });

    /**
     * 
     * chat네임은 사용자가 채팅방에 들어오고 사용자가 채팅방에서 나가고 하는 것들에 대한 이벤트들만 들어 온다. 
     */
    chat.on('connection', (socket) => {
        console.log('chat 네임 스페이스에 접속');
        const req = socket.request;  //요청에 대한 정보가 들어 있다.
        const { headers: { referer } } = req; //여기에 웹 주소가 들어 있다. 여기서 방 아이디를 가져온다.

        const roomId = referer
            .split('/')[referer.split('/').length - 1]
            .replace(/\?.+/, ''); //주소 중에서 방 아이디만 가져오는 부분

        /**
         * socket.join(roomId)
         * socket.to(roomId).emit()
         * socket.leave(roomId)
         */
        socket.join(roomId); //방에 접속 하는 코드 이다.

        /**
         * socket.to는 해당 방에게만 메시지를 보낸다.
         */
        socket.to(roomId).emit('join', {
            user: 'system',
            chat: `${req.session.color}님이 입장 하셨습니다.`
        });

        socket.on('disconnect', () => {
            console.log('chat 네임스페이스 접속 해제');
            socket.leave(roomId);

            /**
             * 방에 인원이 하나도 없으면 방을 지워 버린다.
             */

            const currentRoom = socket.adapter.rooms[roomId]; //방정보와 인원이 들어 있다.
            const userCount = currentRoom ? currentRoom.length : 0;

            if (userCount === 0) {
                axios.delete(`http://localhost:8005/room/${roomId}`)
                    .then(() => {
                        console.log('방 제거 요청');
                    }).catch((e) => {
                        console.error(e);
                    });
            } else {
                socket.to(roomId).emit('exit', {
                    user: 'system',
                    chat: `${req.session.color}님이 퇴장 하셨습니다.`
                });
            }

        });


    });

    io.on('connection', (socket) => {
        const req = socket.request;
        const ip = req.headers['x-forwarded-for'] || req.connection.remoteAddress;
        console.log('새로운 클라이언트 접속!', ip, socket.id, req.ip);

        socket.on('disconnect', () => {
            console.log('클라이언트 접속 해제', ip, socket.id);
            clearInterval(socket.interval);
        });

        socket.on('error', (error) => {
            console.error(error);
        });

        /**
         * reply는 사용자 정의 이벤트이다.
         */
        socket.on('reply', (data) => {
            console.log(data);
        });

        socket.interval = setInterval(() => {
            socket.emit('news', 'Hello Socket.IO');
        }, 3000);

    });
};