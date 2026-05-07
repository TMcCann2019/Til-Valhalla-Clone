#!/usr/bin/env python3

from app import app, db
from models import Product, User

PRODUCTS = [
    {
        "name": "Let there be military police",
        "description": "Military themed shirt",
        "image": "https://image.spreadshirtmedia.com/image-server/v1/mp/products/T812A2MPA1664PT17X11Y16D13097815S59/views/2,width=800,height=800,appearanceId=2,backgroundColor=F2F2F2,modelId=127,crop=list,version=1560425676,modelImageVersion=1554715238/military-police-military-police-mens-premium-t-shirt.jpg",
        "price": 25,
        "size": "Large",
        "color": "black and white"
    },
    {
        "name": "stay low, go fast",
        "description": "Tactical military shirt",
        "image": "https://ih1.redbubble.net/image.361537736.3970/ssrco,classic_tee,flatlay,101010:01c5ca27c6,front,wide_portrait,750x1000.u2.jpg",
        "price": 20,
        "size": "Large",
        "color": "black, gold and white"
    },
    {
        "name": "Never quit",
        "description": "Motivational military apparel",
        "image": "https://i.pinimg.com/originals/01/c7/6c/01c76c83bf5d36fb17377f1836dc08a5.jpg",
        "price": 30,
        "size": "Medium",
        "color": "black and gold"
    }
]

USER = {
    "username": "TMcCann2019",
    "password_hash": "Rio123",
    "email": "timothysmccann@gmail.com"
}

if __name__ == "__main__":

    with app.app_context():

        print("Deleting old data...")

        db.session.execute(db.text("DELETE FROM order_items"))
        db.session.execute(db.text("DELETE FROM orders"))
        db.session.execute(db.text("DELETE FROM users"))
        db.session.execute(db.text("DELETE FROM products"))

        db.session.commit()

        print("Creating products...")

        product_objects = []

        for item in PRODUCTS:
            product = Product(
                name=item["name"],
                description=item["description"],
                image=item["image"],
                price=item["price"],
                size=item["size"],
                color=item["color"]
            )

            product_objects.append(product)

        db.session.add_all(product_objects)

        print("Creating user...")

        user = User(
            username=USER["username"],
            password_hash=USER["password_hash"],
            email=USER["email"]
        )

        db.session.add(user)

        db.session.commit()

        print("Database seeded successfully!")