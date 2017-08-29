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
     * 
     * 뭔가 추가해 주고 싶은 정보가 있다면 deserialize단계에서 추가 해준다.
     * 아래에선 유저의 팔로워와 팔로잉 정보를 추가해 줬다.
     */
    passport.deserializeUser((id, done) => {
        User.find({
            where: { id },
            include: [{
                model: User,
                attributes: ['id', 'nick'],
                as: 'Followers',
            }, {
                model: User,
                attributes: ['id', 'nick'],
                as: 'Followings'
            }]
        })
            .then(user => done(null, user))  //done에서 req.user에 입력 한다.
            .catch((e) => {
                console.error(e);
                done(e);
            });
    });

    local(passport);
    kakao(passport);
};
