function getUser() {
    console.log('getUser이 호출 됨!');
}

document.getElementById('form').addEventListener('submit', function (e) {
    e.preventDefault();
    var name = e.target.username.value;
    console.log("name : ", name);

    if (!name) {
        return alert('이름을 입력하세요!');
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
    xhr.send(JSON.stringify({ name: name }));
    e.target.username.value = '';
});