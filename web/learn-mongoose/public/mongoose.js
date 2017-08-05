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
    console.log("getUser이 실행 됐어요!");

    var xhr = new XMLHttpRequest();

    /**
     * ajax 결과 콜백
     */
    xhr.onload = function () {
        if (xhr.status === 200) {
            var users = JSON.parse(xhr.responseText);
            console.log(users);

            var tbody = document.querySelector('#user-list tbody');
            tbody.innerHTML = '';

            users.map(function (user) {
                console.log(user);

                var row = document.createElement('tr');
                row.addEventListener('click', function () {
                    getComment(user._id);
                });

                var td = document.createElement('td');
                td.textContent = user._id;
                row.appendChild(td);

                td = document.createElement('td');
                td.textContent = user.name;
                row.appendChild(td);

                td = document.createElement('td');
                td.textContent = user.age;
                row.appendChild(td);

                td = document.createElement('td');
                td.textContent = user.married ? '기혼' : '미혼';
                row.appendChild(td);

                tbody.appendChild(row);

            });
        } else {
            console.error(xhr.responseText);
        }
    };

    xhr.open('GET', '/users');
    xhr.send();

};

function getComment(id) {
    console.log("코멘트가 눌렸음");
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
    e.target.name.value = '';
    e.target.age.value = '';
    e.target.married.checked = false;

});