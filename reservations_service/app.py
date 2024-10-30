"""
    Reservations Service:
    User story 5-8
"""

from flask import Flask, jsonify, request
from reservations import select_all_items, find_item_by_id, add_new_item, delete_item_by_id, update_item, find_item_by_guest_id
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

app = Flask(__name__)

BASE_ADMIN_URL = 'http://admin_gateway:5000'

# Get all reservations
@app.route('/reservations', methods=['GET'])
def get_all_reservations():
    result = select_all_items()

    if result[0] == 200:
        reservations_items = []
        # Old way of adding guest and room type data - takes 1 min
        #for item in result[1]:
           # reservations_items.append(_add_guest_room_type_data(item))

        # New way with multithreading - takes 30 sec
        with ThreadPoolExecutor() as executor:
            # executed in a separate thread for each item in result[1]. This means that multiple _add_guest_room_type_data calls will be executed concurrently.
            futures = [executor.submit(_add_guest_room_type_data, item) for item in result[1]]
            # yields future objects as they complete. This allows you to process the results as soon as they are available, rather than waiting for all of them to complete.
            for future in as_completed(futures):
                reservations_items.append(future.result())

        result[1] = reservations_items

    return jsonify(result[1]), result[0]

# Get reservation by id
@app.route('/reservations/<int:id>', methods=['GET'])
def get_reservation_by_id(id):
    result = find_item_by_id(id)

    if result[0] == 200:
        result[1] = _add_guest_room_type_data(result[1])

    return jsonify(result[1]), result[0]

# Get reservation by guest id
@app.route('/reservations/guest/<int:id>', methods=['GET'])
def get_reservation_by_guest_id(id):
    result = find_item_by_guest_id(id)

    if result[0] == 200:
        result[1] = _add_guest_room_type_data(result[1])

    return jsonify(result[1]), result[0]

# Add a reservation
@app.route('/reservations', methods=['POST'])
def add_to_reservations():
    data = request.json
    
    reservation_item = _data_to_reservation_dict(data)

    result = add_new_item(reservation_item)
    return jsonify(result[1]), result[0]

# Remove reservation
@app.route('/reservations/<int:id>', methods=['DELETE'])
def delete_item_from_reservations(id):
    
    result = delete_item_by_id(id)
    return jsonify(result[1]), result[0]
    

# Update reservation
@app.route('/reservations/<int:id>', methods=['PATCH'])
def update_product_amount(id):
    data = request.json

    result = update_item(id, data)
    return jsonify(result[1]), result[0]

# Connect to room_type_service and get room type by id
def get_room_type_by_id(id):
    url = f'{BASE_ADMIN_URL}/room_types/{id}'
    req = requests.get(url)
    if req.status_code == 200:
        return req.json()
    
    return None

# Connect to guest service and get guest by id
def get_guest_by_id(id):
    url = f'{BASE_ADMIN_URL}/guests/{id}'
    req = requests.get(url)
    if req.status_code == 200:
        return req.json()
    
    return None

def _data_to_reservation_dict(data):
    return {
        "guest_id": int(data["guest_id"]) if data["guest_id"] else None,
        "room_type_id": int(data["room_type_id"]) if data["room_type_id"] else None,
        "days_rented": int(data["days_rented"]) if data["days_rented"] else None,
        "season": data["season"] if data["season"] else None,
        "price": int(data["price"]) if data["price"] else None
    }

def _add_guest_room_type_data(item):
        room_type = get_room_type_by_id(item["room_type_id"])
        guest = get_guest_by_id(item["guest_id"])

        if room_type and guest:
            return {
                "days_rented": item["days_rented"],
                "first_name": guest["first_name"],
                "family_name": guest["family_name"],
                "id": item["id"],
                "price": item["price"],
                "room_type": room_type["type"],
                "season": item["season"]
            }
        elif room_type:
            return {
                "days_rented": item["days_rented"],
                "guest_id": item["guest_id"],
                "id": item["id"],
                "price": item["price"],
                "room_type": room_type["type"],
                "season": item["season"]
            }
        elif guest:
            return {
                "days_rented": item["days_rented"],
                "first_name": guest["first_name"],
                "family_name": guest["family_name"],
                "id": item["id"],
                "price": item["price"],
                "room_type_id": item["room_type_id"],
                "season": item["season"]
            }
        else:
            return item

app.run(debug=True, host='0.0.0.0', port=5003)