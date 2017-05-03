from flask import Flask, jsonify, request, render_template, redirect, url_for
from flask_restplus import Api, Resource, fields
from todoManager import todoDao 

app = Flask(__name__)
api = Api(app, version='1.0', title='Todo-Manager API', description='Todo-Manager API')
ns = api.namespace('todos', description='Todo-Manager CRUD operations')

todo_item = api.model("todo_item", {
    "title": fields.String(required=True, description="타이틀"),
    "completed": fields.Boolean(required=False, description="완료여부"),
    "createdAt": fields.String(required=False, description="생성일")
})

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
        return self.get()
    
    def delete(self, id):
        todoDao.remove(id)
        return redirect("/todos/", code=307)
