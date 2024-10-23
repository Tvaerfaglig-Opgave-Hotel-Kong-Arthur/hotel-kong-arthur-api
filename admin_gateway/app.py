'''
    Admin Gateway:
    For admin information from following microservices: reservations, drinks, room_type
'''

from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

BASE_DRINKS_URL = f'http://drinks_service:5002/drinks'
BASE_RESERVATIONS_URL = f'http://reservations_service:5003/reservations'
BASE_ROOM_TYPE_URL = f'http://room_type_service:5004/types' # TODO

@app.route('/', methods=['GET'])
def root():
    return {"message": "Welcome to the admin gateway"}, 200

# ------------------------------------------------------ DRINKS SERVICE
# Get drinks
@app.route('/drinks', methods=['GET'])
def get_drinks_items():
    url = f'{BASE_DRINKS_URL}'
    req = requests.get(url)
    return jsonify(req.json()), req.status_code

# Add new drink
@app.route('/drinks', methods=['POST'])
def add_to_drinks():
    data = request.json
    url = f'{BASE_DRINKS_URL}'
    req = requests.post(url, json=data)
    return jsonify(req.json()), req.status_code

# Remove drink
@app.route('/drinks/<int:id>', methods=['DELETE'])
def delete_item_from_drinks(id):
    url = f'{BASE_DRINKS_URL}/{id}'
    req = requests.post(url)
    return jsonify(req.json()), req.status_code

# Update drink
@app.route('/drinks/<int:id>', methods=['PATCH'])
def update_drink(id):
    data = request.json
    url = f'{BASE_DRINKS_URL}/{id}'
    req = requests.patch(url, json=data)
    return jsonify(req.json()), req.status_code

# ------------------------------------------------------ RESERVATIONS SERVICE
# Get reservations
@app.route('/reservations', methods=['GET'])
def get_reservations():
    url = f'{BASE_RESERVATIONS_URL}'
    req = requests.get(url)
    return jsonify(req.json()), req.status_code

# Get reservation by id
@app.route('/reservations/<int:id>', methods=['GET'])
def get_reservations(id):
    url = f'{BASE_RESERVATIONS_URL}/{id}'
    req = requests.get(url)
    return jsonify(req.json()), req.status_code

# Add new reservation
@app.route('/reservations', methods=['POST'])
def add_to_reservations():
    data = request.json
    url = f'{BASE_RESERVATIONS_URL}'
    req = requests.post(url, json=data)
    return jsonify(req.json()), req.status_code

# Remove reservation
@app.route('/reservations/<int:id>', methods=['DELETE'])
def delete_reservation(id):
    url = f'{BASE_RESERVATIONS_URL}/{id}'
    req = requests.post(url)
    return jsonify(req.json()), req.status_code

# Update reservation
@app.route('/reservations/<int:id>', methods=['PATCH'])
def update_reservation(id):
    data = request.json
    url = f'{BASE_RESERVATIONS_URL}/{id}'
    req = requests.patch(url, json=data)
    return jsonify(req.json()), req.status_code

# ------------------------------------------------------ ROOM TYPE SERVICE
# Get room types
@app.route('/types', methods=['GET'])
def get_room_types():
    url = f'{BASE_ROOM_TYPE_URL}'
    req = requests.get(url)
    return jsonify(req.json()), req.status_code

# Add new room type
@app.route('/types', methods=['POST'])
def add_to_room_types():
    data = request.json
    url = f'{BASE_ROOM_TYPE_URL}'
    req = requests.post(url, json=data)
    return jsonify(req.json()), req.status_code

# Remove room type
@app.route('/types/<int:id>', methods=['DELETE'])
def delete_item_from_room_types(id):
    url = f'{BASE_ROOM_TYPE_URL}/{id}'
    req = requests.post(url)
    return jsonify(req.json()), req.status_code

# Update room type
@app.route('/types/<int:id>', methods=['PATCH'])
def update_room_type(id):
    data = request.json
    url = f'{BASE_ROOM_TYPE_URL}/{id}'
    req = requests.patch(url, json=data)
    return jsonify(req.json()), req.status_code


app.run(debug=True, host='0.0.0.0', port=5000)