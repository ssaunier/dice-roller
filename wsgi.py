import random
from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({ 'roll': random.randint(1, 12) })
