"""Models for Friender."""
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
import datetime

# TODO: add typing to models

bcrypt = Bcrypt()
db = SQLAlchemy()

def connect_db(app):
    """Connect SQLAlchemy to application."""
    db.app = app
    db.init_app(app)


"""Mapping for users that like other users"""
Match = db.Table('Match',
                 db.Column('user_liking_id', db.Integer,
                           db.ForeignKey('users.id')),
                 db.Column('user_liked_id', db.Integer,
                           db.ForeignKey('users.id'))
                 )


class Message(db.Model):
    """Message from one user to another."""

    __tablename__ = "messages"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    message = db.Column(db.String, nullable=False)

    from_user_id = db.Column(db.Integer,
                             db.ForeignKey("users.id"),
                             primary_key=True)

    to_user_id = db.Column(db.Integer,
                           db.ForeignKey("users.id"),
                           primary_key=True)

    timestamp = db.Column(db.DateTime, nullable=False,
                          default=datetime.datetime.now())

class User(db.Model):
    """User Model."""

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    first_name = db.Column(db.String(50), nullable=False)

    last_name = db.Column(db.String(50), nullable=False)

    email = db.Column(db.String(50), unique=True, nullable=False)

    password = db.Column(db.String(), nullable=False)

    # TODO: Add user image to database via correct path, for now will use url
    img_url = db.Column(db.String(50), nullable=False)

    # Users who like this user
    likers = db.relationship(
        'User',
        secondary='Match',
        primaryjoin=(Match.c.user_liked_id == id),
        secondaryjoin=(Match.c.user_liking_id == id)
    )

    # Users who this uses likes
    liked_users = db.relationship(
        'User',
        secondary='Match',
        primaryjoin=(Match.c.user_liking_id == id),
        secondaryjoin=(Match.c.user_liked_id == id)
    )

    def __repr__(self):
        return f"<User first_name:{self.first_name}"\
               f"last_name: {self.last_name}, email: {self.email}>"

    @classmethod
    def register(cls, first_name, last_name, email, password, img_url):
        """Register user to the application given form data.

        Hashes password and adds it to the database.
        """
        hashed_password = bcrypt.generate_password_hash(
            password).decode("utf-8")

        new_user = User(first_name=first_name,
                        last_name=last_name,
                        email=email,
                        password=hashed_password,
                        img_url=img_url)

        db.session.add(new_user)

        return new_user

    @classmethod
    def authenticate(cls, email, password):
        """Authenticate user upon log in request."""
        user = cls.query.filter_by(email=email).first()

        if user and bcrypt.check_password_hash(user.password, password):
            return user
        else:
            return False
    
    def like_user(self, liked_user_id):
        """Have a user like another user.

        The user_liking will be added to the liked_user's list of 
        likers. The liked_user will be added to the likers's list of
        liked_users.
        """
        liked_user = User.query.filter_by(id=liked_user_id)
        liked_user.likers.append(self)
        self.liked_users.append(liked_user)
        return liked_user

    # TODO: create a function that checks if the current user and the user 
    #       in question are matched (they both like each other)

    def serialize(self):
        """Serialize to dictionary."""
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "password": self.password,
            "img_url": self.img_url,
        }
