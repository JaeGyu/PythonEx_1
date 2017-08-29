const express = require('express');
const router = express.Router();

router.get('/', (req, res) => {
    res.render('index_io');
});


router.get('/main', (req, res) => {
    res.render('main',{
        title:'main',
        rooms:[],
        error:{},
    });
});

router.get('/room',(req,res)=>{
    res.render('room', {
        title:'room'
    });
});

router.get('/chat',(req,res)=>{
    res.render('chat', {
        title:'chat',
        chats:[]
    });
});

module.exports = router;