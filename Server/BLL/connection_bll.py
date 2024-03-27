from DAL.users_db import UsersDB

class ConnectionBLL:
    def __init__(self):
        self.__users_db = UsersDB()

    def login(self, email, password):
        user = self.__users_db.get_user_by_email_and_password(email, password)
        if user is not None:
            return user
        else:
            return False
