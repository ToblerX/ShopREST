import unittest
import json
from flask_testing import TestCase
from app import app, db
from app.models import Products_Database, Users_Database
from flask_bcrypt import generate_password_hash

class FlaskTestCase(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        app.config['SECRET_KEY'] = 'SECRETKEY'
        return app

    def setUp(self):
        db.create_all()
        # Add a sample user
        hashed_password = generate_password_hash('password').decode('utf-8')
        user = Users_Database(username='testuser', password=hashed_password)
        db.session.add(user)
        db.session.commit()

        # Add a sample product
        product = Products_Database(name='Sample Product', price=100)
        db.session.add(product)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    # Test for product GET
    def test_get_products(self):
        with self.client:
            self.client.post('/login', json={'username': 'testuser', 'password': 'password'})
            response = self.client.get('/products')
            self.assertEqual(response.status_code, 200)

    # Test for product POST
    def test_post_product(self):
        with self.client:
            self.client.post('/login', json={'username': 'testuser', 'password': 'password'})
            response = self.client.post('/products', json={'name': 'New Product', 'price': 150})
            self.assertEqual(response.status_code, 201)
            self.assertIn('New Product', str(response.data))

    # Test for product GET by ID
    def test_get_product(self):
        with self.client:
            self.client.post('/login', json={'username': 'testuser', 'password': 'password'})
            response = self.client.get('/product/1')
            self.assertEqual(response.status_code, 200)
            self.assertIn('Sample Product', str(response.data))

    # Test for product DELETE
    def test_delete_product(self):
        with self.client:
            self.client.post('/login', json={'username': 'testuser', 'password': 'password'})
            response = self.client.delete('/product/1')
            self.assertEqual(response.status_code, 200)

    # Test for user signup
    def test_signup(self):
        with self.client:
            response = self.client.post('/signup', json={'username': 'newuser', 'password': 'newpassword', 'confirm': 'newpassword'})
            self.assertEqual(response.status_code, 201)
            self.assertIn('User newuser is successfully created.', str(response.data))

    # Test for user login
    def test_login(self):
        with self.client:
            response = self.client.post('/login', json={'username': 'testuser', 'password': 'password'})
            self.assertEqual(response.status_code, 200)
            self.assertIn('testuser', str(response.data))

if __name__ == '__main__':
    unittest.main()
