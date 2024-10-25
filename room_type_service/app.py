"""
    Room_type Service:
    User story ****
"""

from flask import Flask, jsonify, request
from room_type import select_all_items, find_item_by_id, delete_item_by_id, add_new_item, update_item 

app = Flask(__name__)

# ---------- EXAMPLE
# Get alle info
@app.route('/room_type', methods=['GET'])
def get_all_room_types():
    result = select_all_items()

    return jsonify(result[1]), result[0]

# Run the Flask app on port 5004 and allow external access
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5004)