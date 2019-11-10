from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import login, mongo
from flask_pymongo import ObjectId


@login.user_loader
def load_user(id):
    user = mongo.db.users.find_one({'_id': ObjectId(id)}, {'_id': 0, 'password': 0})

    if not user:
        return None
    return User(_id=id, **user)


class User(UserMixin):
    def __init__(self, _id, username, first_name='', last_name='', email='', country='', is_admin='false'):
        self.id = _id
        self.username = username
        self.is_admin = is_admin
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.country = country
