from flask import Blueprint

bp = Blueprint('reset_request', __name__)

from app.reset_request import routes
