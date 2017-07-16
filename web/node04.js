const http = require('http');

http.createServer(function (req, res) {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.write("Hello World\n");

    setInterval(() => {
        res.write("Hello Alice\n");
        // res.end();
    }, 1000);
}).listen(8080, function () {
    console.log("Server is running");
});