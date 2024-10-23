'''
    Admin Gateway:
    For admin information from following microservices: reservations, drinks, room_type
'''

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def all():
    return
