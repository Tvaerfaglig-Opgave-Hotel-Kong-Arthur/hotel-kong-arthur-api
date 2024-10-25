"""
    Reservations Service:
    User story 5-8
"""

from flask import Flask, jsonify, request
from reservations import select_all_items, find_item_by_id, add_new_item, delete_item_by_id, update_item
import requests

app = Flask(__name__)

# Get all reservations
@app.route('/reservations', methods=['GET'])
def get_all_reservations():
    result = select_all_items()

    '''if result[0] == 200: TODO
        reservations_items = []
        for item in result[1]:
            product = get_room_type_by_id(item["product_id"])
            if product:
                reservations_items.append({
                    "id": item["id"],
                    "product": product[0],
                    "amount": item["amount"]
                })

        result[1] = reservations_items
    '''

    return jsonify(result[1]), result[0]

# Get reservation by id
@app.route('/reservations/<int:id>', methods=['GET'])
def get_reservation_by_id(id):
    result = find_item_by_id(id)

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

def get_room_type_by_id(id): # TODO
    url = f'http://product_catalog_service:5000/products/{id}'
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


app.run(debug=True, host='0.0.0.0', port=5003)