const express = require('express');

const router = express.Router();

const users = {
    Followings: [{
        nick: 'alice'
    }, {
        nick: 'bob'
    }],
    Followers: [{
        nick: 'hong'
    }]
};

router.get('/profile', (req, res) => {
    res.render('profile', {
        title: '내 정보 - NodeBird',
        user: users,
        loginError: req.flash('loginError')
    });
});

router.get('/join', (req, res) => {
    res.render('join', {
        title: '회원가입',
        user: null,
        joinError: req.flash('joinError'), //-->
        loginError: req.flash('loginError')
    });
});

router.get('/', (req, res, next) => {
    res.render('main', {
        title: 'NodeBird',
        twits: [],
        user: null,
        loginError: req.flash('loginError')
    });
});

router.get('/lay', (req, res, next) => {
    res.render('layout', {
        title: 'NodeBird',
        twits: [],
        user: 'Alice',
        loginError: req.flash('loginError')
    });
});


module.exports = router;


