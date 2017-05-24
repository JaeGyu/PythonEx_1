from flask import Flask, request, jsonify
from flask_cors import CORS
import json 
import base64 
import numpy as np
from PIL import Image


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