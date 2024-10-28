"""
    Guests Service:
"""

from flask import Flask, jsonify, request
from data import select_all_items, find_item_by_id, add_new_item, delete_item_by_id, update_item

app = Flask(__name__)

# Get all guests
@app.route('/guests', methods=['GET'])
def get_all_guests():
    result = select_all_items()

    return jsonify(result[1]), result[0]

# Get guest by id
@app.route('/guests/<int:id>', methods=['GET'])
def get_guest_by_id(id):
    result = find_item_by_id(id)

    return jsonify(result[1]), result[0]

# Add a guest
@app.route('/guests', methods=['POST'])
def add_to_guests():
    data = request.json
    
    guest_item = _data_to_guest_dict(data)

    result = add_new_item(guest_item)
    return jsonify(result[1]), result[0]

# Remove guest
@app.route('/guests/<int:id>', methods=['DELETE'])
def delete_item_from_guests(id):
    
    result = delete_item_by_id(id)
    return jsonify(result[1]), result[0]
    

# Update guest
@app.route('/guests/<int:id>', methods=['PATCH'])
def update_product_amount(id):
    data = request.json

    result = update_item(id, data)
    return jsonify(result[1]), result[0]

def _data_to_guest_dict(data):
    return {
        "first_name": data["first_name"] if data["first_name"] else None,
        "family_name": data["family_name"] if data["family_name"] else None,
        "country": data["country"] if data["country"] else None,
    }


app.run(debug=True, host='0.0.0.0', port=5005)