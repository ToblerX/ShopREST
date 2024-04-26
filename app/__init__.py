from flask import Flask
from flask_restful import Api, reqparse, fields
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'SECRETKEY'

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///shop.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

api = Api(app)

db = SQLAlchemy(app)

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

from .models import Products_Database
from . import routes

with app.app_context():
    db.create_all()

api.add_resource(routes.Products, "/products")
api.add_resource(routes.Product, "/product/<int:id>")
api.add_resource(routes.Registration, "/signup")
api.add_resource(routes.Users, "/users")