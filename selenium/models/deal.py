from flask_sqlalchemy import SQLAlchemy
from config import db

class Deal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    link=db.Column(db.String(200),nullable=True)
    our_link=db.Column(db.String(200),nullable=True)
    price = db.Column(db.String(20), nullable=False)
    discount = db.Column(db.String(20), nullable=False)
    