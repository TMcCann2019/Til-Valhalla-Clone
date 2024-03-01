#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import abort, make_response, request, session
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
    return '<h1>Til Valhalla</h1>'

class Products(Resource):
    def get(self):
        products = [p.to_dict() for p in Product.query.all()]
        response = make_response(products, 200)
        return response
    
    def post(self):
        data = request.get_json()
        try:
            new_product = Product(**data)
        except ValueError as e:
            abort(400, e.args[0])

        db.session.add(new_product)
        db.session.commit()
        response = make_response(new_product.to_dict(), 201)
        return response
    
api.add_resource(Products, "/products")

class Users(Resource):
    def post(self):
        data = request.get_json()
        try:
            new_user = User(**data)
        except ValueError as e:
            abort(422, e.args[0])

        db.session.add(new_user)
        db.session.commit()
        session['user_id'] = new_user.id
        response = make_response(new_user.to_dict(), 201)
        return response

api.add_resource(Users, "/users", "/signup")

@app.route('/login', methods=['POST'])
def login():
    user = User.query.filter_by(username=request.get_json()['username']).first()
    if not user:
        abort(404, "User not found")
    session["user_id"] = user.id
    return make_response(user.to_dict(), 200)

if __name__ == '__main__':
    app.run(port=5555, debug=True)