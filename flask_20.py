from flask import Flask, jsonify
from flask_restplus import Api, Resource
import flask_20_models as model

app = Flask(__name__)
api = Api(app)

'''
1) get] cars
'''

'''
GET
db를 이용해서 가져온다.
'''
@api.route("/books")
class Cars(Resource):
    def get(self):
        return jsonify(model.books)

@api.route("/cars/")

if __name__ == "__main__":
    app.run(debug = True)