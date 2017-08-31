// const util = require('./_');

// const _filter = util._filter;
// const _map = util._map;
// const _each = util._each;

const { _each, _filter, _map } = require('./util');

var users = [
    { id: 1, name: 'ID', age: 36 },
    { id: 2, name: 'BJ', age: 32 },
    { id: 3, name: 'JM', age: 32 },
    { id: 4, name: 'PJ', age: 27 },
    { id: 5, name: 'HA', age: 25 },
    { id: 6, name: 'JE', age: 26 },
    { id: 7, name: 'JI', age: 31 },
    { id: 8, name: 'MP', age: 23 },
];

console.log(_filter([1, 2, 3, 4], function (num) {
    return num % 2 === 0;
}));


console.log("\n\n_filter적용 : \n", _filter(users, function (user) {
    return user.age >= 30;
}));

console.log("\n\n_filter적용 : \n", _filter(users, function (user) {
    return user.age < 30;
}));

console.log("\n\n_map적용 : \n", _map(_filter(users, function (user) {
    return user.age >= 30;
}), function (user) {
    return user.name;
}));

console.log("\n\n_map적용 : \n", _map(_filter(users, function (user) {
    return user.age < 30;
}), function (user) {
    return user.age;
}));

console.log("\n\n", _map([1, 2, 3, 4], function (num) { return num * 2; }));