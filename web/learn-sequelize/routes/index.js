var express = require('express');
var User = require('../models').User; // User?

var router = express.Router();

router.get('/', function (req, res, next) {

  User.findAll()
    .then((users) => {
      res.render('sequelize', { users });
    })
    .catch((e) => {
      console.error(e);
      next(e);
    });

});

module.exports = router;
