const LocalStrategy = require('passport-local').Strategy;
const bcrypt = require('bcrypt');
const { User } = require('../models');

module.exports = (passport) => {
    passport.use(new LocalStrategy({
        usernameField: 'email',
        passwordField: 'password',
    }, async (email, password, done) => {  //done(에러, 성공, 실패);
        try {
            const exUser = await User.find({ where: { email } });
            if (exUser) {
                const result = await bcrypt.compare(password, exUser.password);  //비밀번호를 비교해 준다. 
                if (result) {
                    done(null, exUser); //성공을 하면 성공 매개변수 위치에 사용자 정보를 넣어 준다.
                } else {
                    done(null, false, { message: '비밀 번호가 일치하지 않습니다.' });
                }
            } else {
                done(null, false, { message: '가입 안된 회원 입니다. ' });  //로그인 실패
            }
        } catch (err) {
            console.error(err);  //로그인 에러
            done(err);
        }
    }));
};