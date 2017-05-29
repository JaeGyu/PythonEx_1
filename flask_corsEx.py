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

@app.route("/")
def helloWorld():
  return "Hello, cross-origin-world!"

# @app.after_request
# def add_header(r):
#     """
#     Add headers to both force latest IE rendering engine or Chrome Frame,
#     and also to cache the rendered page for 10 minutes.
#     """
#     r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
#     r.headers["Pragma"] = "no-cache"
#     r.headers["Expires"] = "0"
#     r.headers['Cache-Control'] = 'public, max-age=0'
#     return r

@app.route("/api/image3", methods=['POST'])
def imagePro():
    req_data = request.data.decode('utf-8')
    json_obj = json.loads(req_data)
    img_str = json_obj['img'].split(',')[-1]
    decode_str = base64.b64decode(img_str)
    print(decode_str)

    with open('temp.png','wb') as temp:
        temp.write(decode_str)

    im = Image.open("./temp.png")
    print("image size : ",im.size)

    img2 = im.resize((28,28))
    img2.save("./temp28x28.png")

    return 'ok'

def convert_to_alpha_list(decode_str):
    img = Image.frombytes(data=decode_str, size=(250,250), mode='RGBA')
    # pixels = Image.open("./temp.png").resize((28,28)).tobytes("raw","A")
    pixels = img.resize((28,28)).tobytes("raw","A")
    return np.array([pixel / 255 for pixel in pixels]).reshape(1,784)


def predict_to_number(img_arr):
    X = tf.placeholder(dtype=tf.float32, shape=[None, 784])
    Y = tf.placeholder(dtype=tf.float32, shape=[None, 10])
    
    W1 = tf.Variable(tf.random_normal(shape=[784, 256], stddev=0.01), name="w1val")
    L1 = tf.nn.relu(tf.matmul(X, W1))
    
    W2 = tf.Variable(tf.random_normal(shape=[256, 256], stddev=0.01), name="w2val")
    L2 = tf.nn.relu(tf.matmul(L1, W2))
    
    W3 = tf.Variable(tf.random_normal([256, 10], stddev=0.01), name="w3val")
    model = tf.matmul(L2, W3)
    
    saver = tf.train.Saver({"w1val":W1, "w2val":W2, "w3val":W3})
    
    with tf.Session() as sess:
        saver.restore(sess, "./number_model/mnist")
        predict = sess.run([ model ], feed_dict = {X : img_arr})
        predict = np.array(predict)
        result = np.argmax(predict[0], axis=1)
        print("result : ", result)
        return result


"""
1) 클라이언트에서 넘어온 이미지를 28*28로 변환한다.
2) 변환한 이미지 중 alpha값만 추출해서 리스트화 한다.
3) 변환한 alpha값을 0~1사이의 값으로 스케일링한다.
4) reshape(1,748)을 하여 텐서플로 모델에 질의 한다.
"""
@app.route("/api/predict", methods=['POST'])
def get_number():
    req_data = request.data.decode('utf-8')
    json_obj = json.loads(req_data)
    img_str = json_obj['img']
    print("넘어온 배열의 길이 : ",len(img_str))
    bt_str = array.array('B', img_str).tostring()
    ll = convert_to_alpha_list(bt_str)
    result = predict_to_number(ll)

    print("예측한 결과는 : ", result[0])
    return str(result[0])


@app.route("/api/image2", methods=['POST'])
def imagePross():
    req_data = request.data.decode('utf-8')
    json_obj = json.loads(req_data)
    img_str = json_obj['img'].split(',')[-1]
    decode_str = base64.b64decode(img_str)
    l = [int(i) for i in decode_str]

    print(l)
    return jsonify(
      img = l
    )

@app.route("/api/image", methods=['POST'])
def imagePros():
    req_data = request.data.decode('utf-8')
    json_obj = json.loads(req_data)
    list_img_str = json_obj['img'].split(',')
    print(list_img_str[0:10])
    return "ok"

if __name__ == "__main__":
    app.run(debug=True)