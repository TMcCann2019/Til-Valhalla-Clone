#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import *

if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
        User.query.delete()
        Order.query.delete()
        OrderItem.query.delete()
        Product.query.delete()
        print("Starting seed...")
        
        products = []

        p1 = Product(
            name=fake.name(),
            description=fake.text(),
            image=fake.image_url(),
            price=randint(1, 1000),
            size=fake.text(),
            color=fake.text()
        )

        products.append(p1)

        p2 = Product(
            name=fake.name(),
            description=fake.text(),
            image=fake.image_url(),
            price=randint(1, 1000),
            size=fake.text(),
            color=fake.text()
        )

        products.append(p2)

        p3 = Product(
            name=fake.name(),
            description=fake.text(),
            image=fake.image_url(),
            price=randint(1, 1000),
            size=fake.text(),
            color=fake.text()
        )

        products.append(p3)

        p4 = Product(
            name=fake.name(),
            description=fake.text(),
            image=fake.image_url(),
            price=randint(1, 1000),
            size=fake.text(),
            color=fake.text()
        )

        products.append(p4)

        p5 = Product(
            name=fake.name(),
            description=fake.text(),
            image=fake.image_url(),
            price=randint(1, 1000),
            size=fake.text(),
            color=fake.text()
        )

        products.append(p5)

        p6 = Product(
            name=fake.name(),
            description=fake.text(),
            image=fake.image_url(),
            price=randint(1, 1000),
            size=fake.text(),
            color=fake.text()
        )

        products.append(p6)

        p7 = Product(
            name=fake.name(),
            description=fake.text(),
            image=fake.image_url(),
            price=randint(1, 1000),
            size=fake.text(),
            color=fake.text()
        )

        products.append(p7)

        p8 = Product(
            name=fake.name(),
            description=fake.text(),
            image=fake.image_url(),
            price=randint(1, 1000),
            size=fake.text(),
            color=fake.text()
        )

        products.append(p8)

        p9 = Product(
            name=fake.name(),
            description=fake.text(),
            image=fake.image_url(),
            price=randint(1, 1000),
            size=fake.text(),
            color=fake.text()
        )

        products.append(p9)

        p10 = Product(
            name=fake.name(),
            description=fake.text(),
            image=fake.image_url(),
            price=randint(1, 1000),
            size=fake.text(),
            color=fake.text()
        )

        products.append(p10)

        db.session.add_all(products)
        db.session.commit()

        user1 = User(
            username='TMcCann2019',
            password='Rio123',
            email='timothysmccann@gmail.com'
        )
        
        db.session.add(user1)
        db.session.commit()