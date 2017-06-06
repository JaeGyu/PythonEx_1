from flask import Flask, request
from flask_cors import CORS
import json 
import array
from numberRecognition.predict import Predict
from numberRecognition.converter import Converter

app = Flask(__name__)
CORS(app)

p = Predict()
c = Converter()

@app.route('/')
def numberRecognition():
    return 'OK!'


@app.route("/api/predict", methods=['POST'])
def get_number():
    req_data = request.data.decode('utf-8')
    json_obj = json.loads(req_data)
    img_str = json_obj['img']
	
    bt_str = array.array('B', img_str).tostring()
    result = p.predict(c.convert_to_alpha_list(bt_str))
	
    print("예측한 결과는 : ", result[0])
	
    return str(result[0])

