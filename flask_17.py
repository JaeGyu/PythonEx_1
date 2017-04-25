from flask import Flask, jsonify
from flask_restplus import Resource, Api 

app = Flask(__name__)
api = Api(app)

students = []
students.append({"std_id" : 2017020001, "name" : "Alice"})
students.append({"std_id" : 2017020002, "name" : "Peter"})

@api.route("/index")
class Index(Resource):
    def get(self):
        return {"message": "/"}

@api.route("/students")
class Students(Resource):
    def get(self):
        return jsonify(students)

@api.route("/students/<int:std_id>")
class Student(Resource):
    def get(self,std_id=None):
        find_list = [student for student in students if student["std_id"] ==  std_id]
        return jsonify(find_list)


if __name__ == "__main__":
    app.run(debug=True)


