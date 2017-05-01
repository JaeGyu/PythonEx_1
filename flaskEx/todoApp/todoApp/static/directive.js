angular.module("todoApp").directive("todoTitle",function(){
		return {
			template: "<h1>Todo</h1>"
		};
	});
	
angular.module("todoApp").directive("todoItem", function(){
	return {
		// templateUrl: "/todoItem.html"
		templateUrl: "/static/todoItem.html"
	}
});

angular.module("todoApp").directive("todoFilters",function(){
    return {
        templateUrl: "/static/todoFilters.html"
    };
});

angular.module("todoApp").directive("todoForm",function(){
    return {
        templateUrl: "/static/todoForm.html"
    };
});