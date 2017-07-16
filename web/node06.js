const http = require('https');

http.get('https://google.co.kr/', (res) => {
    let body = '';

    /*이벤트 등록을 한다. data이벤트 처리 데이터가 들어올때마다 호출된다. */
    res.on('data', (d) => {
        body += d;
    });

    /* end이벤트는 모든 데이터가 다 받아졌음을 의미 한다. */
    res.on('end', () => {
        console.log('Data: ' , body);
    });
}).on('error', (e) => {
    console.log(e);
});


