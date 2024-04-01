from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()


# CREATE TABLE IN DB with the UserMixin
class User(db.Model, UserMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password= db.Column(db.String(250))
    name = db.Column(db.String(250))

    # Add init to remove Unexpected keyword argument warning
    def __init__(self, email, password, name):
        self.email = email
        self.password = password
        self.name = name
