from flask import Flask
from flask_restplus import Api, Resource

app = Flask(__name__)
api = Api(app)


#아래의 클래스는 다른 모듈에 작성하고 import를 통해 불러와서 사용 할 수 있다.
class HelloWorld(Resource):
    def get(self):
        return {"hello2" : "world2"}


api.add_resource(HelloWorld, "/hello", "/world")


if __name__ == "__main__":
    app.run(debug = True)



