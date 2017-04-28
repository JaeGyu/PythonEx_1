from flask import Flask, jsonify, request
from flask_restplus import Api, Resource, fields
import flask_20_models as books

app = Flask(__name__)

api = Api(app, version='1.0', title='Books API',
    description='A simple Books API',
)

ns = api.namespace('books', description='Books operations')

book = api.model("book",{
    "name" : fields.String(required = True, description="도서명"),
    "price" : fields.Integer(required = False, description="가격")
})

@ns.route("/")
class Books(Resource):
    def get(self):
        return jsonify(books.find_all())
    
    @ns.expect(book)
    # @ns.marshal_with(book, code=201)
    def post(self):
        book = api.payload
        books.save(book)
        return self.get()
    

@ns.route("/<id>")
@ns.doc(params={"id":"도서의 아이디"})
class Book(Resource):
    def get(self,id):
        return jsonify(books.find_by_id(id))
    
    def delete(self):
        return []



nss = api.namespace('blog/categories', description='Blog operations')

@nss.route("/")
class CategoryCollection(Resource):

    def get(self):
        return []
    
    @api.response(201, "Category successfully created.")
    def post(self):
        print(request.json)
        return None, 201

if __name__ == "__main__":
    app.run(debug = True)