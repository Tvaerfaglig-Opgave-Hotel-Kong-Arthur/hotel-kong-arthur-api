'''
    Public Gateway:
    For seeing public information like drinks, room types, and their prices
'''

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def all():
    return
