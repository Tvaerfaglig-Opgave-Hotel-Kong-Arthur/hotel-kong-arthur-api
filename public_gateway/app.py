'''
    Public Gateway:
    For seeing public information like drinks, room types, and their prices
'''

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def all():
    return

app.run(debug=True, host='0.0.0.0', port=5001)