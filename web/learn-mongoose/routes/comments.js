var express = require('express');
var Comment = require('../schemas/comment');

var router = express.Router();

router.get('/:id', function (req, res, next) {
    const trimId = req.params.id.trim();
    Comment.find({ commenter: trimId }).populate('commenter')
        .then((comments) => {
            console.log(comments);
            res.json(comments);
        })
        .catch((err) => {
            console.log("에러남");
            console.error("에러남 : ",err);
            next(err);
        });
});

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
            console.log("json 리턴~");
            res.status(201).json(result);
        })
        .catch((err) => {
            console.error(err);
            next(err);
        });
});


module.exports = router;