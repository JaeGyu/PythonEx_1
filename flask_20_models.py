from sqlite3 import * 

"""
TODO
AOP 비슷한 기능으로 DB 연결 관리 할 것
"""

def update(id,book):
    name = book["name"]
    price = book["price"]
    mydb = connect("/Users/jaegyuhan/dev/sqlite3/books.db") #db파일에 연결 없다면 생성
    csr = mydb.cursor()  #커서 객체 얻기 
    csr.execute("update books set name = ?, price = ?  where id = ?", (name, price, id))
    mydb.commit()
    mydb.close()


def delete(id):
    mydb = connect("/Users/jaegyuhan/dev/sqlite3/books.db") #db파일에 연결 없다면 생성
    csr = mydb.cursor()  #커서 객체 얻기 
    csr.execute("delete from books where id = ?", id)
    mydb.commit()
    mydb.close()

def save(book):
    name = book["name"]
    price = book["price"]
    mydb = connect("/Users/jaegyuhan/dev/sqlite3/books.db") #db파일에 연결 없다면 생성
    csr = mydb.cursor()  #커서 객체 얻기 
    rst = csr.execute("insert into books(name,price) values(?,?)", (name,price))
    print("rst : ",rst)
    mydb.commit()
    mydb.close()

def find_all():
    mydb = connect("/Users/jaegyuhan/dev/sqlite3/books.db") #db파일에 연결 없다면 생성
    csr = mydb.cursor()  #커서 객체 얻기 
    csr.execute("""select name, 
                      price 
                 from books""")

    all_data = csr.fetchall()
    col_names = [column[0] for column in csr.description]

    rows = [rec for rec in all_data]
    rows_dict = map(lambda row: dict(zip(col_names, row)), all_data)

    l = [r for r in rows_dict]  

    mydb.commit()
    mydb.close()

    return l

def find_by_id(id):
    mydb = connect("/Users/jaegyuhan/dev/sqlite3/books.db") #db파일에 연결 없다면 생성
    csr = mydb.cursor()  #커서 객체 얻기 
    csr.execute("""select name, 
                      price 
                 from books
                 where id = ?
                 """,id)

    all_data = csr.fetchall()
    col_names = [column[0] for column in csr.description]

    rows = [rec for rec in all_data]
    rows_dict = map(lambda row: dict(zip(col_names, row)), all_data)

    l = [r for r in rows_dict]  

    mydb.commit()
    mydb.close()

    return l
    


    