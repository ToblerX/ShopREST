from flask import Flask
from flask_restful import Api, reqparse, fields
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from .utils import TestClientLogin
from .test import BASE

app = Flask(__name__)
app.secret_key = 'SECRETKEY'

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///shop.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

api = Api(app)

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

products_post_args = reqparse.RequestParser()
products_post_args.add_argument("name", type=str, help="Name of a product")

products_fields = {
    'id' : fields.Integer,
    'name' : fields.String
}

users_fields = {
    'id' : fields.Integer,
    'username' : fields.String
}

test_client = TestClientLogin(app, 'test3', '12345')

from .models import Products_Database, Users_Database
from . import routes

with app.app_context():
    db.create_all()

@login_manager.user_loader
def load_user(user_id):
    return Users_Database.query.get(int(user_id))

api.add_resource(routes.Products, "/products")
api.add_resource(routes.Product, "/product/<int:id>")
api.add_resource(routes.Signup, "/signup")
api.add_resource(routes.Login, "/login")
api.add_resource(routes.Users, "/users")


# testing /products endpoint for logged in users

#data = {
#    "name": "table",
#}

#test_client.test_get_request(BASE + 'products', Users_Database, 3)
#test_client.test_post_request(BASE + 'products', Users_Database, 3, data)