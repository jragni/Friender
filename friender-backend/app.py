"""Models for Friender."""
from flask import Flask, g, request, jsonify
from models import db, connect_db, User
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///friender'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "oh-so-secret"
debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

@app.route('/api/auth/login', methods=['POST'])
def login():
    """Authenticate user from login form credentials.

    Returns JSON {'user': {id, first_name, last_name, token}}
    """

    #TODO: build out login
    pass

@app.route('/api/auth/register', methods=['POST'])
def register():
    """Register user from form data.

    Returns JSON {'users': {id, first_name, last_name, token}} 
    """

    first_name = request.json['first_name']
    last_name = request.json['last_name']
    email = request.json['email']
    password = request.json['password']
    img_url = request.json['img_url']

    new_user = User.register(first_name=first_name, 
                             last_name=last_name,
                             email=email, 
                             password=password, 
                             img_url=img_url) 

    db.session.commit()
    g.user = new_user
    serialized = new_user.serialize()

    # Return w/status code 201 --- return tuple (json, status)
    return (jsonify(dessert=serialized), 201)


# TODO: Create a route for GET current user's matches
# TODO: Create a route for POST matching user with selected user
# TODO: Create a route Getting all messages between two users
# TODO: create a route for Posting a Message from one user to another user
# TODO: Create a route for editing the current user