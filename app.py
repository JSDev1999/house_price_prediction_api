from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import util

app = Flask(__name__)
CORS(app)

import numpy
print(numpy.version.version)
@app.route('/', methods=['GET'])
def Home():
    return " Hello from api!! ,Have fun"

@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
 #   response.headers.add('Access-Control-Allow-Origin', '*')

    return response


@app.route('/predict_home_price', methods=['GET', 'POST'])
def predict_home_price():
    total_sqft = float(request.json['total_sqft'])
    location = request.json['location']
    bhk = int(request.json['bhk'])
    bath = int(request.json['bath'])

    #print("aaaa", total_sqft, location, bhk, bath)

    response = jsonify({
        'estimated_price': util.get_estimated_price(location, total_sqft, bhk, bath)
    })
  #  response.headers.add('Access-Control-Allow-Origin', '*')

    return response


if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run()
