from flask import abort, make_response, request, session, render_template
from flask_restful import Resource
from werkzeug.exceptions import NotFound, Unauthorized

from config import app, db, api

from models import *

@app.route('/')
@app.route('/<int:id>')
def index(id=0):
    return render_template("index.html")

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
        product = Product.query.filter(Product.id == id).first()
        if not product:
            raise NotFound
        product_dict = product.to_dict()
        response = make_response(product_dict, 200)
        return response

    def patch(self, id):
        product = Product.query.filter(Product.id == id).first()
        if not product:
            raise NotFound

        for attr in request.get_json():
            setattr(product, attr, request.get_json()[attr])

        db.session.add(product)
        db.session.commit()

        product_dict = product.to_dict()

        response = make_response(product_dict, 200)
        return response

    def delete(self, id):
        product = Product.query.filter(Product.id == id).first()
        if not product:
            raise NotFound
        db.session.delete(product)
        db.session.commit()

        response = make_response("", 204)
        return response

api.add_resource(ProductByID, "/products/<int:id>")

# class Orders(Resource):
#     def get(self):
#         orders = [o.to_dict() for o in Order.query.all()]
#         response = make_response(orders, 200)
#         return response
    
#     def post(self):
#         data = request.get_json()
#         try:
#             new_order = Order(
#                 user_id=data['user_id'],
#                 status=data['status'],
#                 total=data['total']
#             )
#         except ValueError as e:
#             abort(422, e.args[0])

#         db.session.add(new_order)
#         db.session.commit()
#         response = make_response(new_order.to_dict(), 201)
#         return response
    
# api.add_resource(Orders, "/cart")

class OrderItems(Resource):
    def get(self):
        order_items = [o.to_dict() for o in OrderItem.query.all()]
        response = make_response(order_items, 200)
        return response
    
    def post(self):
        data = request.get_json()
        try:
            new_order_item = OrderItem(
                product_id=data['product_id'],
                # order_id=data['order_id'],
                quantity=data['quantity'],
                sub_total=data['sub_total']
            )
        except ValueError as e:
            abort(422, e.args[0])

        db.session.add(new_order_item)
        db.session.commit()
        response = make_response(new_order_item.to_dict(), 201)
        return response
    
api.add_resource(OrderItems, "/cart")

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
    user_data = request.get_json()
    user = User.query.filter_by(username=user_data['username']).first()
    if user and user.authenticate(user_data['password']):
        session["user_id"] = user.id
        existing_order = Order.query.filter_by(user_id=user.id, status="In Cart").first()
        if not existing_order:
            new_order = Order(
                user_id=user.id,
                status="In Cart",
                total=0
            )
            db.session.add(new_order)
            db.session.commit()
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