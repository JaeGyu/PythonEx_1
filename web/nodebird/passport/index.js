const local = require('./localStrategy');
const kakao = require('./kakaoStrategy');
const { User } = require('../models');

module.exports = (passport) => {

    /**
     * 세션 메모리에 user정보 전부를 저장 하면 메모리 부족하니
     * user.id만 저장 한다. 
     */
    passport.serializeUser((user, done) => {
        done(null, user.id);
    });

    /**
     * user.id를 토대로 다시 user정보를 복원 한다. 
     */
    passport.deserializeUser((id, done) => {
        User.find({ where: { id } })
            .then(user => done(null, user))
            .catch((e) => {
                console.error(e);
                done(e);
            });
    });

    local(passport);
    kakao(passport);
};
