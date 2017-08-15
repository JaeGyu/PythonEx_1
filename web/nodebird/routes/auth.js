const express = require('express');
const router = express.Router();
const bcrypt = require('bcrypt');
const passport = require('passport');
const { isLoggedIn, isNotLoggedIn } = require('./middlewares');
const { User } = require('../models');


router.post('/join', isNotLoggedIn, async (req, res, next) => {
    const { email, nick, password } = req.body;
    try {
        const exUser = await User.find({ where: { email } });
        if (exUser) {
            req.flash('joinError', '이미 가입 되어 있습니다.');
            return res.redirect('/join');
        }

        console.time('암호');
        const hash = await bcrypt.hash(password, 12); //비밀번호를 암호화 한다. 
        console.timeEnd('암호');

        await User.create({
            email,   //email: email
            nick,    // nick: nick
            password: hash,
        });

        return res.redirect('/');

    } catch (err) {
        console.log(err);
        next(err);
    }
});


router.post('/login', isNotLoggedIn, (req, res, next) => {
    /* 
        local전략 의 결과인 done(에러, 성공, 실패)가 아래 콜백으로 넘어온다. 
        (authError, user, info)
    */
    passport.authenticate('local', (authError, user, info) => {  // 'local' 은 로컬전략을 수행하라는 뜻
        if (authError) {
            console.error(authError);
            return next(authError);  //에러처리 핸들러로 넘겨 버린다.
        }

        if (!user) {
            req.flash('loginError', info.message);
            return res.redirect('/');
        }

        return req.login(user, (loginError) => {   //로그인이 성공하면 passport는 세션에 로그인 정보를 저장해둔다. req.user에서 찾을 수 있다. 
            if (loginError) {
                console.error(loginError);
                return next(loginError);
            }
            return res.redirect('/');
        });  //passport가 login을 req에 추가 해준다.
    })(req, res, next);
});

router.get('/logout', isLoggedIn, (req, res, next) => {
    req.logout();  //passport에서 req에 자동으로 logout를 추가 해 준다.
    req.session.destroy();
    res.redirect('/');
});

router.get('/kakao', passport.authenticate('kakao'));

router.get('/kakao/callback', passport.authenticate('kakao', {
    failureRedirect: "/",

}), (req, res) => {
    res.redirect('/');
});

module.exports = router;