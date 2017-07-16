const http = require('http')
const qs = require('querystring')

const postData = qs.stringify({ 
    "name": "test", 
    "salary": "123", 
    "age": "23" 
});

const postOptions = {
    host: 'http://dummy.restapiexample.com',
    port: '80',
    path: '/create',
    method: 'POST',
    headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Length': postData.length
    }
};

const postReq = http.request(postOptions, (res) => {
    res.setEncoding('utf-8');
    res.on('data', (chunk) => {
        console.log('response: ', chunk);
    });
});

postReq.write(postData);
postReq.end();