from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from util import load_saved_artifacts, get_location_names, get_estimated_price
app = Flask(__name__)
CORS(app)
 
load_saved_artifacts()

@app.route('/', methods=['GET'])
def Home():
    return " Hello from api!! ,Have fun"

@app.route('/get_location_names', methods=['GET'])
def get_location_names_fun():
    locations = get_location_names()
    print(locations)
    response = jsonify({
        'locations': locations
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


@app.route('/predict_home_price', methods=['GET', 'POST'])
def predict_home_price():
    total_sqft = float(request.json['total_sqft'])
    location = request.json['location']
    bhk = int(request.json['bhk'])
    bath = int(request.json['bath'])

    response = jsonify({
        'estimated_price': get_estimated_price(location, total_sqft, bhk, bath)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


if __name__ == '__main__':
   
    app.run(debug=True)
    
