[].forEach.call(document.querySelectorAll('#user-list tr'), function (el) {
    el.addEventListener('click', function () {
        console.log(el.querySelector('td'));  //첫번째 td를 가져 온다.
        var id = el.querySelector('td').textContent;
        getComment(id);
    });
});

function getComment(id) {
    console.log(id);
};