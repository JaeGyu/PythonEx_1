from flask import Flask, render_template, request

app = Flask(__name__)

def isPrime(num):
	return num % 2 == 0

@app.route('/')
def jaegyu():
	return render_template("number.html")

@app.route("/number", methods=["POST"])
def get_name():
	if request.method == "POST":
		num = request.form['num']
	return render_template("result.html", func = isPrime,length = int(num))




