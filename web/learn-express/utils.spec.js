const utils = require('./utils');
const assert = require('assert');
const should = require('should');


/**
 * 테스트 환경을 만든다.
 */
describe('utils.js 모듈의 capitialize함수는 ', () => {
    it('문자열의 첫번째 문자를 대문자로 반환한다.', () => {
        const result = utils.capitialize('hello');
        // assert.equal(result, 'Hello');

        result.should.be.equal('Hello');
    });
})