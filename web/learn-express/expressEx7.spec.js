const app = require('./expressEx7');
const request = require('supertest');
const should = require('should');

/**
 * 테스트 수트를 만든다. 
 */
describe('GET /users는 ', () => {
    describe('성공시', () => {
        it('유저 객체를 담은 배열로 응답 한다.', (done) => {
            request(app)
                .get('/users')
                .end((err, res) => {
                    // console.log(res.body);
                    res.body.should.be.instanceOf(Array);
                    done();
                });
        });

        it('최대 limit갯수만큼 응답 한다.', (done) => {
            request(app)
                .get('/users?limit=2')
                .end((err, res) => {
                    res.body.should.have.lengthOf(2);
                    done();
                });
        });
    });

    describe('실패시', () => {
        it('limit시 숫자형이 아니면 400을 응답한다.', (done) => {
            request(app)
                .get('/users?limit=two')
                .expect(400)
                .end(done);
        });
    });
});

describe('GET /users/:id는 ', () => {
    describe('성공시', () => {
        it('id가 1인 유저 객체를 반환한다.', (done) => {
            request(app)
                .get('/users/1')
                .end((err, res) => {
                    res.body.should.have.property('id', 1);
                    done();
                });
        });
    });

    describe('실패시', () => {
        it('id가 숫자가 아닐경우 400으로 응답 한다.', (done) => {
            request(app)
                .get("/users/a")
                .expect(400)
                .end(done);
        });
        it('id로 유저를 찾을 수 없는 경우 404로 응답 한다.', (done) => {
            request(app)
                .get("/users/5")
                .expect(404)
                .end(done);
        });
    });
});

describe('GET /users/:id', () => {
    describe('성공시', () => {
        it('204를 응답 한다.', (done) => {
            request(app)
                .delete('/users/1')
                .expect(204)
                .end(done);
        });
    });
    describe('실패시', () => {
        it('id가 숫자가 아닐경우 400을 응답 한다.', (done) => {
            request(app)
                .delete('/users/a')
                .expect(400)
                .end(done);
        });
    });
});

describe('POST /users', () => {
    describe('성공시', () => {
        let name = 'kobin';
        let body;
        before(done => {
            request(app)
                .post('/users')
                .send({ name, age: 45 })
                .expect(201)
                .end((err, res) => {
                    body = res.body;
                    done();
                })
        });

        /**
         * 아래는 비동기 테스트가 아니기 때문에 done 메커니즘이 필요 없다.
         */
        it('생성된 유저 객체를 반환 한다.', () => {
            body.should.have.property('id');
        });

        /**
         * 아래는 비동기 테스트가 아니기 때문에 done 메커니즘이 필요 없다.
         */
        it('입력한 네임을 반환 한다. ', () => {
            body.should.have.property('name', name);
        });
    });
    describe('실패시', () => {
        it('name 파라메터를 누락시 400을 반환한다.', (done) => {
            request(app)
                .post('/users')
                .send({})
                .expect(400)
                .end(done)
        });
        it("name이 중복일 경우 409를 반환 한다. ", (done) => {
            request(app)
                .post('/users')
                .send({ name: 'bob', age: 45 })
                .expect(409)
                .end(done)
        });
    });
});

describe('PUT /users/:id', () => {
    describe('성공시', () => {
        it('변경된 name을 응답 한다.', (done) => {
            const name = 'peter';
            request(app)
                .put('/users/3')
                .send({ name })
                .end((err, res) => {
                    res.body.should.have.property('name', name);
                    done();
                })

        });
    });
    describe('실패시', () => {
        it('정수가 아닌 id일경우 400 응답', (done) => {
            request(app)
                .put("/users/a")
                .expect(400)
                .end(done);
        });

        it('name이 없는 경우 400응답', (done) => {
            request(app)
                .put('/users/3')
                .send({})
                .expect(400)
                .end(done);
        });

        it('없는 유저일 경우 404응답', (done) => {
            request(app)
                .put('/users/30')
                .expect(404)
                .end(done);
        });

        it('이름이 중복일 경우 409응답', (done) => {
            const name = '홍길동';
            request(app)
                .put('/users/3')
                .send({ name })
                .expect(409)
                .end(done);
        });
    });
});
