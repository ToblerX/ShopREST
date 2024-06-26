from flask import request, redirect, jsonify
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_restful import Resource, marshal_with, abort
from .models import Products_Database, Users_Database
from . import products_post_args, db, products_fields, users_fields, app
from .forms import RegistrationForm, LoginForm
from flask_login import login_user, login_required
from datetime import timedelta
from cloudipsp import Api, Checkout

class Products(Resource):
    @marshal_with(products_fields)
    @login_required
    def get(self):
        products = Products_Database.query.all()
        return products

    @marshal_with(products_fields)
    @login_required
    def post(self):
        data = products_post_args.parse_args()
        new_product = Products_Database(name=data['name'], price=data['price'])
        db.session.add(new_product)
        db.session.commit()
        return new_product, 201

class Product(Resource):
    @marshal_with(products_fields)
    @login_required
    def get(self, id):
        product = Products_Database.query.get(id)
        if not product:
            abort(404, message="Product not found")
        return product

    @login_required
    def delete(self, id):
        product_to_delete = Products_Database.query.get_or_404(id)
        db.session.delete(product_to_delete)
        db.session.commit()
        return {'message': f'Successfully deleted product with id {id}.'}, 200

class Signup(Resource):
    def get(self):
        return {'message': 'This is registration page.'}, 200

    def post(self):
        reg_form = RegistrationForm(data=request.get_json())

        if reg_form.validate():
            username = reg_form.username.data
            password = reg_form.password.data

            hashed_password = generate_password_hash(password).decode('utf-8')

            new_user = Users_Database(username=username, password=hashed_password)

            try:
                db.session.add(new_user)
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                return {'message': f'Failed to create a user. Error: {str(e)}'}, 400

            return {'message': f'User {username} is successfully created.'}, 201
        else:
            #print("Form validation errors:", reg_form.errors)
            return {'message': 'Failed to create a user.', 'errors': reg_form.errors}, 400

class Login(Resource):
    def get(self):
        return {'message': 'This is a login page.'}, 200

    def post(self):
        login_form = LoginForm(data=request.get_json())

        if login_form.validate():
            username = login_form.username.data
            password = login_form.password.data

            user = Users_Database.query.filter_by(username=username).first()

            if user:
                if check_password_hash(user.password, password):
                    login_user(user)
                    app.permanent_session_lifetime = timedelta(minutes=1)
                    return {'message': f'User {username} is successfully logged in.'}, 200
                else:
                    return {'message': f'Failed to login. Incorrect password.'}, 400
            else:
                return {'message': f'Failed to login. No user found.'}, 400
        else:
            return {'message': f'Failed to login.'}, 400

class Users(Resource):
    @marshal_with(users_fields)
    def get(self):
        users = Users_Database.query.all()
        return users, 200

class Buy(Resource):
    def get(self, id):
        product = Products_Database.query.get(id)
        api = Api(merchant_id=1396424, secret_key='test')
        checkout = Checkout(api=api)
        data = {
            "currency": "USD",
            "amount": product.price
        }
        url = checkout.url(data).get('checkout_url')
        return redirect(url)
