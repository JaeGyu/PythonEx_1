from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

"""
아래처럼 class 로 자원을 표현 하면 
테스트 하기 편리 해진다. 서버를 안띄워도 되니깐
"""
class User(Resource):
    def post(self):
        return {'status' : 'success'}
    def get(self):
        return [{'name' : 'alice'}, {'name' : 'bob'}]

class Hello(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(User, '/users')
api.add_resource(Hello, "/")

if __name__ == "__main__":
    app.run(debug=True)