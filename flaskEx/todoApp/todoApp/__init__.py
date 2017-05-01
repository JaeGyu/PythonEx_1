from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def todoApp():
	# print(url_for("static",filename="todoScript.js"))
	return render_template("todo.html")
	# return render_template("test.html")

@app.route("/todoItem.html")
def todoItem():
	return render_template("todoItem.html")