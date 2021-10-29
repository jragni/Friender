"""Models for Friender."""
from flask_bcrypt import Bcrypt  
from flask_sqlalchemy import SQLAlchemy
import datetime

bcrypt = Bcrypt()
db = SQLAlchemy()

def connect_db(app):
    """Connect SQLAlchemy to application."""
    db.app = app
    db.init_app(app)

class Match(db.Model):
    """Mapping for user matching with other users.

    When users like each one another, they are matched and can now message each other.
    """

    __tablename__ = "matches"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    # The user_liking -> user_liked
    user_liking_id = db.Column(db.Integer,
                       db.ForeignKey("users.id"),
                       primary_key=True)

    user_liked_id = db.Column(db.Integer, 
                       db.ForeignKey("users.id"),
                       primary_key=True)
    

class Message(db.Model):
    """Message from one user to another."""

    __tablename__ = "messages"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    message = db.Column(db.String, nullable=False)

    from_user_id= db.Column(db.Integer,
                             db.ForeignKey("users.id"),
                             primary_key=True)

    to_user_id = db.Column(db.Integer,
                           db.ForeignKey("users.id"),
                           primary_key=True)

    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now())

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
    # TODO: Add message

    # Users who like this user
    likers = db.relationship('User',
                                       secondary='Match',
                                       primaryjoin=(Match.user_liked_id==id),
                                       secondaryjoin=(Match.user_liking_id==id))

    likees = db.relationship('User',
                                       secondary='Match',
                                       primaryjoin=(Match.user_liked_id==id),
                                       secondaryjoin=(Match.user_liking_id==id))

    messages_from = db.relationship('User',
                                       secondary='Message',
                                       primaryjoin=(Message.from_user_id ==id),
                                       secondaryjoin=(Message.to_user_id == id))

    messages_to = db.relationship('User',
                                       secondary='message',
                                       primaryjoin=(Match.user_liked_id==id),
                                       secondaryjoin=(Match.user_liking_id==id))
            

    def __repr__(self):
        return f"<User first_name:{self.first_name}, last_name: {self.last_name}, email: {self.email}>"
    
    @classmethod
    def register(cls, first_name, last_name, email, password, img_url):
        """Register user to the application given form data.

        Hashes password and adds it to the database.
        """
        hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")

        new_user = User(first_name=first_name, 
                        last_name=last_name, 
                        email=email, 
                        password=hashed_password, 
                        img_url=img_url)

        db.session.add(new_user)

        return new_user

