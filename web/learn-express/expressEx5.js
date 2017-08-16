const express = require('express');
const app = express();
const logger3 = require('morgan');


/**
 * 미들웨어는 인터페이스가 정해져 있다. (req,res,next)
 * 미들웨어는 자기가 할일을 다 한 다음에 next함수를 호출 해줘야 한다.
 */
function logger(req, res, next) {
    console.log("i am logger");
    next();
};

function logger2(req, res, next) {
    console.log("i am logger2");
    next();
};


app.use(logger);
app.use(logger);
app.use(logger2);
app.use(logger3('dev'));

app.listen(3000, () => {
    console.log("Server is Running!");
});
