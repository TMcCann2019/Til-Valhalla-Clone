#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import abort, jsonify, make_response, request, session
from flask_restful import Resource
from werkzeug.exceptions import NotFound, Unauthorized

# Local imports
from config import app, db, api
# Add your model imports
from models import *

app.secret_key = "enter secret key here"

# Views go here!
@app.route('/')
def index():
    return '<h1>Project Server</h1>'


if __name__ == '__main__':
    app.run(port=5555, debug=True)

