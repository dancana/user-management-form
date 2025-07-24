#forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, FileField, SubmitField
from wtforms.validators import input_required, Email,  EqualTo
from flask_wtf.file import FileAllowed
from email_validator import *

class LoginForm(FlaskForm):
    email = StringField("Email",validators=[input_required(),Email()])
    password = PasswordField("Password", validators=[input_required()])
    submit = SubmitField("Login")

class RegisterForm(FlaskForm):
    username = StringField("Username", validators=[input_required()])
    email = StringField("Email", validators=[input_required(), Email()])
    password = PasswordField("Password", validators=[input_required(), EqualTo('confirm_password', message='Passwords must match')])
    confirm_password = PasswordField("Confirm Password", validators=[input_required(),EqualTo('password', message='Passwords must match')])
    profile_image = FileField("Profile Image", validators=[FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!')])
    submit = SubmitField("Register")

class EditProfileForm(FlaskForm):
    username = StringField("Username", validators=[input_required()])
    email = StringField("Email", validators=[input_required(), Email()])
    profile_image = FileField("Profile Image", validators=[FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!')])
    submit = SubmitField("Update Profile")

class AdminCreateUserForm(FlaskForm):
    username = StringField("Username", validators=[input_required()])
    email = StringField("Email", validators=[input_required(), Email()])
    password = PasswordField("Password", validators=[input_required(), EqualTo('comfirm_password', message='Passwords must match')])
    comfirm_password = PasswordField("Confirm Password", validators=[input_required()])
    submit = SubmitField("Create User")

    