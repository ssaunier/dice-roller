import random
from flask import Flask, jsonify
app = Flask(__name__)

import os

sentry_dsn = os.getenv('SENTRY_DSN', None)
if sentry_dsn:
    import sentry_sdk
    from sentry_sdk.integrations.flask import FlaskIntegration

    sentry_sdk.init(
        sentry_dsn,
        integrations=[FlaskIntegration()]
    )

@app.route('/')
def home():
    return jsonify({ 'roll': random.randint(1, 12) })

@app.route('/error')
def erro():
    return jsonify({ 'roll': 1 / 0 })
