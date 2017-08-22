const express = require('express');
const { isLoggedIn, isNotLoggedIn } = require('./middlewares');
const { Post, User } = require('../models');

const router = express.Router();
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
    Post.findAll({
        include: {
            model: User,
            attributes: ['id', 'nick'],
        },
        order: [['createdAt', 'DESC']],
    })
        .then((posts) => {
            res.render('main', {
                title: 'NodeBird',
                twits: posts,
                user: req.user,
                loginError: req.flash('loginError'),
            });
        })
        .catch((e) => {
            console.error(e);
            next(e);
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


