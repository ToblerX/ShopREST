from flask import jsonify
from flask_restful import Resource, marshal_with
from .models import Products_Database
from . import products_post_args, db, products_fields
class Products(Resource):
    @marshal_with(products_fields)
    def get(self):
        products = Products_Database.query.all()
        return products

    @marshal_with(products_fields)
    def post(self):
        data = products_post_args.parse_args()
        new_product = Products_Database(name=data['name'])
        db.session.add(new_product)
        db.session.commit()
        return new_product, 201

class Product(Resource):
    @marshal_with(products_fields)
    def get(self, id):
        product = Products_Database.query.get_or_404(id)
        return product

    @marshal_with(products_fields)
    def delete(self, id):
        product_to_delete = Products_Database.query.get_or_404(id)
        db.session.delete(product_to_delete)
        db.session.commit()
        return {'message' : f'Successfully deleted product with id {id}'}, 200