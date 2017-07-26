const express = require('express');
const router = express.Router();

// router.get('/', function(req, res, next) {
//   res.render('index', { title: 'Express' });
// });

router.get('/', (req, res, next) => {
  console.log('세번째 미들웨어');

  try {
    throw new Error('에러 발생');
  } catch (error) {
    next(error);
  }

  res.send("hello");
});


router.get('/posts', (req, res) => {
});

router.post('/', (req, res) => {
});


module.exports = router;
