const filesystem_var = require('fs');

//파일을 삭제 한다.
filesystem_var.unlink('/tmp/hello', (err) => {
    if (err) {
        throw err;
        return;
    }

    console.log('delete success');
});






















