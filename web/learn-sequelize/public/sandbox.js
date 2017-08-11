const { User } = require('../models');

User.create({
    name: 'alice2',
    age: 32,
    married: false,
    comment: '앨리스 입니다.',
}).then((result) => {
    console.log(result);
}).catch((err) => {
    console.log(err);
});

User.findAll({})
    .then((result) => {
        console.log(result);
    })
    .catch((e) => {
        console.error(e);
    });