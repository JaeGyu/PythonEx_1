from numberRecognition import app
from numberRecognition import predict

if __name__ == '__main__':
	predict.test()
	app.run(host='0.0.0.0')