/**
 * List의 생성자 함수 정의
 */
function List() {
    this.listSize = 0;
    this.pos = 0;
    this.dataStore = [];
    // this.clear = clear;
    this.find = function (element) {
        for (let i = 0; i < this.dataStore.length; i++) {
            if (this.dataStore[i] === element) {
                return i;
            }
        }
        return -1;
    };
    this.toString = function () {
        return this.dataStore;
    };
    // this.insert = insert;
    this.append = function (element) {
        this.dataStore[this.listSize++] = element;  //추가한 다음 listSize를 하나 증가 해준다.
    };
    this.remove = function (element) {
        const foundAt = this.find(element);
        if (foundAt > -1) {
            this.dataStore.splice(foundAt, 1);  //찾은 인덱스에서 1개만큼 제거 한다.
            --this.listSize;
            return true;
        }
        return false;
    };
    this.length = function(){
        return this.listSize;
    };
}

const l = new List();
l.append("a");
l.append("b");
l.append("c");
console.log(l.length());
console.log(l.toString());
l.remove("b");
console.log(l.length());
console.log(l.toString());







