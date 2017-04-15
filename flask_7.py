from sqlite3 import * 

mydb = connect("/Users/jaegyuhan/dev/sqlite3/fruit.db") #db파일에 연결 없다면 생성
csr = mydb.cursor()  #커서 객체 얻기 

csr.execute("CREATE TABLE test(fruit VARCHAR(20), num INT, price INT)") # 테이블 생성 
csr.execute("insert into test(fruit, num, price) values('Apple', 10, 1000)")
csr.execute("select * from test")

row = csr.fetchone()  #선택된 테이블에서 하나의 레코드 읽기
print(row)
mydb.commit()
mydb.close()
