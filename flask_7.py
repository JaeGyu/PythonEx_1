from sqlite3 import * 

mydb = connect("/Users/jaegyuhan/dev/sqlite3/fruit.db") #db파일에 연결 없다면 생성
csr = mydb.cursor()

csr.execute("CREATE TABLE test(fruit VARCHAR(20), num INT, price INT)")
csr.execute("insert into test(fruit, num, price) values('Apple', 10, 1000)")
csr.execute("select * from test")

row = csr.fetchone()
print(row)
mydb.commit()
mydb.close()
