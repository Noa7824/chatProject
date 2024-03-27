# from bson.objectid import ObjectId
from DAL.DB import db


class UsersDB:
    def __init__(self):
        self.__db = db
        self.__collection = self.__db["users"]
    def get_all_users(self):
        users = self.__collection.find({})
        return users
    def add_user(self, user):
        self.__collection.insert_one(user)
        return "Created"
    def get_user_by_email_and_password(self, email, password):
        user = self.__collection.find_one({"email": email, "password": password})
        return user
