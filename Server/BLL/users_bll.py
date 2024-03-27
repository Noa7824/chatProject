from DAL.users_db import UsersDB


class UsersBLL:
    def __init__(self):
        self.__users_db = UsersDB()

    def get_all_users(self):
        users = list(self.__users_db.get_all_users())
        return users



