/**
 * 노드 더미 api 서버
 */
const express = require('express');
const cors = require('cors');
const app = express();

app.use(cors());

const members = [];

members.push({
    id: 1,
    name: 'alice',
    age: 32
});

members.push({
    id: 2,
    name: 'bob',
    age: 44
});

app.get('/', (req, res, next) => {
    res.send("Hello");
});

app.get('/members', (req, res, next) => {
    res.json(members);
});

app.get("/members/:id", (req, res, next) => {
    const mem = members.filter((m) => {
        return m.id == req.params.id;
    });
    res.json(mem);
});

app.listen(8080, () => {
    console.log("서버가 8080포트로 올라갔습니다.");
});