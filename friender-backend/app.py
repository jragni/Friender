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

email = os.getenv("EMAIL")
email_password =  os.environ.get("EMAIL_PASSWORD")
zip_api_key =  os.environ.get("ZIP_API_KEY")
test_zip = {'data': [{'ZipCode': '94121', 'distance': '0'},{'ZipCode': '90210', 'distance': '0'}, {'ZipCode': '90077', 'distance': '2.0723805210278052'}, {'ZipCode': '90069', 'distance': '2.1146886594328533'}, {'ZipCode': '90209', 'distance': '2.2443215484549315'}, {'ZipCode': '90213', 'distance': '2.2443215484549315'}, {'ZipCode': '90095', 'distance': '2.7017962523312495'}, {'ZipCode': '90046', 'distance': '2.7246824139797385'}, {'ZipCode': '90024', 'distance': '2.781801455858396'}, {'ZipCode': '91604', 'distance': '2.861208782218938'}, {'ZipCode': '90212', 'distance': '3.0181212235615384'}, {'ZipCode': '91423', 'distance': '3.1159349318911445'}, {'ZipCode': '90067', 'distance': '3.1386642126299464'}, {'ZipCode': '90048', 'distance': '3.1920119219937284'}, {'ZipCode': '90211', 'distance': '3.3281790774731768'}, {'ZipCode': '90084', 'distance': '3.372157317031148'}, {'ZipCode': '90073', 'distance': '3.6396304145950467'}, {'ZipCode': '91413', 'distance': '3.792957922366101'}, {'ZipCode': '90035', 'distance': '3.946173959980035'}, {'ZipCode': '91403', 'distance': '4.094573905639882'}, {'ZipCode': '91495', 'distance': '4.107419133211345'}, {'ZipCode': '90049', 'distance': '4.280099064539145'}, {'ZipCode': '90025', 'distance': '4.287044000579212'}, {'ZipCode': '91602', 'distance': '4.300583583141856'}, {'ZipCode': '91608', 'distance': '4.330233950495441'}, {'ZipCode': '91607', 'distance': '4.356872763300985'}, {'ZipCode': '90036', 'distance': '4.389288883363444'}, {'ZipCode': '90064', 'distance': '4.611786008311598'}, {'ZipCode': '90068', 'distance': '4.976911006233663'}, {'ZipCode': '90028', 'distance': '5.081800112404942'}, {'ZipCode': '90038', 'distance': '5.188612750361459'}, {'ZipCode': '90034', 'distance': '5.189254431819732'}, {'ZipCode': '91601', 'distance': '5.241960550336604'}, {'ZipCode': '91603', 'distance': '5.244966714967491'}, {'ZipCode': '91609', 'distance': '5.244966714967491'}, {'ZipCode': '91610', 'distance': '5.244966714967491'}, {'ZipCode': '91611', 'distance': '5.244966714967491'}, {'ZipCode': '91612', 'distance': '5.244966714967491'}, {'ZipCode': '91614', 'distance': '5.244966714967491'}, {'ZipCode': '91615', 'distance': '5.244966714967491'}, {'ZipCode': '91616', 'distance': '5.244966714967491'}, {'ZipCode': '91617', 'distance': '5.244966714967491'}, {'ZipCode': '91618', 'distance': '5.244966714967491'}, {'ZipCode': '91401', 'distance': '5.334839699691691'}, {'ZipCode': '91522', 'distance': '5.513014247038491'}, {'ZipCode': '91411', 'distance': '5.768817927657642'}, {'ZipCode': '90231', 'distance': '5.7830010443852755'}, {'ZipCode': '90233', 'distance': '5.7830010443852755'}, {'ZipCode': '90019', 'distance': '5.789469252707566'}, {'ZipCode': '91436', 'distance': '5.822885000636254'}, {'ZipCode': '91523', 'distance': '5.932754275976305'}, {'ZipCode': '90232', 'distance': '5.935368136454564'}, {'ZipCode': '91606', 'distance': '5.954752921425913'}, {'ZipCode': '91404', 'distance': '6.072785808599031'}, {'ZipCode': '91407', 'distance': '6.072785808599031'}, {'ZipCode': '91408', 'distance': '6.072785808599031'}, {'ZipCode': '91409', 'distance': '6.072785808599031'}, {'ZipCode': '91410', 'distance': '6.072785808599031'}, {'ZipCode': '91470', 'distance': '6.072785808599031'}, {'ZipCode': '91482', 'distance': '6.072785808599031'}, {'ZipCode': '91496', 'distance': '6.072785808599031'}, {'ZipCode': '91499', 'distance': '6.072785808599031'}, {'ZipCode': '90016', 'distance': '6.117199346188278'}, {'ZipCode': '90404', 'distance': '6.157182124523801'}, {'ZipCode': '91416', 'distance': '6.17361944447183'}, {'ZipCode': '91426', 'distance': '6.17361944447183'}, {'ZipCode': '90004', 'distance': '6.318975973637847'}, {'ZipCode': '91521', 'distance': '6.394233105122598'}, {'ZipCode': '91505', 'distance': '6.491644349175417'}, {'ZipCode': '90020', 'distance': '6.523012253618317'}, {'ZipCode': '90010', 'distance': '6.566787184357505'}, {'ZipCode': '90403', 'distance': '6.571568007876203'}, {'ZipCode': '90005', 'distance': '6.752993269932517'}, {'ZipCode': '90402', 'distance': '6.808098021569328'}, {'ZipCode': '90405', 'distance': '7.011227922947532'}, {'ZipCode': '91316', 'distance': '7.030999881334973'}, {'ZipCode': '91405', 'distance': '7.064945467408466'}, {'ZipCode': '90029', 'distance': '7.134681129123895'}, {'ZipCode': '90406', 'distance': '7.176300048026865'}, {'ZipCode': '90407', 'distance': '7.176300048026865'}, {'ZipCode': '90408', 'distance': '7.176300048026865'}, {'ZipCode': '90409', 'distance': '7.176300048026865'}, {'ZipCode': '90410', 'distance': '7.176300048026865'}, {'ZipCode': '90411', 'distance': '7.176300048026865'}, {'ZipCode': '90066', 'distance': '7.1765574673833274'}, {'ZipCode': '91506', 'distance': '7.189280898718823'}, {'ZipCode': '91605', 'distance': '7.365826922711315'}, {'ZipCode': '90027', 'distance': '7.4764041229379306'}, {'ZipCode': '90230', 'distance': '7.499885451530581'}, {'ZipCode': '90401', 'distance': '7.509988088142807'}, {'ZipCode': '90018', 'distance': '7.7013720803802395'}, {'ZipCode': '90272', 'distance': '7.702700435123977'}, {'ZipCode': '91406', 'distance': '7.7586238643182845'}, {'ZipCode': '90008', 'distance': '7.778954824456292'}, {'ZipCode': '90056', 'distance': '7.881268409435679'}, {'ZipCode': '91502', 'distance': '7.963848928286943'}, {'ZipCode': '90291', 'distance': '8.00421158715575'}, {'ZipCode': '90006', 'distance': '8.066298229171286'}, {'ZipCode': '90294', 'distance': '8.166405086819289'}, {'ZipCode': '91503', 'distance': '8.179725708976369'}, {'ZipCode': '91507', 'distance': '8.179725708976369'}, {'ZipCode': '91508', 'distance': '8.179725708976369'}, {'ZipCode': '91510', 'distance': '8.179725708976369'}, {'ZipCode': '91526', 'distance': '8.179725708976369'}, {'ZipCode': '91356', 'distance': '8.253646441703465'}, {'ZipCode': '91353', 'distance': '8.356897923271015'}, {'ZipCode': '90057', 'distance': '8.498152545368136'}, {'ZipCode': '90295', 'distance': '8.51524450873876'}, {'ZipCode': '91201', 'distance': '8.548630494458866'}, {'ZipCode': '91504', 'distance': '8.604679499860103'}, {'ZipCode': '91412', 'distance': '8.617961295972462'}, {'ZipCode': '91393', 'distance': '8.697662491762092'}, {'ZipCode': '90094', 'distance': '8.76828103561101'}, {'ZipCode': '90070', 'distance': '8.802564307799418'}, {'ZipCode': '90292', 'distance': '8.813802624721607'}, {'ZipCode': '91402', 'distance': '8.832988318175587'}, {'ZipCode': '90026', 'distance': '9.00334255682298'}, {'ZipCode': '91204', 'distance': '9.077159413453275'}, {'ZipCode': '90062', 'distance': '9.188735346288876'}, {'ZipCode': '91357', 'distance': '9.209643891826229'}, {'ZipCode': '90089', 'distance': '9.228001770181978'}, {'ZipCode': '91501', 'distance': '9.231390743637249'}, {'ZipCode': '91203', 'distance': '9.275031326422836'}, {'ZipCode': '90043', 'distance': '9.282299511065'}, {'ZipCode': '90007', 'distance': '9.293168994897984'}, {'ZipCode': '90039', 'distance': '9.296446259511923'}, {'ZipCode': '90017', 'distance': '9.334638668586436'}, {'ZipCode': '91210', 'distance': '9.563154829590461'}, {'ZipCode': '90015', 'distance': '9.574606899269622'}, {'ZipCode': '91337', 'distance': '9.616675989908586'}, {'ZipCode': '91209', 'distance': '9.652910592285519'}, {'ZipCode': '91221', 'distance': '9.652910592285519'}, {'ZipCode': '91222', 'distance': '9.652910592285519'}, {'ZipCode': '91224', 'distance': '9.652910592285519'}, {'ZipCode': '91225', 'distance': '9.652910592285519'}, {'ZipCode': '91226', 'distance': '9.652910592285519'}, {'ZipCode': '90302', 'distance': '9.681054625928457'}, {'ZipCode': '91202', 'distance': '9.73648482966614'}, {'ZipCode': '91385', 'distance': '9.744018874789017'}, {'ZipCode': '91352', 'distance': '9.778982312490095'}, {'ZipCode': '91335', 'distance': '9.787486038529822'}, {'ZipCode': '90071', 'distance': '9.85361671300343'}]}

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
"""{
  "user": {
    "description": null,
    "email": "simon@gmail.com",
    "first_name": "simon",
    "id": 2,
    "last_name": "simon"
  }
}"""
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
            
            return jsonify(user=user.serialize())
    # Return error later
    return jsonify(failed="failed")



@app.route('/logout')
def logout():
    """Handle logout of user."""

    do_logout()

    # flash("You have successfully logged out.", 'success')
    # return redirect("/login")



###################      Swipes #######################
"""
  returns  a profile
  {
  "profile": {
    "description": null,
    "email": "ray@gmail.com",
    "first_name": "ray",
    "id": 3,
    "last_name": "ray"
  }
}
"""
@app.route('/person')
def get_profile():

    r = requests.get(f"https://service.zipapi.us/zipcode/radius/{g.user.zipcode}?X-API-KEY={zip_api_key}&radius={g.user.friend_radius}",
    auth=HTTPBasicAuth(email, email_password))
    response = r.json()

    zipcodes = []
    for zipcode in response["data"]:
        zipcodes.append( (zipcode["ZipCode"] ))

    nearby_profiles = User.query.filter( User.zipcode.in_(zipcodes) ).all()
    likes =  g.user.likes
    rejection = g.user.rejections
    do_not_include = likes+rejection
    profiles = [ profile for profile in nearby_profiles if profile not in do_not_include]

    rand = random.randrange(0,len(profiles) ) 
    profile  = profiles[rand]
    serialized = profile.serialize()
    return jsonify(profile=serialized)

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
    g.user.rejections.append(rejected_user)

    db.session.commit()

    return jsonify(success="rejects")

"""{
  "matches": [
    {
      "description": null,
      "email": "ke@gmail.com",
      "first_name": "buk",
      "id": 4,
      "last_name": "ka"
    },
    {
      "description": null,
      "email": "ray@gmail.com",
      "first_name": "ray",
      "id": 3,
      "last_name": "ray"
    }
  ]
}"""
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
    
    return jsonify(matches=matches)
