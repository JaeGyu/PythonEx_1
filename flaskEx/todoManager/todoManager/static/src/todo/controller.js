angular.module("todoApp").controller("todoCtrl", ["$scope", "todoStorage", "todoRepository", function ($scope, todoStorage, todoRepository) {

    todoRepository.findAll().then(function(d) {
        $scope.todos = d.data;
    });

    $scope.remove = function (todo) {
        todoRepository.remove(todo).then(function(d){
            $scope.todos = d.data;
        });
        
        // todoStorage.remove(todo);
    };

    $scope.add = function (newTodoTitle) {
        todoRepository.save(newTodoTitle).then(function(d){
            console.log(d);
            $scope.todos = d.data;
        });
        
        $scope.newTodoTitle = "";
    };

    $scope.update = function () {
        // todoRepository.
        todoStorage.update();
    };

}]);