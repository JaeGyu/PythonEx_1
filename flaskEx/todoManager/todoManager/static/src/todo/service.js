angular.module("todoApp").factory("todoRepository", function ($http) {
    var promise;
    var promise2;
    var promise3;

    var repository = {
        todos: [],

        test: function () {
            return [];
        },

        update: function (todo) {
            var id = todo.id;
            
            console.log(todo);
            
            $http({
                method: 'PUT',
                url: '/todos/' + id,
                data: todo,
                headers: {
                    'Content-Type': 'application/json'
                }

            }).then(function (response) {
                angular.copy(response, repository.todos);
                return repository.todos;
            });
        },

        findAll: function () {
            if (!promise) {
                promise = $http({
                    method: 'GET',
                    url: '/todos/',
                }).then(function (response) {
                    angular.copy(response, repository.todos);
                    return repository.todos;
                });
            }

            return promise;
        },

        remove: function (todo) {
            // console.log("todo.id : " + todo.id);
            var id = todo.id;

            // if (!promise3) {
                promise3 = $http({
                    method: "DELETE",
                    url: "/todos/" + id //이부분은 RESTful하게 변경 할 것
                }).then(function (response) {
                    angular.copy(response, repository.todos);
                    return repository.todos;
                });
            // }
            
            

            return promise3;

        },

        save: function (newTodoTitle) {
            var newTodo = {
                title: newTodoTitle,
                completed: false,
                createdAt: Date.now()
            };
            // if (!promise2) {
                promise2 = $http({
                    method: "POST",
                    url: "/todos/", //이부분은 RESTful하게 변경 할 것
                    data: newTodo,
                    headers: {
                        'Content-Type': 'application/json'
                    }
                }).then(function (response) {
                    angular.copy(response, repository.todos);
                    return repository.todos;
                });
            // }

            return promise2;
        }

    };

    return repository;
});


angular.module("todoApp").factory("todoStorage", function () {
    var TODO_DATA = "TODO_DATA";
    var storage = {
        todos: [],
        /*
         함수명에 _를 붙이면 private라는 의미이다. 
         자바스크립트 코드 작성시 관습
         */
        _saveToLocalStorage: function (data) {
            localStorage.setItem(TODO_DATA, JSON.stringify(data));
        },

        _getFromLocalStorage: function () {
            return JSON.parse(localStorage.getItem(TODO_DATA)) || [];
        },

        get: function () {
            /*
             뷰와 연결된 데이터를 자동으로 리프레시 해주는 기능이 있는데 즉 다이제스트 사이클이라고 한다. 
             이 사이클에 맞게 작성을 할려면 앵귤러에서 제공해주는 몇가지 메서드를 사용해야 핟다. 
             그중에 하나가 angular.copy이다. 
             */
            console.log(storage._getFromLocalStorage());
            angular.copy(storage._getFromLocalStorage(), storage.todos);
            return storage.todos;
        },

        remove: function (todo) {
            var idx = storage.todos.findIndex(function (item) {
                return item.title === todo.title;
            });

            if (idx > -1) {
                storage.todos.splice(idx, 1);
                storage._saveToLocalStorage(storage.todos);
            }
        },

        add: function (newTodoTitle) {
            var newTodo = {
                title: newTodoTitle,
                completed: false,
                createdAt: Date.now()
            };

            storage.todos.push(newTodo);
            storage._saveToLocalStorage(storage.todos);
        },

        update: function () {
            storage._saveToLocalStorage(storage.todos);
        }

    };

    return storage;
});