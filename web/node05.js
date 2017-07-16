const http = require('http')

http.createServer((req, res) => {
    // res.writeHead(200, { 'Content-Type': 'text/plain' })
    res.writeHead(200, { 'Content-type': 'text/html' })
    res.end('<h1>Hello</h1>')
}).listen(8080, () => {
    console.log("서버가 올라 갔다.")
})
