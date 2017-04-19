from flask import Flask
from flask_restplus import Resource, Api 

app = Flask(__name__)
api = Api(app)

@api.route("/hello","/world")
class Hello(Resource): #Resource객체를 상속 받는다. 
    def get(self):
        return {"hello" : "world"}

if __name__ == "__main__":
    app.run(debug = True)

