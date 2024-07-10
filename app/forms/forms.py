# app/forms/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from app.models.user import User  # Correct import path

# Custom Validators
class UniqueUserName:
    def __init__(self, message=None):
        if not message:
            message = 'This username is already taken.'
        self.message = message

    def __call__(self, form, field):
        if User.query.filter_by(user_name=field.data).first():
            raise ValidationError(self.message)

class UniqueEmail:
    def __init__(self, message=None):
        if not message:
            message = 'This email is already in use.'
        self.message = message

    def __call__(self, form, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError(self.message)

# Form Classes
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), UniqueUserName()])
    email = StringField('Email', validators=[DataRequired(), Email(), UniqueEmail()])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('confirm_password', message='Passwords must match')])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Register')



class RequestResetForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('confirm_password', message='Passwords must match')])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Reset Password')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    message = TextAreaField('Message', validators=[DataRequired()])
    submit = SubmitField('Send')
