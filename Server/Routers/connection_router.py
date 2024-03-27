from flask import Blueprint, request, jsonify
from bson import json_util


from BLL.connection_bll import ConnectionBLL

connection = Blueprint("connection", __name__)

BLL = ConnectionBLL()
#login
@connection.route("/login", methods=["POST"])
def login():
    email = request.json.get('email')
    password = request.json.get('password')

    # Perform login operation in your business logic layer (BLL)
    user = BLL.login(email, password)


    if user:
        # Assuming BLL returns user details upon successful login
        return json_util.dumps({'success': True, 'message': 'Login successful', 'user': user}), 200
    else:
        return json_util.dumps({'success': False, 'message': 'Invalid email or password'}), 401


#login
@connection.route("/register", methods=["POST"])
def register():
    # אחרי שהלקוח נרשם יחזיר את הלקוח החדש
    return None