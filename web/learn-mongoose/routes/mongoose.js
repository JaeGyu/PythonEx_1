var express = require('express');
var router = express.Router();

router.get('/', (req, res, next) => {
    let users = [{
        _id: '12341234',
        name: 'alice',
        age: 23,
        married: 1,
    }, {
        _id: '1887888',
        name: 'bob',
        age: 33,
        married: 0,
    }];
    res.render('mongoose', {
        title: '몽구스 서버',
        users
    });
});

module.exports = router;