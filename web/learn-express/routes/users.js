const express = require('express');
const router = express.Router();


router.get('/', (req, res, next) => {
  console.log('네번째 미들웨어');
  res.send("유저들의 목록 입니다.");
});

router.delete('/', (req, res) => { });

module.exports = router;
