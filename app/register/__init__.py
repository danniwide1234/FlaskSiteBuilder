from flask import Blueprint

bp = Blueprint('register', __name__, url_prefix='/register')

from app.register import routes  # Import routes to register them
