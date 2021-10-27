""" Models for Friender"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy


def connect_db(app):
    """ initializes and connects the models to the app"""
    db.app = app
    db.init_app(app)


class User(db.Model):
    """User Model."""

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    first_name = db.Column(db.String(50), nullable=False)

    last_name = db.Column(db.String(50), nullable=False)

    email = db.Column(db.String(50), unique=True, nullable=False)

    password = db.Column(db.String(50), nullable=False)

    # TODO: Add user image to database via correct path, for now will use url
    img_url = db.Column(db.String(50), nullable=False)
    
    matches = db.relationship("Matches", 
                               backref="user", 
                               secondary="Matches")

    messages = db.relationship("Message")


class Match(db.Model):
    """ Mapping for user matching with other users.
    When users match with one another, they will be added to this table.
    """

    __tablename__ = "matches"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    user_a = db.Column(db.Integer, 
                       db.ForeignKey("users.id"), 
                       primary_key=True)

    user_b = db.Column(db.Integer, db.ForeignKey("users.id"), primary_key=True) 

class Message(db.Model):
    """ Messages between two users."""

    __tablename__ = "messages"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    message = db.Column(db.String, nullable=False)
    user_from_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    user_to_id = db.Column(db.Integer, db.ForeignKey("users.id"))


    
