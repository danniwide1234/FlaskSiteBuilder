from flask import Blueprint

bp = Blueprint('edit_page', __name__)

from app.edit_page import routes
