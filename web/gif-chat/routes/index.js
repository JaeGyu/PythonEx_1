const express = require('express');
const router = express.Router();

const Room = require('../schemas/room');
const Chat = require('../schemas/chat');


// router.get('/', (req, res) => {
//     res.render('index_io');
//     // res.render('index');  //webSocket용
// });

router.get('/', async (req, res, next) => {
    try {
        const rooms = await Room.find({});
        res.render('main', {
            rooms,
            title: 'GIF 채팅방',
            error: req.flash('roomError')
        });
    } catch (error) {
        console.error(error);
        next(error);
    }
});

router.get('/main', (req, res) => {
    res.render('main', {
        title: 'main',
        rooms: [],
        error: {},
    });
});

/**
 * 방 만드는 화면 용 라우터 
 */
router.get('/room', (req, res) => {
    res.render('room', {
        title: '채팅방 생성'
    });
});

/**
 * 실제 방을 생성 하는 라우터
 */
router.post('/room', async (req, res, next) => {
    try {
        const room = new Room({
            title: req.body.title,
            max: req.body.max,
            owner: req.session.color,
            password: req.body.password,
        });
        const newRoom = await room.save();
        const io = req.app.get('io');
        io.of('/room').emit('newRoom', newRoom);  // /room에 있던 사용자들에게 새로운 방이 생겼다고 알려 준다.
        res.redirect(`/room/${newRoom._id}?password=${req.body.password}`);
    } catch (error) {
        console.error(error);
        next(error);
    }
});

/**
 * 채팅방 안에 들어가는 라우터
 */
router.get('/room/:id', async (req, res, next) => {
    try {
        const room = await Room.findOne({ _id: req.params.id }); //해당 방에 대한 정보를 가져 온다.
        const io = req.app.get('io');


        if (!room) {  //없는 방에 들어 갔을 경우
            req.flash('rromError', '존재하지 않는 방 입니다. ');
            return res.redirect('/');
        }

        if (room.password && room.password != req.query.password) {
            req.flash('rromError', '방 비밀 번호가 틀렸습니다.');
            return res.redirect('/');
        }

        const { rooms } = io.of('/chat').adapter;

        //방 정원 초과 했을때
        if (rooms && rooms[req.params.id] && room.max <= rooms[req.params.id].length) {
            req.flash('rromError', '허용 인원 초과');
            return res.redirect('/');
        }

        const chats = await Chat.find({ room: room._id }).sort('createAt');

        return res.render('chat', {
            room,
            title: room.title,
            chats,
            user: req.session.color,
        });
    } catch (error) {
        console.error(error);
        next(error);
    }
});

router.post('/room/:id/chat', async (req, res, next) => {
    try {
        const chat = new Chat({
            room: req.params.id,
            user: req.session.color,
            chat: req.body.chat,
        });

        await chat.save();
        req.app.get('io').of('/chat').to(req.params.id).emit('chat', chat);
        res.send('ok');
        
    } catch (error) {
        console.error(error);
        next(error);
    }
});

router.get('/chat', (req, res) => {
    res.render('chat', {
        title: 'chat',
        chats: []
    });
});

module.exports = router;