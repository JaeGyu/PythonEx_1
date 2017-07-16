const url = require("url");
const querystring = require("querystring");
const parsedUrl = url.parse("http://www.a.com/?page=3&limit=10&category=nodejs&category=javascript");

console.log(parsedUrl.query);

const query = querystring.parse(parsedUrl.query);

console.log(query);  //분해되어서 객체화 되었다. 
console.log(querystring.stringify(query)); //객체화된 쿼리를 문자열로 다시 조립한다.










