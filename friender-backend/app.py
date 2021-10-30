from flask import Flask, g, request, jsonify, session
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

# key for getting the current user
CURR_USER_KEY = "curr_user"

# AUTH: Log in and registration


@app.before_request
def add_user_to_g():
    """If we are logged in, add current user to g."""
    if CURR_USER_KEY in session:
        g.user = User.query.get(session[CURR_USER_KEY])

    else:
        g.user = None


def do_login(user):
    """Log user in.

    Assigns the user id to the session.
    """
    session[CURR_USER_KEY] = user.id


@app.route('/api/auth/login', methods=['POST'])
def login():
    """Authenticate user from login form credentials.

    Returns JSON {'user': {id, first_name, last_name, token}}
    """
    email = request.json['email']
    password = request.json['password']

    valid_user = User.authenticate(email, password)
    if valid_user:
        do_login(valid_user)
        serialized = valid_user.serialize()
        return jsonify(user=serialized)
    
    return jsonify(msg="Invalid credentials. Please try again")


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

    # If the email already exists, respond with a message.
    if (User.query.filter_by(email=email).first()):
        msg = "Email is already registered. Please use another email"
        return jsonify(msg=msg)

    new_user = User.register(first_name=first_name,
                             last_name=last_name,
                             email=email,
                             password=password,
                             img_url=img_url)

    db.session.commit()
    do_login(new_user)
    serialized = new_user.serialize()

    # Return w/status code 201 --- return tuple (json, status)
    return (jsonify(user=serialized), 201)


@app.route("/api/auth/logout", methods=["POST"])
def logout():
    """Log the current user out."""
    if g.user:
        print('g.user: ', g.user, "session: ", session[CURR_USER_KEY])
        g.user = None
        session.pop(CURR_USER_KEY, None)
        msg = "You have been logged out!"
        return jsonify(msg=msg)
    
    return jsonify(msg="You are not logged in!")
# END AUTH


# FOR DEV TESTING
@app.route("/api/test", methods=["POST"])
def api_tests():
    """Docstrings the test."""
    data = request.json["data"]
    print('This is the data: ', data, '-----------------')
    if g.user:
        return jsonify(user=g.user.serialize())

    return jsonify("TEST PASSED")

# end DEV TESTING


@app.route('/api/users/like/<int:id>', methods=['POST'])
def like_user(id):
    """Like a user."""
    pass

# TODO: Create a route for GET current user's matches
# TODO: Create a route for POST matching user with selected user
# TODO: Create a route Getting all messages between two users
# TODO: create a route for Posting a Message from one user to another user
# TODO: Create a route for editing the current user
