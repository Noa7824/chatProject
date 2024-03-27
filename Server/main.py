from flask import Flask
from flask_cors import CORS
from Routers.connection_router import connection
from Routers.users_router import users



app = Flask(__name__)


CORS(app)


app.register_blueprint(users, url_prefix="/users")
app.register_blueprint(connection, url_prefix="")


if __name__ == "__main__":
    app.run("localhost", 8000)

