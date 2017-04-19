from flask import Flask
from flask_restplus import Api, Resource

app = Flask(__name__)
api = Api(app)

# @api.route("/hello_ep")
# class HelloEp(Resource):
#     def get(self):
#         return {"message" : "404 Not Found"}

@api.route("/hello", endpoint = "hello_ep" )
class Hello(Resource):
    def get(self):
        return {"hello" : "world3"}


if __name__ == "__main__":
    app.run(debug = True)

