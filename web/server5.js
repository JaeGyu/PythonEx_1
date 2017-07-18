const http = require('http');
const fs = require('fs');
const url = require('url');
const qs = require('querystring');
const pc = require('./parsedCookies.js');

http.createServer((req, res) => {
    res.end("Hello World");
}).listen(8080, () => {
    console.log("Server is running");
});

