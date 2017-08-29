const express = require('express');
const axios = require('axios');
const router = express.Router();

const URL = 'http://localhost:8002/v2';

const request = async (req, api) => {
    try {
        if (!req.session.jwt) {
            const tokenResult = await axios.post(`${URL}/token`, {
                clientSecret: process.env.CLIENT_SECRET
            });

            req.session.jwt = tokenResult.data.token;
        }
        return await axios.get(`${URL}${api}`, {
            headers: { authorization: req.session.jwt }
        }); //파라미터로 넘어온 API로 요청을 날린다.
    } catch (error) {
        console.error(error);
        if (error.response.status < 500) {
            return error.response;  //500이하의 에러라면 에러메시지를 넘겨준다. 
        }
        throw error;  //에러 자체를 넘겨 준다.
    }
};

router.get('/mypost', async (req, res, next) => {
    try {
        const result = await request(req, '/posts/my');
        res.json(result.data);
    } catch (error) {
        console.error(error);
        next(error);
    }
});

router.get('/search/:hashtag', async (req, res, next) => {
    try {
        const result = await request(req, `/posts/hashtag/${encodeURIComponent(req.params.hashtag)}`);
        res.json(result.data);
    } catch (error) {
        if (error.code) {
            console.error(error);
            next(error);
        }
    }
});

router.get('/test', async (req, res, next) => {
    try {
        if (!req.session.jwt) {
            const tokenResult = await axios.post('http://localhost:8002/v1/token', {
                clientSecret: process.env.CLIENT_SECRET
            });

            if (tokenResult.data && tokenResult.data.code === 200) {
                req.session.jwt = tokenResult.data.token;
            } else {
                return res.json(tokenResult.data);  //토큰 발급 실패 이유
            }
        }

        const result = await axios.get('http://localhost:8002/v1/test', {
            headers: { authorization: req.session.jwt }
        });

        return res.json(result.data);
    } catch (e) {
        console.error(e);
        if (e.response.status === 419) {  //토큰 만료
            return res.json(e.response.data);
        }
        return next(e);
    }
});

router.get('/', (req, res) => {
    res.render('main', { key: process.env.CLIENT_SECRET });
});

module.exports = router;