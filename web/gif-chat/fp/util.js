const util = {
    _each: function (list, iter) {
        for (var i = 0; i < list.length; i++) {
            iter(list[i]);
        }
        return list;
    },
    _filter: function (list, predicate) {
        var new_list = [];
        util._each(list, function (value) {
            if (predicate(value)) {
                new_list.push(value);
            }
        });
        return new_list;
    },
    _map: function (list, mapper) {
        var new_list = [];

        util._each(list, function (value) {
            new_list.push(value);
        });

        return new_list;
    },
};


module.exports = util;