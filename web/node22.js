const fs = require('fs');

const data = fs.readFileSync('./readme.txt', 'utf8');
console.log(data);

fs.readFile('./readme.txt', 'utf8', (err, data) => {
    console.log(data);
});