from sqlite3 import *

conn = connect("/Users/jaegyuhan/dev/sqlite3/fruit.db")
cus = conn.cursor()

script = """
insert into test(fruit,num,price) values('a',1,1);
insert into test(fruit,num,price) values('b',2,2);
insert into test(fruit,num,price) values('c',3,3);
"""

cus.executescript(script)

cus.close()
conn.commit()
conn.close()