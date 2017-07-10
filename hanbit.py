from flask import Flask, request
import sqlite3
import json

app = Flask(__name__)
app.debug = True

def get_db_con() -> sqlite3.connect:
    return sqlite3.connect("./토요_파이썬/db.sqlite")

def jsonize(result, header):
    items = [dict(zip([key[0] for key in header], row)) for row in result]
    return json.dumps(items, ensure_ascii=False, indent=4)

@app.route("/")
def hello():
    with get_db_con() as con:
        cur = con.cursor()
        q = "select * from hanbit_books"
        result = cur.execute(q)
        result_json = jsonize(result, cur.description)

        print(result_json)

    return result_json

@app.route("/books/by/author")
def get_books_by_author():
    name = request.args.get("name")

    with get_db_con() as con:
        cur = con.cursor()
        q = "select * from hanbit_books where author like :name order by title"
        param = {
            "name": "%" + name + "%"
        }

        result = cur.execute(q, param)
        result_json = jsonize(result, cur.description)
    
    return result_json

@app.route("/books/by/month")
def get_books_by_month():
    month = request.args.get("month")
    if int(month) < 10:
        month = "0" + str(int(month))
    with get_db_con() as con:
        cur = con.cursor()
        q = "select * from hanbit_books where strftime('%m', pub_date) = :month order by pub_date desc"
        param = {
            "month" : month
        }
        result = cur.execute(q, param)
        result_json = jsonize(result, cur.description)
    
    return result_json


#아래처럼 json을 처리하면 안될거 같음 
#클라이언트 쪽에서 사용자가 스키마를 알고 있다면 문제 없긴 할 거 같음
def jsonize2(result):
    result_json = json.dumps(list(result.fetchall()), ensure_ascii=False)
    return result_json

if __name__ == "__main__":
    app.run()