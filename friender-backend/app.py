
from flask import Flask, render_template, redirect, g
from models import db, connect_db, User
from forms import UserForm
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///friender'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "oh-so-secret"
debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

@app.route('/auth/login', methods=['POST']
def login():
    """ Authenticates user from login form credentials

    Returns JSON {'user': {id, first_name, last_name}}
    """
    serialize
    # query user info from DB
    pass


