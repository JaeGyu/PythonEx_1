var express = require('express');
var Comment = require('../schemas/comment');

var router = express.Router();


router.post('/', function (req, res, next) {
    const comment = new Comment({
        commenter: req.body.id,
        comment: req.body.comment,
    });

    comment.save()
        .then((result) => {
            return Comment.populate(result, { path: 'commenter' });
        })
        .then((result) => {
            res.status(201).json(result);
        })
        .catch((err) => {
            console.error(err);
            next(err);
        });
});


module.exports = router;