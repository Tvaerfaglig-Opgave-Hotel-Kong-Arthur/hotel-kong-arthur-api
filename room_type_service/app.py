"""
    Drinks Service:
    User story 1-4
"""

from flask import Flask, jsonify, request
from room_type_service.db import select_all_items, find_item_by_id, add_new_item, delete_item_by_id, update_amount

app = Flask(__name__)

# ---------- EXAMPLE
# Get cart items
@app.route('/cart', methods=['GET'])
def get_cart_items():
    result = select_all_items()

    if result[0] == 200:
        cart_items = []
        for item in result[1]:
            product = get_product_by_id(item["product_id"])
            if product:
                cart_items.append({
                    "id": item["id"],
                    "product": product[0],
                    "amount": item["amount"]
                })

        result[1] = cart_items


    return jsonify(result[1]), result[0]

