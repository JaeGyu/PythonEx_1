from flask import g

def modify(query):
    mydb = g.db
    csr = mydb.cursor()  # 커서 객체 얻기 
    csr.execute(query)
    mydb.commit()

def update(id, todo_item):
    title = todo_item["title"]
    completed = todo_item["completed"]
    modify("update todo_list set title = '{}', completed = {}  where id = {}".format(title, int(completed), id))

def remove(id):
    modify("delete from todo_list where id = {}".format(id))


def save(todo_item):
    title = todo_item["title"]
    completed = todo_item["completed"]
    createdAt = todo_item["createdAt"]
    modify("insert into todo_list(title,completed,create_time) values('{}',{},'{}')".format(title, int(completed), createdAt))

def find_all():
    mydb = g.db 
    csr = mydb.cursor()  # 커서 객체 얻기 
    csr.execute("""select id,
                          title, 
                          create_time,
                          completed
                 from todo_list""")

    all_data = csr.fetchall()
    
    col_names = [column[0] for column in csr.description]

    # rows = [rec for rec in all_data]
    rows_dict = map(lambda row: dict(zip(col_names, row)), all_data)

    l = [r for r in rows_dict]

    #함수로 뺄 것 (response 관련된 model 정의 할 것)
    l = map(lambda data: {"id": data["id"], "title": data["title"], "createdAt": data["create_time"],
                                 "completed": bool(int(data["completed"]))}, l)
    
    l = [i for i in l] #왜 이렇게 해줘야 하는 것인가?

    mydb.commit()

    return l
