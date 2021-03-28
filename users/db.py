import pymongo
from pymongo import MongoClient

cluster = MongoClient('mongodb://root:password@localhost:27017')
db = cluster.users


def register(login: str, password: str):
    try:
        db.users.insert_one({
            '_id': login,
            'password': password
        })
    except pymongo.errors.DuplicateKeyError:
        raise UserAlreadyExists


def login(login: str, password: str):
    user = db.users.find_one({
        '_id': login,
        'password': password
    })
    if user is None:
        raise AuthenticationError
    return user


class UserAlreadyExists(Exception):
    pass


class AuthenticationError(Exception):
    pass
