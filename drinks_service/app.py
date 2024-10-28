"""
    Drinks Service:
    User story 1-4
"""

from flask import Flask, jsonify, request
from data import select_all_drinks, drinks_category, drinks_prices, add_new_drink

app = Flask(__name__)

# Get drinks items
@app.route('/drinks', methods=['GET'])
def get_drinks():
    
    result = select_all_drinks()
    return jsonify(result[1]), result[0]


# Get drinks order by category
@app.route('/drinks/<category>', methods=['GET'])
def get_drinks_sorted_by_category(category):
    status,data = drinks_category(category=category)

    return jsonify(data), status

# Get the drinks prices in a descending order, so you can see the highst price first
@app.route('/drinks/prices', methods=['GET'])
def get_drinks_prices():
    status, data = drinks_prices()

    return jsonify(data), status

# Add new drinks to the database
@app.route('/drinks', methods=['POST'])
def add_new_drinks():
    data = request.get_json()

    drink_name = data.get("drink_name")
    category = data.get("category")
    price = data.get("price")
    units_sold = data.get("units_sold")

    if not all ([drink_name, category, price, units_sold]):
        return jsonify({"error": "All fields are required."}), 400
    
    status, response_data = add_new_drink(drink_name, category, price, units_sold)

    return jsonify(response_data), status

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5002)
