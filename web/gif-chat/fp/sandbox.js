const referer = "/room/x887dfffd";

const roomId = referer
    .split('/')[referer.split('/').length - 1]
    .replace(/\?.+/, '');



console.log(roomId);
console.log(referer.split('/'));
console.log(referer.split('/')[referer.split('/').length - 1]);



