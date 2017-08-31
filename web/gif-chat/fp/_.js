/**
 * filter같은 함수를 응용형 함수라고 한다.
 * 응용형 함수란 함수를 인자로 받아서 원하는 시점에 해당하는 함수가 알고 있는 인자를 적용하는 식으로 프로그래밍하게 한다.
 * 이걸 응용형 프로그래밍이라고 한다. 또는 적용형 프로그래밍 이라고 한다. 
 * 이런 필터함수를 고차함수라고도 한다. 고차함수는 함수를 인자로 받거나 함수를 리턴하거나 함수안에서 인자로 받은 함수를 실행하는 함수등을
 * 고차 함수라고 한다.
 */
function _filter(list, predicate) {
    var new_list = [];

    _each(list, function (value) {
        /**
         * 함수형 프로그래밍에서는 중복을 제거하거나 어떤 부분들을 추상화 할때 함수를 사용한다.
         * 아래 users[i].age >= 30의 부분을 추상화 할 것이다. 이부분을 함수에게 위임 한다.
         * 그래서 어떤 조건일때 필터링을 할 것인가를 정한다. 
         * 어떤 조건일때 if안에 들어올 것인가를 predicate함수한테 완전히 위임 하게 된다.
         */
        if (predicate(value)) {
            new_list.push(value);
        }
    });

    // for (var i = 0; i < list.length; i++) {
    /**
     * 함수형 프로그래밍에서는 중복을 제거하거나 어떤 부분들을 추상화 할때 함수를 사용한다.
     * 아래 users[i].age >= 30의 부분을 추상화 할 것이다. 이부분을 함수에게 위임 한다.
     * 그래서 어떤 조건일때 필터링을 할 것인가를 정한다. 
     * 어떤 조건일때 if안에 들어올 것인가를 predicate함수한테 완전히 위임 하게 된다.
     */
    //     if (predicate(list[i])) {
    //         new_list.push(list[i]);
    //     }
    // }
    return new_list;
}

/**
 * 아래에서 데이터형이 어ㄸ너 건지 전혀 알수 없다.
 * 이것이 함수형 프로그래밍의 또다른 특징이다.
 */
function _map(list, mapper) {
    var new_list = [];

    /**
     * 코드가 점점 간결해지고 아래와 같은 명령형의 코드가 점점 없어 진다.
     */
    _each(list, function (value) {
        new_list.push(value);
    });

    // for (var i = 0; i < list.length; i++) {
    //     new_list.push(mapper(list[i]));
    // }
    return new_list;
}

/**
 * for문을 돌면서 안에서 하던일을 iter에게 완전히 위임을 한다.
 */
function _each(list, iter) {
    for (var i = 0; i < list.length; i++) {
        iter(list[i]);
    }

    return list;
}


exports._filter = _filter;
exports._map = _map;
exports._each = _each;
