from app import db
from models import *
import os

if os.path.exists('my_database.db'):
    print("Datenbank wird gelöscht")
    os.remove('my_database.db')

db.create_all()

user = User(username="jonas", email="jonas.juenemann@gmx.de")
user.set_password("1234")
db.session.add(user)

user2 = User(username="betty", email="betty@betty.com")
user2.set_password("password")
db.session.add(user2)
p1 = Post(city="New York", country="USA", description="Hello New York", user_id=1)
p2 = Post(city="Berlin", country="germany", description="Das Brandenburger Tor besuchen!", user_id=2)

db.session.add(p1)
db.session.add(p2)
db.session.add(user)
db.session.add(user2)

try:
    db.session.commit()
except Exception as ex:
    print("The error is the following:", ex)
    db.session.rollback()

db.session.close()
