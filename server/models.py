from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import validates

from config import db

# Models go here!
class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(10), unique=True, nullable=False)
    email = db.Column(db.String(25), unique=True, nullable=False)
    _password = db.Column(db.String(100), nullable=False)
    orders = db.relationship('Order', backref='user')

    serialize_rules = ("-orders.user",)

    @validates('username')
    def validate_username(self, key, value):
        if User.query.filter_by(username=value).first() is not None:
            raise ValueError("Username already taken")
        return value
    
    @validates('email')
    def validate_email(self, key, value):
        if User.query.filter_by(email=value).first() is not None:
            raise ValueError("Email is already associated with an account")
        return value
    
    def __repr__(self):
        return f'<Username: {self.username}, Email: {self.email}'

class Order(db.Model, SerializerMixin):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    status = db.Column(db.String)
    total = db.Column(db.Float)
    users = db.relationship('User', backref='orders')

    serialize_rules = ("-users.orders",)

    @validates('status')
    def validate_status(self, key, value):
        valid_status = ["In Cart", "Processing", "Shipped", "Ordered"]
        if value not in valid_status:
            raise ValueError("Invalid order status")
        return value

class OrderItem(db.Model, SerializerMixin):
    __tablename__ = 'order_items'

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'))
    quantity = db.Column(db.Integer)
    sub_total = db.Column(db.Float)
    products = db.relationship('Product', backref='order_item')

    serialize_rules = ("-products.order_items",)

class Product(db.Model, SerializerMixin):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    price = db.Column(db.Float)
    size = db.Column(db.String)
    color = db.Column(db.String)
    order_items = db.relationship('OrderItem', backref='product')

    serialize_rules = ("-order_items.products",)

    @validates('name')
    def validate_name(self, key, value):
        if Product.query.filter_by(name=value).first() is not None:
            raise ValueError("Product name already taken")
        return value