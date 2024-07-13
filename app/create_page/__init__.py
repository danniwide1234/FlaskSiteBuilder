from flask import Blueprint

bp = Blueprint('create_page', __name__)

from app.create_page import routes
