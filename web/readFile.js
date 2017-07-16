const fs = require('fs');

fs.readFile('./readme.txt', (err, data) => {
    if (err) {
        throw err;
    }

    console.log(data);  //바이트로 나옴
    console.log(data.toString());
});




