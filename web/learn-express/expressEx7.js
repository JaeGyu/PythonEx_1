const express = require('express');
const morgan = require('morgan');
const app = express();

const users = [{
    name: 'alice',
    age: 33
}, {
    name: '홍길동',
    age: 35
}];

app.use(morgan('dev'));

app.get('/', (req, res) => {
    res.send("hello");
});

app.get('/users', (req, res) => {
    res.json(users);
    // res.send(users);
})

app.listen(3000, () => {
    console.log("Server is Running");
});



module.exports = app;