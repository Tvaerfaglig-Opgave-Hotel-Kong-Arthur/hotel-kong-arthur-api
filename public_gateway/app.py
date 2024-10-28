'''
    Public Gateway:
    For seeing public information like drinks, room types, and their prices
'''

from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

BASE_DRINKS_URL = f'http://drinks_service:5002/drinks'
BASE_ROOM_TYPE_URL = f'http://room_type_service:5004/room_types'

@app.route('/', methods=['GET'])
def root():
    return {"message": "Welcome to the public gateway"}, 200

# ------------------------------------------------------ DRINKS SERVICE
# Get drinks
# TODO GET ONLY DRINKS AND THEIR PRICES
@app.route('/drinks', methods=['GET'])
def get_drinks_items():
    url = f'{BASE_DRINKS_URL}/prices'
    req = requests.get(url)
    return jsonify(req.json()), req.status_code

# ------------------------------------------------------ ROOM TYPE SERVICE
# Get room types
@app.route('/room_types', methods=['GET'])
def get_room_types():
    url = f'{BASE_ROOM_TYPE_URL}'
    req = requests.get(url)
    return jsonify(req.json()), req.status_code


app.run(debug=True, host='0.0.0.0', port=5001)