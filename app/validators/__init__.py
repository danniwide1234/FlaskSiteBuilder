from flask import Blueprint

bp = Blueprint('validators', __name__)

from app.validators import routes  # Import your routes

# Import your validators here if needed
from app.validators.routes import UniqueUsername, UniqueEmail
