const util = require('util');
const crypto = require('crypto');

const dontUseMe = util.deprecate((x, y) => {
    console.log(x + y);
}, '더이상 사용 하지 마세요!');

dontUseMe(1, 2);

const rand = util.promisify(crypto.randomBytes);

rand(64)
    .then((buf) => {
        console.log(buf.toString('base64'));
    })
    .catch((error) => {
        console.log(error);
    });



