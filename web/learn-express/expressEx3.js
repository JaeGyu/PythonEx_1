const express = require('express');
const app = express();

app.get('/', (req, res) => {
    const result = [];
    const multipleNumber = 9;

    for (let i = 1; i < 5; i++) {
        result.push({
            number: `${multipleNumber} * ${i}`,
            multiple: multipleNumber * i
        });
    }

    res.send(result);
});

app.get('/filedown', (req, res) => {
    res.end('end!');
});

app.get('/redirect', (req, res) => {
    console.log('리다이렉트를 합니다.');
    res.redirect('/filedown');
});

app.get('/error', (req, res) => {
    res.status(404).send('404 NOT FOUND');
});


app.listen(3000, () => {
    console.log('Server is running!');
});


