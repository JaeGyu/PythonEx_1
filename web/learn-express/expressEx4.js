const express = require('express');
const app = express();

app.use((req, res) => {
    const agent = req.header('User-Agent');
    const paramName = req.query.name;
    console.log('age: ', req.query);
    const browerChrome = 'Hello chrome';
    const browerOthers = 'Hello Others';
    console.log(agent);
    console.log(paramName);
    console.log(req.headers);
    console.log(req.baseUrl);
    console.log(req.hostname);
    console.log(req.protocol);

    if (agent.toLocaleLowerCase().match('chrome/')) {
        res.write(`<div><p>${browerChrome}</p></div>`);
    } else {
        res.write(`<div><p>${browerOthers}</p></div>`);
    }

    res.write(`<div><p>${agent}</p></div>`);
    res.write(`<div><p>${paramName}</p></div>`);

    res.end();

});

app.listen(3000, () => {
    console.log('Server is running!');
});