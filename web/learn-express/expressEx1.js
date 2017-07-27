const express = require('express');

const app = express();

app.get('/', (req, res) => {
    res.send('Hello express module!');
});

app.listen(3000, () => {
    console.log('Server is running port 3000!');
});