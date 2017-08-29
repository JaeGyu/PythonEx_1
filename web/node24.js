
console.log("A");
setTimeout(() => { console.log("B") }, 0);
console.log("C");

//==============

function sleep(callback) {
    setTimeout(() => {
        callback();
    }, 1000);
}


/**
 * 콜백 지옥
 */
sleep(() => {
    console.log("A");
    sleep(() => {
        console.log("B");
        sleep(() => {
            console.log("C");
        });
    });
});


//==============


