from flask import Flask, jsonify, request, render_template, redirect, url_for, g
from flask_restplus import Api, Resource, fields
from todoManager import todoDao, tens
from sqlite3 import *

DATABASE = "/Users/jaegyuhan/dev/sqlite3/todo.db"

app = Flask(__name__)
app.config.from_object(__name__)
api = Api(app, version='1.0', title='그냥 API', description='그냥 API')
ns = api.namespace('todos', description='TODO 관리 CRUD API')
ts = api.namespace('tensorflow', description = "Tensorflow 서비스 테스트" )

todo_item = api.model("todo_item", {
    "title": fields.String(required = True, description = "타이틀"),
    "completed": fields.Boolean(required = False, description = "완료여부"),
    "createdAt": fields.String(required = False, description = "생성일")
})

def connect_db():
    return connect(app.config["DATABASE"])

#g객체는 애플리케이션 전반에 공유해야할 데이터를 저장해두고 사용하는데 효율적이다 
"""
Flask에서 g 객체는 스레드와 각각의 request 내에서만 값이 유효한 스레드 로컬 변수입니다. 
사용자의 요청이 동시에 들어오더라도 각각의 request 내에서만 g 객체가 유효하기 때문에 사용자 ID를 저장해도 문제가 없습니다.
""" 
@app.before_request
def before_request():
    g.db = connect_db()


@app.teardown_request
def teardown_request(exceprion):
    if hasattr(g, "db"):
        g.db.close()
        

@app.route("/todos")
def index():
    return render_template("todoManager.html")

@ns.route('/')
class Todos(Resource):
    def get(self):
        return jsonify(todoDao.find_all())

    @ns.expect(todo_item)
    def post(self):
        todoDao.save(api.payload)
        return self.get()

@ns.route("/<id>")
@ns.doc(params={"id":"Todo item의 식별자"})
class Todo(Resource):
    
    @ns.expect(todo_item)
    def put(self, id):
        todoDao.update(id, request.json)
        return jsonify(todoDao.find_all())
    
    def delete(self, id):
        todoDao.remove(id)
        return jsonify(todoDao.find_all())

    
@ts.route("/version")
class Tens(Resource):
    def get(self):
        return jsonify(tens.getVersion())
    

@ts.route("/<value>")
class TensGet(Resource):
    def get(self, value):
        return jsonify(tens.getValue(value))
        
