from sqlite3 import * 


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
print(l)

mydb.commit()
mydb.close()

    