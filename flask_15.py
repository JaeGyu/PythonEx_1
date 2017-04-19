from flask import Flask
from flask_restplus import Api, Resource

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return {"hello2" : "world2"}


api.add_resource(HelloWorld, "/hello", "/world")


if __name__ == "__main__":
    app.run(debug = True)



