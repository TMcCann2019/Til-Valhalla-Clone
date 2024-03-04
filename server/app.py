from flask import abort, make_response, request, session
from flask_restful import Resource
from werkzeug.exceptions import NotFound, Unauthorized

from config import app, db, api

from models import *

@app.route('/')
def index():
    return '<h1>Til Valhalla</h1>'

# @app.before_request
# def check_if_logged_in():
#     open_access_pages = ["signup", "login", "authorized", "products"]
#     if request.endpoint not in open_access_pages and not session.get('user_id'):
#         raise Unauthorized

class Products(Resource):
    def get(self):
        products = [p.to_dict() for p in Product.query.all()]
        response = make_response(products, 200)
        return response
    
    def post(self):
        data = request.get_json()
        try:
            new_product = Product(
                name=data['name'],
                description=data['description'],
                image=data['image'],
                price=data['price'],
                size=data['size'],
                color=data['color']
            )
        except ValueError as e:
            abort(422, e.args[0])

        db.session.add(new_product)
        db.session.commit()
        response = make_response(new_product.to_dict(), 201)
        return response
    
api.add_resource(Products, "/products")

class ProductByID(Resource):
    def get(self, id):
        product = Product.query.filter(product.id == id).first()
        if not product:
            raise NotFound
        product_dict = product.to_dict()
        response = make_response(product_dict, 200)
        return response

    def patch(self, id):
        product = Product.query.filter(product.id == id).first()
        if not product:
            raise NotFound

        for attr in request.form:
            setattr(product, attr, request.form[attr])

        product.price = int(request.form["price"])
        product.size = request.form["size"]
        product.color = request.form["color"]

        db.session.add(product)
        db.session.commit()

        product_dict = product.to_dict()

        response = make_response(product_dict, 200)
        return response

    def delete(self, id):
        product = Product.query.filter(product.id == id).first()
        if not product:
            raise NotFound
        db.session.delete(product)
        db.session.commit()

        response = make_response("", 204)
        return response

api.add_resource(ProductByID, "/products/<int:id>")

class Users(Resource):
    def post(self):
        data = request.get_json()
        try:
            new_user = User(
                username=data['username'],
                email=data['email'],
                password_hash=data['password']
            )
        except:
            abort(422, "Some of the values failed")

        db.session.add(new_user)
        db.session.commit()
        session['user_id'] = new_user.id
        response = make_response(new_user.to_dict(), 201)
        return response

api.add_resource(Users, "/users", "/signup")

@app.route('/login', methods=['POST'])
def login():
    user = User.query.filter_by(username=request.get_json()['username']).first()
    if user and user.authenticate(request.get_json()['password']):
        session["user_id"] = user.id
        return make_response(user.to_dict(), 200)
    else:
        raise Unauthorized
    
@app.route('/authorized')
def authorized():
    user = User.query.filter_by(id = session.get('user_id')).first()
    if not user:
        raise Unauthorized
    return make_response(user.to_dict(), 200)

@app.route('/logout', methods = ['DELETE'])
def logout():
    session['user_id'] = None
    return make_response({}, 204)

@app.errorhandler(NotFound)
def handle_not_found(e):
    response = make_response(
        {"message" : "Not Found: Sorry the resource you are looking for does not exist"}, 404
    )
    return response

@app.errorhandler(Unauthorized)
def handle_unauthorized(e):
    response = make_response(
        {"message": "Unauthorized: you must be logged in to make that request."},
        401,
    )
    return response

if __name__ == '__main__':
    app.run(port=5555, debug=True)