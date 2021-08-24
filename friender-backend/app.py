import os

from flask import Flask, render_template, request, session, g, jsonify 
from flask_debugtoolbar import DebugToolbarExtension
from sqlalchemy.exc import IntegrityError

from forms import  UserRegisterForm, LoginForm
from models import db, connect_db, User


app = Flask(__name__)

# Get DB_URI from environ variable (useful for production/testing) or,
# if not set there, use development local db.
app.config['SQLALCHEMY_DATABASE_URI'] = (
    os.environ.get('DATABASE_URL', 'postgresql:///friender'))

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = True
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', "it's a secret")
toolbar = DebugToolbarExtension(app)
connect_db(app)

# will need to update later on user, use flask.g
CURR_USER_KEY = "curr_user"

##############################################################################
# User signup/login/logout

@app.before_request
def add_user_to_g():
    """If we're logged in, add curr user to Flask global."""

    if CURR_USER_KEY in session:
        # DOes this need to change depending on  how we want to get user
        g.user = User.query.get(session[CURR_USER_KEY])

    else:
        g.user = None


def do_login(user):
    """Log in user."""

    session[CURR_USER_KEY] = user.id


def do_logout():
    """Logout user."""

    if CURR_USER_KEY in session:
        del session[CURR_USER_KEY]

# Should not need a get route as REACT would build form and send
# data in JSON
@app.route('/signup', methods=[ "POST"])
def signup():
    """Handle user signup.

    Create new user and add to DB. Redirect to home page.

    If form not valid, present form.

    If the there already is a user with that username: flash message
    and re-present form.
    """

    incoming_request = request.json

    if CURR_USER_KEY in session:
        del session[CURR_USER_KEY]
    # TURNING OFF CSRF? BECASUE REACT -> FLASK react no csrf
    form = UserRegisterForm( formadata=incoming_request,
                        meta={'csrf': False})

    if form.validate_on_submit():
        try:
            user = User.signup(
                first_name=form.first_name.data,
                last_name=form.last_name.data,
                email=form.email.data,
                password=form.password.data
            )
            db.session.commit()

        except IntegrityError as e:
            flash("Username already taken", 'danger')
            return render_template('users/signup.html', form=form)

        do_login(user)

        # shouldnt need to redirect as REACT Will handle it
        #perhaps send JSON for success
        return jsonify(success="success")
    # Return error later
    return jsonify(failed="failed")

    # shouldnt need to redirect as REACT Will handle it
    #perhaps send JSON for success
    # return redirect("/")
    # else:
    #     return render_template('users/signup.html', form=form)

# Should not need a get route as REACT would build form and send
# data in JSON
@app.route('/login', methods=["POST"])
def login():
    """Handle user login."""
    incoming_request = request.json

    form = LoginForm(formadata=incoming_request,
                        meta={'csrf': False})

    if form.validate_on_submit():
        user = User.authenticate(form.email.data,
                                 form.password.data)

        if user:
            do_login(user)
            # flash(f"Hello, {user.username}!", "success")
            # return redirect("/")
            return jsonify(success="success")
    # Return error later
    return jsonify(failed="failed")

        # flash("Invalid credentials.", 'danger')

    # return render_template('users/login.html', form=form)


@app.route('/logout')
def logout():
    """Handle logout of user."""

    do_logout()

    # flash("You have successfully logged out.", 'success')
    # return redirect("/login")

