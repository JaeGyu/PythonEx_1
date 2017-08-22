const express = require('express');

const { isLoggedIn } = require('./middlewares');
const { User } = require('../models')

const router = express.Router();

/**
 * 팔로우를 누르면 로그인한 유저를 검색한다음 파라미터로 넘어온 
 * id를 팔로우 정보에 입력한다. 
 */
router.post('/:id/follow', isLoggedIn, async (req, res, next) => {
    try {
        const user = await User.find({ where: { id: req.user.id } });
        await user.addFollowing(parseInt(req.params.id, 10));
        res.send('success');
    } catch (e) {
        console.error(e)
        next(e);
    }
});

module.exports = router;