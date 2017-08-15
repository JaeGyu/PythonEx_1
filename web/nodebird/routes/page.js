const express = require('express');
const router = express.Router();
const { isLoggedIn, isNotLoggedIn } = require('./middlewares');

// const users = {
//     Followings: [{
//         nick: 'alice'
//     }, {
//         nick: 'bob'
//     }],
//     Followers: [{
//         nick: 'hong'
//     }]
// };

router.get('/profile', isLoggedIn, (req, res) => {
    res.render('profile', {
        title: '내 정보 - NodeBird',
        user: users,
        loginError: req.flash('loginError')
    });
});

router.get('/join', isNotLoggedIn, (req, res) => {
    res.render('join', {
        title: '회원가입',
        user: req.user,
        joinError: req.flash('joinError'), //-->
        loginError: req.flash('loginError')
    });
});

router.get('/', (req, res, next) => {
    res.render('main', {
        title: 'NodeBird',
        twits: [],
        user: req.user,
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


