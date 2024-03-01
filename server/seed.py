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
            image='https://image.spreadshirtmedia.com/image-server/v1/mp/products/T812A2MPA1664PT17X11Y16D13097815S59/views/2,width=800,height=800,appearanceId=2,backgroundColor=F2F2F2,modelId=127,crop=list,version=1560425676,modelImageVersion=1554715238/military-police-military-police-mens-premium-t-shirt.jpg',
            price=randint(1, 1000),
            size=fake.text(),
            color=fake.text()
        )

        products.append(p1)

        p2 = Product(
            name=fake.name(),
            description=fake.text(),
            image='https://ih1.redbubble.net/image.361537736.3970/ssrco,classic_tee,flatlay,101010:01c5ca27c6,front,wide_portrait,750x1000.u2.jpg',
            price=randint(1, 1000),
            size=fake.text(),
            color=fake.text()
        )

        products.append(p2)

        p3 = Product(
            name=fake.name(),
            description=fake.text(),
            image='https://i.pinimg.com/originals/0c/86/70/0c867045c528b0413b3d8c753aa1d0c7.jpg',
            price=randint(1, 1000),
            size=fake.text(),
            color=fake.text()
        )

        products.append(p3)

        p4 = Product(
            name=fake.name(),
            description=fake.text(),
            image='https://i.pinimg.com/originals/d2/7b/12/d27b12659a889e3ff2467d42ecbbf816.jpg',
            price=randint(1, 1000),
            size=fake.text(),
            color=fake.text()
        )

        products.append(p4)

        p5 = Product(
            name=fake.name(),
            description=fake.text(),
            image='https://image.spreadshirtmedia.com/image-server/v1/mp/products/T686A2MPA3026PT17X12Y0D1017862662FS4322/views/1,width=378,height=378,appearanceId=2,backgroundColor=F2F2F2,version=1571718329/funny-navy-design-united-states-navy-army-parody-mens-v-neck-t-shirt.jpg',
            price=randint(1, 1000),
            size=fake.text(),
            color=fake.text()
        )

        products.append(p5)

        p6 = Product(
            name=fake.name(),
            description=fake.text(),
            image='https://i.pinimg.com/originals/ed/44/14/ed44147d57f2805064b604b31669a815.jpg',
            price=randint(1, 1000),
            size=fake.text(),
            color=fake.text()
        )

        products.append(p6)

        p7 = Product(
            name=fake.name(),
            description=fake.text(),
            image='https://image.spreadshirtmedia.com/image-server/v1/mp/products/T812A2PA1663PT17X12Y62D13350611S77/views/1,width=378,height=378,appearanceId=2,backgroundColor=E8E8E8,version=1524725084/ptsd-result-of-one-s-duty-and-doing-the-task-men-s-premium-t-shirt.jpg',
            price=randint(1, 1000),
            size=fake.text(),
            color=fake.text()
        )

        products.append(p7)

        p8 = Product(
            name=fake.name(),
            description=fake.text(),
            image='https://m.media-amazon.com/images/I/A13usaonutL._CLa%7C2140%2C2000%7C81f1k2mXBvL.png%7C0%2C0%2C2140%2C2000%2B0.0%2C0.0%2C2140.0%2C2000.0_AC_UL1500_.png',
            price=randint(1, 1000),
            size=fake.text(),
            color=fake.text()
        )

        products.append(p8)

        p9 = Product(
            name=fake.name(),
            description=fake.text(),
            image='https://i.pinimg.com/736x/c7/9f/7a/c79f7a3a71c7f4cf61677f381c7ab2dd--snipers-funny-tee-shirts.jpg',
            price=randint(1, 1000),
            size=fake.text(),
            color=fake.text()
        )

        products.append(p9)

        p10 = Product(
            name=fake.name(),
            description=fake.text(),
            image='https://i.pinimg.com/originals/8c/9e/44/8c9e44ffecb5cc9d3f12dc3396915e92.jpg',
            price=randint(1, 1000),
            size=fake.text(),
            color=fake.text()
        )

        products.append(p10)

        p11 = Product(
            name=fake.name(),
            description=fake.text(),
            image='https://i.pinimg.com/originals/01/c7/6c/01c76c83bf5d36fb17377f1836dc08a5.jpg',
            price=randint(1, 1000),
            size=fake.text(),
            color=fake.text()
        )

        products.append(p11)

        db.session.add_all(products)
        db.session.commit()

        user1 = User(
            username='TMcCann2019',
            password_hash='Rio123',
            email='timothysmccann@gmail.com'
        )

        db.session.add(user1)
        db.session.commit()