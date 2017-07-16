const url = require('url');
const URL = url.URL;
const myURL = new URL('http://www.gilbut.co.kr/book/bookList.aspx?servate1=1314234234#anchor');

console.log("myURL : ",myURL);
console.log("url.format(myURL) : " , url.format(myURL));

const parsedUrl = url.parse('http://www.gilbut.co.kr/book/bookList.aspx?servate1=1314234234#anchor');

console.log("parsedUrl : ",parsedUrl);
console.log("url.format() : ",url.format(parsedUrl));


