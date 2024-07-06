from flask import Blueprint

bp = Blueprint('register', __name__, template_folder='templates')

# Import routes at the end to avoid circular import issues
from app.register import routes

