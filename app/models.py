from . import db
class Products_Database(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

class Users_Database(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), nullable=False)
    password = db.Column(db.String(), nullable=False)