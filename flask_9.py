from sqlite3 import *

conn = connect("/Users/jaegyuhan/dev/sqlite3/fruit.db")
cus = conn.cursor()

f = input("과일명 : ")
n = input("수량  : ")
q = input("가격  : ")

cus.execute("insert into test(fruit,num,price) values(?,?,?)", (f,n,q))

cus.execute("select * from test")

print(cus.fetchall())

conn.commit()
conn.close()
