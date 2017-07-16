const crypto = require('crypto');

/**
 * 
 * createHash : 해시 알고리즘 
 * update : 변환할 문자열 
 * digest : 인코딩할 알고리즘 
 * 
 */

console.log("base64", crypto.createHash('sha512').update('비밀번호').digest('base64'));
console.log('hex', crypto.createHash('sha512').update('비밀번호').digest('hex'));
console.log('base64', crypto.createHash('sha512').update('다른 비밀번호').digest('base64'));










