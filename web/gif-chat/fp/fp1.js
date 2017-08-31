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

// 30세 이상인 유저를 거른다.
var list = [];
for (var i = 0; i < users.length; i++) {
    if (users[i].age >= 30) {
        list.push(users[i]);
    }
}

console.log(list);

//30세 이상인 users의 names를 수집 한다.
var names = [];
for (var i = 0; i < list.length; i++) {
    names.push(list[i].name);
}
console.log(names);

//30세 미만인 users를 거른다.
var list = [];
for (var i = 0; i < users.length; i++) {
    if (users[i].age < 30) {
        list.push(users[i]);
    }
}
console.log(list);

//30세 미만인 users의 age를 수집한다.
var age = [];
for (var i = 0; i < list.length; i++) {
    age.push(list[i].age);
}
console.log(age);

/**
 * 위의 코드를 함수형으로 변경하면서 중복을 제거 할 것이다.
 */

// _filter , _map으로 리팩토링

/**
 * filter같은 함수를 응용형 함수라고 한다.
 * 응용형 함수란 함수를 인자로 받아서 원하는 시점에 해당하는 함수가 알고 있는 인자를 적용하는 식으로 프로그래밍하게 한다.
 * 이걸 응용형 프로그래밍이라고 한다. 또는 적용형 프로그래밍 이라고 한다. 
 * 이런 필터함수를 고차함수라고도 한다. 고차함수는 함수를 인자로 받거나 함수를 리턴하거나 함수안에서 인자로 받은 함수를 실행하는 함수등을
 * 고차 함수라고 한다.
 */
function _filter(list, predicate) {
    var new_list = [];
    for (var i = 0; i < list.length; i++) {
        /**
         * 함수형 프로그래밍에서는 중복을 제거하거나 어떤 부분들을 추상화 할때 함수를 사용한다.
         * 아래 users[i].age >= 30의 부분을 추상화 할 것이다. 이부분을 함수에게 위임 한다.
         * 그래서 어떤 조건일때 필터링을 할 것인가를 정한다. 
         * 어떤 조건일때 if안에 들어올 것인가를 predicate함수한테 완전히 위임 하게 된다.
         */
        if (predicate(list[i])) {
            new_list.push(list[i]);
        }
    }
    return new_list;
}

/**
 * 아래에서 데이터형이 어ㄸ너 건지 전혀 알수 없다.
 * 이것이 함수형 프로그래밍의 또다른 특징이다.
 */
function _map(list, mapper) {
    var new_list = [];
    for (var i = 0; i < list.length; i++) {
        new_list.push(mapper(list[i]));
    }
    return new_list;
}

console.log("\n\n_filter적용 : \n", _filter(users, function (user) {
    return user.age >= 30;
}));

console.log("\n\n_filter적용 : \n", _filter(users, function (user) {
    return user.age < 30;
}));

// console.log("\n\n", _filter([1, 2, 3, 4], function (num) { return num % 2 === 0; }));

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