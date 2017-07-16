const os = require('os');

console.log("os.arch() : " + os.arch());
console.log("os.uptime() : " + (os.uptime() / 60 / 60 / 24) + " 일");
console.log("os.hostname() : " + os.hostname());

console.log("os.homedir() : " + os.homedir());
console.log("os.cpus() : " + os.cpus());
console.log("os.cpus().length : " + os.cpus().length);

console.log("os.freemem() : " + os.freemem());
console.log("os.totalmem() : " + os.totalmem());

console.dir(os.cpus(), { colors: true, depth: 2 });

console.log("os.release() : " + os.release());




