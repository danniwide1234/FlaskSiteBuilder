from wtforms import ValidationError
from app.models.user import User

class UniqueUsername:
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
            message = 'This email is already registered.'
        self.message = message

    def __call__(self, form, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError(self.message)
