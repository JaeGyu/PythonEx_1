from sqlite3 import *

conn = connect("/Users/jaegyuhan/dev/sqlite3/fruit.db")
cus = conn.cursor()

r1 = ("수박", 10, 1000)
r2 = ("참외", 67, 2033)
r3 = ("토마토", 23, 123123)

data = (r1,r2,r3)

cus.executemany("insert into test(fruit,num,price) values(?,?,?)", data)

conn.commit()
conn.close()
