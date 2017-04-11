from flask import Flask, jsonify, render_template
from subprocess import call
from flask_socketio import SocketIO, send


app = Flask(__name__)
app.secret_key = "mysecret"

socket_io = SocketIO(app)

@app.route('/')
def socketIOEx():
	return 'hello world'

@app.route("/chat")
def chatting():
	return render_template("chat2.html")

@socket_io.on("message")
def request(message):
	print("message : " + message)
	to_client = dict()
	if message == "new_connect":
		to_client["message"] = "사로운 유저가 난입했다."
		to_client["type"] = "connect"
	else:
		to_client["message"] = message
		to_client["type"] = "nomal"
	send(to_client, broadcast = True)


