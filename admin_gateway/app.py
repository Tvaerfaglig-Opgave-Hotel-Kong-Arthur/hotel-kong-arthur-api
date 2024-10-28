'''
    Admin Gateway:
    For admin information from following microservices: reservations, drinks, room_type
'''

from flask import Flask, jsonify, request, Response
import requests
import csv
import io

app = Flask(__name__)

BASE_DRINKS_URL = f'http://drinks_service:5002/drinks'
BASE_RESERVATIONS_URL = f'http://reservations_service:5003/reservations'
BASE_ROOM_TYPE_URL = f'http://room_type_service:5004/room_types'
BASE_GUESTS_URL = f'http://guests_service:5005/guests'

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

@app.route('/drinks/csv', methods=['GET'])
def get_drinks_items_csv():
    url = f'{BASE_DRINKS_URL}'
    req = requests.get(url)
    
    data = _data_to_csv(req.json())

    if isinstance(data, str):
        return Response(data, mimetype='text/csv', headers={"Content-Disposition": "attachment;filename=data.csv"})
    else:
        return jsonify(data[1]), data[0]

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

@app.route('/reservations/csv', methods=['GET'])
def get_reservations_csv():
    url = f'{BASE_RESERVATIONS_URL}'
    req = requests.get(url)

    data = _data_to_csv(req.json())

    if isinstance(data, str):
        return Response(data, mimetype='text/csv', headers={"Content-Disposition": "attachment;filename=data.csv"})
    else:
        return jsonify(data[1]), data[0]

# Get reservation by id
@app.route('/reservations/<int:id>', methods=['GET'])
def get_reservations_by_id(id):
    url = f'{BASE_RESERVATIONS_URL}/{id}'
    req = requests.get(url)
    return jsonify(req.json()), req.status_code

# Get reservation by guest id
@app.route('/reservations/guest/<int:id>', methods=['GET'])
def get_reservations_by_guest_id(id):
    url = f'{BASE_RESERVATIONS_URL}/guest/{id}'
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
@app.route('/room_types', methods=['GET'])
def get_room_types():
    url = f'{BASE_ROOM_TYPE_URL}'
    req = requests.get(url)
    return jsonify(req.json()), req.status_code

@app.route('/room_types/csv', methods=['GET'])
def get_room_types_csv():
    url = f'{BASE_ROOM_TYPE_URL}'
    req = requests.get(url)
    
    data = _data_to_csv(req.json())

    if isinstance(data, str):
        return Response(data, mimetype='text/csv', headers={"Content-Disposition": "attachment;filename=data.csv"})
    else:
        return jsonify(data[1]), data[0]

# Add new room type
@app.route('/room_types', methods=['POST'])
def add_to_room_types():
    data = request.json
    url = f'{BASE_ROOM_TYPE_URL}'
    req = requests.post(url, json=data)
    return jsonify(req.json()), req.status_code

# Remove room type
@app.route('/room_types/<int:id>', methods=['DELETE'])
def delete_item_from_room_types(id):
    url = f'{BASE_ROOM_TYPE_URL}/{id}'
    req = requests.post(url)
    return jsonify(req.json()), req.status_code

# Update room type
@app.route('/room_types/<int:id>', methods=['PATCH'])
def update_room_type(id):
    data = request.json
    url = f'{BASE_ROOM_TYPE_URL}/{id}'
    req = requests.patch(url, json=data)
    return jsonify(req.json()), req.status_code

# ------------------------------------------------------ GUESTS SERVICE
# Get guests
@app.route('/guests', methods=['GET'])
def get_room_types():
    url = f'{BASE_GUESTS_URL}'
    req = requests.get(url)
    return jsonify(req.json()), req.status_code

@app.route('/guests/csv', methods=['GET'])
def get_guests_csv():
    url = f'{BASE_GUESTS_URL}'
    req = requests.get(url)
    
    data = _data_to_csv(req.json())

    if isinstance(data, str):
        return Response(data, mimetype='text/csv', headers={"Content-Disposition": "attachment;filename=data.csv"})
    else:
        return jsonify(data[1]), data[0]

# Add new guest
@app.route('/guests', methods=['POST'])
def add_to_guests():
    data = request.json
    url = f'{BASE_GUESTS_URL}'
    req = requests.post(url, json=data)
    return jsonify(req.json()), req.status_code

# Remove guest
@app.route('/guests/<int:id>', methods=['DELETE'])
def delete_item_from_guests(id):
    url = f'{BASE_GUESTS_URL}/{id}'
    req = requests.post(url)
    return jsonify(req.json()), req.status_code

# Update guest
@app.route('/guests/<int:id>', methods=['PATCH'])
def update_guests(id):
    data = request.json
    url = f'{BASE_GUESTS_URL}/{id}'
    req = requests.patch(url, json=data)
    return jsonify(req.json()), req.status_code

# ------------------------------------------------------ Data to CSV function
def _data_to_csv(data):

    if not isinstance(data, list):
        return [500, {"error": 'Data is not a list'}]
    
    try:
        # Create a string buffer to hold the CSV data
        output = io.StringIO()

        writer = csv.DictWriter(output, fieldnames=data[0].keys())
        writer.writeheader()
        for dictionary in data:
            writer.writerow(dictionary)
        
        # Move to the beginning of the StringIO buffer
        output.seek(0)

        # Return all the data written to the buffer as a string
        return output.getvalue()

    except Exception as e:
        return [500, {"error": str(e)}]


app.run(debug=True, host='0.0.0.0', port=5000)