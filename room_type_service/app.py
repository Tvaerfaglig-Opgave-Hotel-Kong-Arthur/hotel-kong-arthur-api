"""
    Room_type Service:
    User story ****
"""

from flask import Flask, jsonify, request
from room_type import select_all_items, find_item_by_id, delete_item_by_id, add_new_item, update_item 

app = Flask(__name__)


# Get alle info
@app.route('/room_types', methods=['GET'])
def get_all_room_types():
    result = select_all_items()

    return jsonify(result[1]), result[0]

# FInd by id
@app.route('/room_types/<int:id>', methods=['GET'])
def get_room_by_id(id):
    result = find_item_by_id(id)

    return jsonify(result[1]), result[0]


@app.route('/room_types', methods=['POST'])
def add_to_room_types():
    data = request.json

    room_type_item = _data_to_room_types_dict(data)

    result = add_new_item(room_type_item)
    
    return jsonify(result[1]), result[0]

# Delete item by id
@app.route('/room_types/<int:id>', methods=['DELETE'])
def delete_item_from_room_types(id):
    
    result = delete_item_by_id(id)
    return jsonify(result[1]), result[0]

#Update room type
@app.route('/room_types/<int:id>', methods=['PATCH'])
def update_room_types(id):
    data = request.json

    result = update_item(id, data)
    return jsonify(result[1]), result[0]


def _data_to_room_types_dict(data):
    return {
        "type": data["type"] if data["type"] else None,
        "low": int(data["low"]) if data["low"] else None,
        "mid": int(data["mid"]) if data["mid"] else None,
        "high": int(data["high"]) if data["high"] else None,
    }

# Run the Flask app on port 5004 and allow external access
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5004)