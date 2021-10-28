"""Models for Friender."""

from flask_sqlalchemy import SQLAlchemy
import datetime
import bcrypt

db = SQLAlchemy()


def connect_db(app):
    """Connect SQLAlchemy to application."""
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

    matches = db.relationship("Match")

    messages = db.relationship("Message")

    def __repr__(self):
        return f"<User first_name:{self.first_name}, last_name: {self.last_name}, email: {self.email}>"
    
    @classmethod
    def register(cls, username, email, password, img_url):
        """Register user to the application given form data.

        Hashes password and adds it to the database.
        """
        hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())

        new_user = User(username=username, email=email, password=hashed_password, img_url=img_url)

        db.session.add(new_user)

        return new_user

class Match(db.Model):
    """Mapping for user matching with other users.

    When users match with one another, they will be added to this table.
    """

    __tablename__ = "matches"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    user_a = db.Column(db.Integer,
                       db.ForeignKey("users.id"),
                       primary_key=True)

    user_b = db.Column(db.Integer, db.ForeignKey("users.id"), primary_key=True)


class Message(db.Model):
    """Messages between two users."""

    __tablename__ = "messages"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    message = db.Column(db.String, nullable=False)

    user_from_id = db.Column(db.Integer,
                             db.ForeignKey("users.id"),
                             primary_key=True)

    user_to_id = db.Column(db.Integer,
                           db.ForeignKey("users.id"),
                           primary_key=True)

    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.now())
