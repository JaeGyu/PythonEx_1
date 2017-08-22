const express = require('express');
const multer = require('multer');
const router = express.Router();
const path = require('path');
const fs = require('fs');

const { Post, Hashtag, User } = require('../models');
const { isLoggedIn } = require('./middlewares');

fs.readdir('uploads', (error) => {
    if (error) {
        console.error('uploads 폴더가 없어 uploads 폴더를 생성합니다.');
        fs.mkdirSync('uploads');
    }
});

const upload = multer({
    storage: multer.diskStorage({   //서버의 디스크에 이미지를 저장한다.
        destination(req, file, cb) {  //파일 저장 경로
            cb(null, 'uploads/');
        },
        filename(req, file, cb) {
            const ext = path.extname(file.originalname);  //넘어오는 파일 정보에서 파일명을 빼낸다.
            cb(null, path.basename(file.originalname, ext) + new Date().valueOf() + ext);
        }
    }),
    limits: { fileSize: 5 * 1024 * 1024 },
});


/**
 * 여기는 예외 처리 안해주나?
 */
router.post('/img', isLoggedIn, upload.single('img'), (req, res) => {
    console.log(req.file);  //upload.single로 저장한 파일은 req.file에 저장 되어 있다. 
    res.json({ url: `/img/${req.file.filename}` });
});

const upload2 = multer();
router.post('/', isLoggedIn, upload2.none(), async (req, res, next) => {
    //게시글 업로드
    try {
        const post = await Post.create({
            content: req.body.content,
            img: req.body.url,
            userId: req.user.id
        });

        const hashtags = req.body.content.match(/#[^\s]*/g);
        if (hashtags) {
            const result = await Promise.all(hashtags.map(tag => Hashtag.findOrCreate({
                where: { title: tag.slice(1).toLowerCase() },
            })));

            await post.addHashtags(result.map(r => r[0]));
        }
    } catch (error) {
        console.error(error);
        next(error);
    }
});


router.get('/hashtag', async (req, res, next) => {
    const query = req.query.hashtags;
    if (!query) {
        return res.redirect('/');
    }

    try {
        const hashtag = await Hashtag.find({ where: { title: query } });
        let posts = [];
        if (hashtag) {
            posts = await hashtag.getPosts({ include: [{ model: User }] }); //관련 포스트를 가져오는데 사용자 정보를 포함해준다.
        }
        return res.render('main', {
            title: `${query} | NodeBird`,
            user: req.user,
            twits: posts,
        });
    } catch (e) {
        console.error(e);
        return next(e);
    }
});

module.exports = router;