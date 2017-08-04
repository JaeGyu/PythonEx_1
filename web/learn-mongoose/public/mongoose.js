/**
 * document.querySelectorAll의 결과는 유사 배열이다. 
 * forEach를 사용하기 위해 Array의 프로토타임을 call 했다.
 */
[].forEach.call(document.querySelectorAll('#user-list tr'), function (el) {
    el.addEventListener('click', function () {
        console.log(el.querySelector('td'));  //첫번째 td를 가져 온다.
        var id = el.querySelector('td').textContent;
        getComment(id);
    });
});

//사용자 로딩
function getUser() {
    var xhr = new XMLHttpRequest();

    console.log("getUser이 실행 됐어요!");
};

function getComment(id) {
    console.log(id);
};

document.getElementById('user-form').addEventListener('submit', function (e) {
    e.preventDefault();
    console.log("user-form 서브밋~!!");
    var name = e.target.username.value;
    var age = e.target.age.value;
    var married = e.target.married.checked;
    console.log(name, age, married);

    if (!name) {
        return alert('이름을 입력하세요');
    }

    if (!age) {
        return alert('나이를 입력하세요');
    }

    var xhr = new XMLHttpRequest();

    xhr.onload = function () {
        if (xhr.status === 201) {
            console.log(xhr.responseText);
            getUser();
        } else {
            console.error(xhr.responseText);
        }
    };

    xhr.open('POST', '/users');
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.send(JSON.stringify({ name: name, age: age, married: married }));
    e.target.age.value = '';
    e.target.married.checked = false;

});