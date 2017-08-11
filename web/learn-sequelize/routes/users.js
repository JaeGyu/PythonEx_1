var express = require('express');
var User = require('../models').User;
var router = express.Router();

router.get('/', function (req, res, next) {
  User.findAll()
    .then((users) => {
      res.json(users);
    })
    .catch((e) => {
      console.log(e);
      next(e);
    });
});

router.post('/', function (req, res, next) {
  User.create({
    name: req.body.name,
    age: req.body.age,
    married: req.body.married,
  })
    .then((result) => {
      console.log(result);
      res.status(201).json(result);
    })
    .catch((e) => {
      console.log(e);
      next(e);
    });
});

module.exports = router;
