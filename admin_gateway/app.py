'''
    Admin Gateway:
    For admin information from following microservices: reservations, drinks, room_type
'''

from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

BASE_PCS_URL = f'http://product_catalog_service:5000/products'
BASE_CS_URL = f'http://cart_service:5001/cart'

@app.route('/', methods=['GET'])
def all():
    return

# ------------------------------------------------------ CART SERVICE
# Get cart items
@app.route('/cart', methods=['GET'])
def get_cart_items():
    url = f'{BASE_CS_URL}'
    req = requests.get(url)
    return jsonify(req.json()), req.status_code

app.run(debug=True, host='0.0.0.0', port=5000)