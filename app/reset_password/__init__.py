from flask import Blueprint

bp = Blueprint('reset_password', __name__)

from app.reset_password import routes
