from flask import Blueprint, jsonify, request
from BLL.users_bll import UsersBLL
from bson import json_util


# אני רוצה ליצור תת מסלול חדש שאליו מקושרות כל הבקשות של לקוחות
users = Blueprint("users", __name__)

BLL = UsersBLL()

#Get All
@users.route("/", methods=["GET"])
def get_all_users():
    users = BLL.get_all_users()
    print(users)

    return json_util.dumps(users)
