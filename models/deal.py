from flask_sqlalchemy import SQLAlchemy
from config import db

class Deal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    price = db.Column(db.String(20), nullable=False)
    discount = db.Column(db.String(20), nullable=False)
    def __init__(self, title, price,discount):
        self.title = title
        self.price = price
        self.discount = discount