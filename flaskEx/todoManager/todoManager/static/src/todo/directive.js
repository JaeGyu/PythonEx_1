angular.module("todoApp").directive("todoTitle",function(){
		return {
			template: "<h1>Todo Manager</h1>"
		};
	});
	
angular.module("todoApp").directive("todoItem", function(){
	return {
		// templateUrl: "/todoItem.html"
		templateUrl: "/static/src/todo/view/todoItem.html"
	}
});

angular.module("todoApp").directive("todoFilters",function(){
    return {
        templateUrl: "/static/src/todo/view/todoFilters.html"
    };
});

angular.module("todoApp").directive("todoForm",function(){
    return {
        templateUrl: "/static/src/todo/view/todoForm.html"
    };
});