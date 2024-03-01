from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates
from sqlalchemy.ext.hybrid import hybrid_property

from config import db, bcrypt

# Models go here!
class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(10), unique=True, nullable=False)
    email = db.Column(db.String(25), unique=True, nullable=False)
    _password_hash = db.Column(db.String)
    orders = db.relationship('Order', backref='user', cascade = ("all, delete"))

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
    
    @hybrid_property
    def password_hash(self):
        return self._password_hash
    
    @password_hash.setter
    def password_hash(self, password):
        password_hash = bcrypt.generate_password_hash(password.encode('utf-8'))
        self._password_hash = password_hash.decode('utf-8')

    def authenticate(self, password):
        return bcrypt.check_password_hash(self._password_hash, password.encode('utf-8'))
    
    def __repr__(self):
        return f'<Username: {self.username}, Email: {self.email}'

class Order(db.Model, SerializerMixin):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    status = db.Column(db.String)
    total = db.Column(db.Float)

    serialize_rules = ("-users.orders",)

    @validates('status')
    def validate_status(self, key, value):
        valid_status = ["In Cart", "Processing", "Shipped", "Ordered"]
        if value not in valid_status:
            raise ValueError("Invalid order status")
        return value
    
    def __repr__(self):
        return f'<Status: {self.status}'

class OrderItem(db.Model, SerializerMixin):
    __tablename__ = 'order_items'

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'))
    quantity = db.Column(db.Integer)
    sub_total = db.Column(db.Float)
    products = db.relationship('Product', backref='order_item', cascade = ("all, delete"))

    serialize_rules = ("-products.order_items",)

    def __repr__(self):
        return f'<Quantity: {self.quantity}'

class Product(db.Model, SerializerMixin):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    image = db.Column(db.String)
    price = db.Column(db.Integer)
    size = db.Column(db.String)
    color = db.Column(db.String)
    order_items = db.relationship('OrderItem', backref='product', cascade = ("all, delete"))

    serialize_rules = ("-order_items.products",)

    @validates('name')
    def validate_name(self, key, value):
        if Product.query.filter_by(name=value).first() is not None:
            raise ValueError("Product name already taken")
        return value
    
    # @validates('image')
    # def validate_image(self, key, image_path):
    #     if '.jpg' not in image_path or '.jpeg' not in image_path or '.png' not in image_path:
    #         raise ValueError("Invalid image format")
    #     return image_path
    
    def __repr__(self):
        return f'<Name: {self.name}, Description: {self.description}, Price: {self.price}, Size: {self.size}, Color: {self.color}'