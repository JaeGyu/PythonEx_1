const express = require('express');
const morgan = require('morgan');
const bodyParser = require('body-parser');
const app = express();

let users = [{
    id: 1,
    name: 'alice',
    age: 33
}, {
    id: 2,
    name: '홍길동',
    age: 35
}, {
    id: 3,
    name: 'bob',
    age: 45
}];

app.use(morgan('dev'));
app.use(bodyParser.json());  // application/json 형태를 파싱해 준다.
app.use(bodyParser.urlencoded({ extended: true }));  //urlencoded를 파싱해 준다.

app.get('/', (req, res) => {
    res.send("hello");
});

app.get('/users', (req, res, next) => {
    req.query.limit = req.query.limit || 10;
    next();
}, (req, res) => {
    const { limit } = req.query;

    if (Number.isNaN(parseInt(limit, 10))) {
        return res.status(400).end();
    }
    res.json(users.slice(0, limit));
    // res.send(users);
});

app.get('/users/:id', (req, res) => {
    const id = parseInt(req.params.id, 10);

    if (Number.isNaN(id)) {
        return res.status(400).end();
    }

    const user = users.filter((user) => {
        return user.id === id;
    })[0];

    if (user === undefined) {
        return res.status(404).end();
    }

    res.json(user);
});

app.delete('/users/:id', (req, res) => {
    const id = parseInt(req.params.id, 10);
    if (Number.isNaN(id)) {
        return res.status(400).end();
    }
    users = users.filter(user => user.id !== id);
    res.status(204).end();
});

app.post('/users', (req, res) => {
    const name = req.body.name;  //이건 bodyParser을 적용해야 사용할 수 있다.

    if (!name) return res.status(400).end();
    if (users.filter(user => user.name === name).length) {
        return res.status(409).end();
    }

    const age = req.body.age;
    const id = Date.now();
    const user = { id, name, age }
    users.push(user);
    res.status(201).json(user);
});

app.listen(3000, () => {
    console.log("Server is Running");
});

module.exports = app;