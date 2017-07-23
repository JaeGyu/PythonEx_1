const buffer = Buffer.from('저를 버퍼로 바꿔보세요');

console.log('from():', buffer);
console.log('length:', buffer.length);
console.log('toString():', buffer.toString());
console.log('toString(base64):', buffer.toString('base64'));
console.log('toString(hex):', buffer.toString('hex'));

console.log('저를 버퍼로 바꿔보세요'.length);

const array = [Buffer.from('띄엄 '), Buffer.from('띄엄 '), Buffer.from('쓰기 ')];
const buffer2 = Buffer.concat(array);

console.log('concat():', buffer2.toString());

const buffer3 = Buffer.alloc(5);
console.log('alloc():', buffer3);


