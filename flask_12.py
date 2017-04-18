from flask import Flask
from flask_restplus import Resource, Api  

app = Flask(__name__)
api = Api(app, version='1.0', title='Sample API',
    description='스터디용 API',
)

@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'hello':'Alice'}

if __name__ == "__main__":
    app.run(debug = True)



