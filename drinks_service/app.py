"""
    Drinks Service:
    User story 1-4
"""

from flask import Flask, jsonify, request
from data import select_all_drinks

app = Flask(__name__)

# Get drinks items
@app.route('/drinks', methods=['GET'])
def get_drinks():
    
    data = select_all_drinks()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5002)