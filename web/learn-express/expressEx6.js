const express = require('express');
const app = express();

function commonMiddleware(req, res, next) {
    console.log("commonMiddleWare!!");
    next(new Error("에러 발생"));
    // next();
};

/**
 * 이전 미들웨어에서 에러가 발생 하면 아래의 미들웨어는 건너 뛴다. 
 * 바로 에러 미들웨어로 간다. 
 */
function commonMiddleware2(req, res, next) {
    console.log("중간 미들웨어");
    next();
};

/**
 * 에러 미들웨어는 에러를 처리 하거나 아니면 다음 미들웨어에게 에러를 넘긴다. 
 * 에러를 처리 했으면 그냥 next()만 호출 안했으면 next(err) 호출!
 */
function errorMiddleware(err, req, res, next) {
    console.log("에러미들웨어 실행");
    console.log(err.message);
    next();
};

app.use(commonMiddleware);
app.use(commonMiddleware2);
app.use(errorMiddleware);


app.listen(3000, () => {
    console.log('Server is Running');
});