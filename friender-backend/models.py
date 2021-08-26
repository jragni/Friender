"""SQLAlchemy models for Friender."""

from datetime import datetime

from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

bcrypt = Bcrypt()
db = SQLAlchemy()


# class Follows(db.Model):
# """Connection of a follower <-> followed_user."""

# __tablename__ = 'follows'

# user_being_followed_id = db.Column(
# db.Integer,
# db.ForeignKey('users.id', ondelete="cascade"),
# primary_key=True,
# )

# user_following_id = db.Column(
# db.Integer,
# db.ForeignKey('users.id', ondelete="cascade"),
# primary_key=True,
# )


class Like(db.Model):
    """User in the system."""

    __tablename__ = 'likes'

    from_id = db.Column(
        db.Integer,
        db.ForeignKey('users.id'),
        primary_key=True,
    )

    likes_id = db.Column(
        db.Integer,
        db.ForeignKey('users.id'),
        primary_key=True,
    )

class Rejection(db.Model):
    """User in the system."""

    __tablename__ = 'rejections'

    from_id = db.Column(
        db.Integer,
        db.ForeignKey('users.id'),
        primary_key=True,
    )

    rejections_id = db.Column(
        db.Integer,
        db.ForeignKey('users.id'),
        primary_key=True,
    )

class User(db.Model):
    """User in the system."""

    __tablename__ = 'users'

    id = db.Column(
        db.Integer,
        primary_key=True,
    )

    first_name = db.Column(
        db.String,
        nullable=False
    )

    last_name = db.Column(
        db.String,
        nullable=False
    )

    email = db.Column(
        db.Text,
        nullable=False,
        unique=True
    )

    password = db.Column(
        db.Text,
        nullable=False
    )

    description = db.Column(
        db.Text,
    )

    likes = db.relationship(
        "User",
        secondary="likes",
        primaryjoin=( Like.from_id == id),
        secondaryjoin=( Like.likes_id == id)
    )

    rejections = db.relationship(
        "User",
        secondary="rejections",
        primaryjoin=( Rejection.from_id == id),
        secondaryjoin=( Rejection.rejections_id == id)
    )

    def is_liked_by(self, likes_id):
        """Is this user followed by `other_user`?"""

        found_user_list = [user for user in self.likes if user == likes_id]
        return len(found_user_list) == 1


    # REVISIT ONCE AWS IS COMPLETE
    # image_url = db.Column(
    #     db.Text,
    #     # default="/static/images/default-pic.png",
    # )

    # REVISIT ONCE WE MAKE INTEREST TABLE
    # interest_id = db.column(
    #     db.Integer
    # )

    # REVISIT ONCE WE MAKE Hobby TABLE
    # hobbies_id = db.column(
    #     db.Integer
    # )

    # REVISIT ONCE WE MAKE Friends/Match table
    # friend_id = db.Column(
    #     db.Integer,
    # )

    # location = db.Column(
    #     db.Text,
    # )

    # messages = db.relationship('Message')


    # liked_messages = db.relationship('Message', secondary="likes")

    def __repr__(self):
        return f"<User #{self.id}: {self.first_name}, {self.last_name}, {self.email}>"

  
    def serialize(self):
        """Serialize to dictionary."""

        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email":self.email,
            "description":self.description
        }
        
    @classmethod
    def signup(cls, first_name, last_name, email, password):
        """Sign up user.

        Hashes password and adds user to system.
        """

        hashed_pwd = bcrypt.generate_password_hash(password).decode('UTF-8')

        user = User(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=hashed_pwd,
        )

        db.session.add(user)
        return user

    @classmethod
    def authenticate(cls, email, password):
        """Find user with `username` and `password`.

        This is a class method (call it on the class, not an individual user.)
        It searches for a user whose password hash matches this password
        and, if it finds such a user, returns that user object.

        If can't find matching user (or if password is wrong), returns False.
        """

        user = cls.query.filter_by(email=email).first()

        if user:
            is_auth = bcrypt.check_password_hash(user.password, password)
            if is_auth:
                return user

        return False






class Message(db.Model):
    """An individual messag"""

    __tablename__ = 'messages'

    id = db.Column(
        db.Integer,
        primary_key=True,
    )

    text = db.Column(
        db.String(140),
        nullable=False,
    )

    timestamp = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow(),
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey('users.id', ondelete='CASCADE'),
        nullable=False,
    )

    to_user_id = db.Column(
        db.Integer,
        db.ForeignKey('users.id', ondelete='CASCADE'),
        nullable=False,
    )


    user = db.relationship('User')


# def connect_db(app):
#     """Connect this database to provided Flask app.

#     You should call this in your Flask app.
#     """

#     db.app = app
#     db.init_app(app)


# class Like(db.Model):
#     """ Join table between users and messages (the join represents a like)."""

#     __tablename__ = 'likes'

#     id = db.Column(
#         db.Integer,
#         primary_key=True
#     )

#     user_id = db.Column(
#         db.Integer,
#         db.ForeignKey('users.id', ondelete='CASCADE'),
#         nullable=False, 
#     )

#     message_id = db.Column(
#         db.Integer,
#         db.ForeignKey('messages.id', ondelete='CASCADE'),
#         nullable=False, 
#     )
 

def connect_db(app):
    """Connect this database to provided Flask app.

    You should call this in your Flask app.
    """

    db.app = app
    db.init_app(app)
