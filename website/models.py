from . import db
from sqlalchemy.sql import func

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    oauth = db.Column(db.Boolean, nullable=False)

class User_Info(db.Model):
    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True,)