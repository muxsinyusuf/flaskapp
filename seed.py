# from random import choice as rc

from faker import Faker

from app import app
from models import db, Car, User


fake = Faker()

with app.app_context():

    User.query.delete()
    # Car.query.delete()


    users= []

    for i in range (20):
        user = User(name=fake.name())
        users.append(user)


    

    db.session.add_all(users)
    db.session.commit()
    