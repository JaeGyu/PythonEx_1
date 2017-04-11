from socketIOEx import app, socket_io
if __name__ == '__main__':
	#app.run(host='0.0.0.0')
	socket_io.run(app, debug = True, port=5000)