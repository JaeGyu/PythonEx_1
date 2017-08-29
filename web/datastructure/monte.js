function main() {
    console.log('몬테카를로 시뮬레이션');

    let num_square = 0;
    let num_circle = 0;

    for (let i = 0; i < 1000; i++) {
        const x = getRandomNumber(0, 1);
        const y = getRandomNumber(0, 1);

        num_square++;

        if (isInsideCircle() === true) {
            num_circle++;
            console.log(`${x}, ${y}`);
        }
    }

    console.log(":" , num_circle, num_square);

    const pi = 4.0 * (parseFloat(num_circle) / parseFloat(num_square));

    console.log(pi);

}

function getRandomNumber(min, max) {
    let temp = Math.random();
    temp = min + (max - min) * temp;

    return temp;
}

function isInsideCircle(x, y) {
    const x_c = 0.5;
    const y_c = 0.5;
    const r = 0.5;

    const f = Math.sqrt(x - x_c) + Math.sqrt(y - y_c) - Math.sqrt(r);

    if (f > 0.0) {
        return false;
    } else {
        return true;
    }
}

main();  // <-여기서 실행이 되어진다. 즉 getRandomNumber이 main보다 뒤에 있어도 된다.