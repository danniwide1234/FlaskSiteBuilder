import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a_hard_to_guess_string'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'instance/app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True  # Ensure this is True for development
    WTF_CSRF_ENABLED = True 

class ProductionConfig(Config):
    DEBUG = False  # Ensure this is False for production
