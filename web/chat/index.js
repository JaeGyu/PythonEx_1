const express = require('express');
const path = require('path');
const indexRouter = require('./routes');

const app = express();
app.use(express.static(path.join(__dirname, 'public')));
app.set('views', path.join(__dirname, 'views'));

app.set('port', process.env.PORT || 8080);

app.use('/', indexRouter);

const server = app.listen(app.get('port'), () => {
    console.log(app.get('port'), '번 포트에서 대기 중');
});

