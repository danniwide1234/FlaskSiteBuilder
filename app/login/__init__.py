# app/login/__init__.py

from flask import Blueprint

bp = Blueprint('login', __name__)

# Import routes here to avoid circular import
from app.login import routes
