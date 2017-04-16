from sqlite3 import *

mydb = connect("/Users/jaegyuhan/dev/sqlite3/fruit.db")
csr = mydb.cursor()  #커서 객체 얻기 

csr.execute("insert into test(fruit, num, price) values('banana', 10, 1000)")
csr.execute("select * from test")
print(csr.fetchall())
mydb.commit()
mydb.close()
