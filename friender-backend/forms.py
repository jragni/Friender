from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, IntegerField
from wtforms.validators import DataRequired, Email, Length, NumberRange

class UserRegisterForm(FlaskForm):
    """Form for registering users."""

    first_name = StringField('First name', validators=[DataRequired()])
    last_name = StringField('Last name', validators=[DataRequired()])
    description = TextAreaField('Bio')
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[Length(min=6)])
    zipcode = StringField('Zipcode', validators=[DataRequired()])
    friend_radius = IntegerField('Friend Radius',  validators=[DataRequired(), NumberRange(min=10, max=100) ] )

class LoginForm(FlaskForm):
    """Login Form"""
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[Length(min=6)])

