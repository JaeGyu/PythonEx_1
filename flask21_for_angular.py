from flask import Flask, jsonify
from flask_restplus import Api, Resource, fields

app = Flask(__name__)
api = Api(app)

@app.route("/")
def index():
    return ""

if __name__ == "__main__":
    app.run(debug=True)

