from flask import Flask, request
from flask_restplus import Resource, Api 

app = Flask(__name__)
api = Api(app)

todos = {}

@api.route("/<string:todo_id>")
class TodoSimple(Resource):
    def get(self, todo_id):
        #내용 , 상태코드, 사용자 정의 헤더
        return {todo_id : todos[todo_id]}, 201, {"schoolCode": "23232323"}

    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id : todos[todo_id]}

if __name__ == "__main__":
    app.run(debug = True)