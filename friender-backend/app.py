import os
import boto3
from flask import Flask, render_template, request, session, g, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from sqlalchemy.exc import IntegrityError
# from flask_jwt import JWT, jwt_required, current_identity #used for flask token
import jwt
from forms import  UserRegisterForm, LoginForm
from models import Like, db, connect_db, User, Match
import random
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv




# aws_access_key = os.environ.get('S3_ACCESS_KEY')
# aws_secret_key = os.environ.get('S3_SECRET_KEY')
# bucket_name='friender-rithm-r-s'


# s3 = boto3.client(
#   "s3",
#   region_name="us-west-1",
#   aws_access_key_id=aws_access_key,
#   aws_secret_access_key=aws_secret_key
# )
# boto3.resource(
#   "s3",
#   region_name="us-west-1",
#   aws_access_key_id=aws_access_key,
#   aws_secret_access_key=aws_secret_key
# )

# def upload_file(file, object_name=None):

#     if object_name is None:
#         object_name = os.path.basename(file)

#     try:
#         s3.upload_file(file, bucket_name ,object_name, ExtraArgs={ "ContentType": "image/jpeg"})

#     except Exception as e:
#         print("Something Happened: ", e)



app = Flask(__name__)

CURR_USER_KEY = "CurrentUser"
# g.user = CURR_USER_KEY
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

# NOTE: if we have a single page app, and we make a request to axios we can
#       check in the session

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
                password=form.password.data,
                zipcode=form.zipcode.data,
                friend_radius = form.friend_radius.data
            )
            db.session.commit()

        except IntegrityError as e:
            return jsonify(failed="failed")

        do_login(user)

        # shouldnt need to redirect as REACT Will handle it
        #perhaps send JSON for success
        return jsonify(success="success")
    # Return error later
    return jsonify(failed="failed")


# Should not need a get route as REACT would build form and send
# data in JSON∂
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
            
            return jsonify(success="success")
    # Return error later
    return jsonify(failed="failed")



@app.route('/logout')
def logout():
    """Handle logout of user."""

    do_logout()

    # flash("You have successfully logged out.", 'success')
    # return redirect("/login")



###################      Swipes #######################

@app.route('/person')
def get_profile():

    email = os.getenv("EMAIL")
    email_password =  os.environ.get("EMAIL_PASSWORD")
    zip_api_key =  os.environ.get("ZIP_API_KEY")

    # r = requests.get(f"https://service.zipapi.us/zipcode/radius/90210?X-API-KEY={zip_api_key}&radius=10",
    # auth=HTTPBasicAuth(email, email_password))

    print(os.environ)
    print(zip_api_key,email,email_password)

    # rand = random.randrange(1,len(User.query.all())+1 ) 
    # profile  = User.query.get(rand)
    # serialized = profile.serialize()
    return jsonify(zip="zip")

@app.route('/likes', methods=["POST"])
def likes():
    
    likes_id = int(request.json["id"])
    liked_user = User.query.get_or_404(likes_id)
    if liked_user:
        g.user.likes.append(liked_user)
    
    liked_user_likes = liked_user.likes
    for liked_user_like in liked_user_likes:
        if liked_user_like.id == g.user.id:
            Match.match(g.user.id, likes_id)
  
    db.session.commit()

    return jsonify(success="likes")

@app.route('/rejects', methods=["POST"])
def rejects():
    rejects_id = int(request.json["id"])
    rejected_user = User.query.get_or_404(rejects_id)
    g.user.likes.append(rejected_user)

    db.session.commit()

    return jsonify(success="rejects")


@app.route('/matches')
def match():
    
    # matches = User.query.get(session[CURR_USER_KEY]).matches
    first_match = Match.query.with_entities(Match.second_id).filter( Match.first_id== g.user.id ).all()
    second_match = Match.query.with_entities(Match.first_id).filter( Match.second_id==g.user.id ).all()
    matches_id = []
    #this was returned as a tuple
    for match in first_match:
        matches_id.append(match[0])
    for match in second_match:
        matches_id.append(match[0])
    
    matches_unserialized = [ User.query.get(id) for id in matches_id ]
    matches = [ user.serialize() for user in matches_unserialized]

    # for like in likes:
    #     potential_matches = User.query.get(like.id)
    #     for  potential_match in potential_matches.likes:
    #         if potential_match.id == session[CURR_USER_KEY]:
    #             matches.append(like.serialize()) 
    
    return jsonify(matches=matches)
