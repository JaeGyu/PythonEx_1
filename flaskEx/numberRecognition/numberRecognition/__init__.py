from flask import Flask, request, jsonify
from flask_cors import CORS
import json 
import base64 
import numpy as np
from PIL import Image
import tensorflow as tf
import array

app = Flask(__name__)
CORS(app)

#다른 모듈로 뺄 것
def convert_to_alpha_list(decode_str):
    img = Image.frombytes(data=decode_str, size=(250, 250), mode='RGBA')
    pixels = img.resize((28, 28)).tobytes("raw", "A")
    print(pixels)
    return np.array([pixel / 255 for pixel in pixels]).reshape(1,784)


#다른 모듈로 뺄 것
def predict_to_number(img_arr):
	X = tf.placeholder(dtype=tf.float32, shape=[None, 784])
	# Y = tf.placeholder(dtype=tf.float32, shape=[None, 10])

	W1 = tf.Variable(tf.random_normal(shape=[784, 256], stddev=0.01), name="w1val")
	L1 = tf.nn.relu(tf.matmul(X, W1))

	W2 = tf.Variable(tf.random_normal(shape=[256, 256], stddev=0.01), name="w2val")
	L2 = tf.nn.relu(tf.matmul(L1, W2))

	W3 = tf.Variable(tf.random_normal([256, 10], stddev=0.01), name="w3val")
	model = tf.matmul(L2, W3)

	saver = tf.train.Saver({"w1val": W1, "w2val": W2, "w3val": W3})

	with tf.Session() as sess:
		saver.restore(sess, "./numberRecognition/static/tf_model/mnist")
		predict = sess.run([model], feed_dict={X: img_arr})
		predict = np.array(predict)
		result = np.argmax(predict[0], axis=1)
		print("result : ", result)
		return result


@app.route('/')
def numberRecognition():
	return 'hello world'


@app.route("/api/predict", methods=['POST'])
def get_number():
    req_data = request.data.decode('utf-8')
    json_obj = json.loads(req_data)
    img_str = json_obj['img']
	
    print("넘어온 배열의 길이 : ", len(img_str))
	
    bt_str = array.array('B', img_str).tostring()
    result = predict_to_number(convert_to_alpha_list(bt_str))
	
    print("예측한 결과는 : ", result[0])
	
    return str(result[0])

