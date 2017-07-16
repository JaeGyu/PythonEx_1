var releShip1 = {
    name: "zero",
    friends: ['nero', 'hero', 'xero'],
    logFriends: function () {
        var that = this;
        this.friends.forEach(function (friend) {
            console.log(that.name, friend);
        });
    }
};

releShip1.logFriends();

const releShip2 = {
    name: 'zero2',
    friends: ['aa', 'bb', 'cc'],
    logFriends() {
        this.friends.forEach((f) => {
            console.log(this.name, f);
        });
    }
};

releShip2.logFriends();

const a = function () {
    console.log("alice!");
};

const b = function add(x, y) {
    return x + y;
};

const c = function (x, y) {
    return x + y;
};

const d = (x, y) => {
    return x + y;
};

console.log(b(1, 2));
console.log(c(1, 2));
console.log(d(1, 2));