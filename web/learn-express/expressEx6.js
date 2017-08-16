const express = require('express');
const app = express();

function commonMiddleware(req, res, next) {
    console.log("commonMiddleWare!!");
    next();
};


app.listen(3000, () => {
    console.log('Server is Running');
});