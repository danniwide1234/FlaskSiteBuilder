from flask import Blueprint

bp = Blueprint('validators', __name__)

# Directly import UniqueUsername and UniqueEmail here
from app.validators.routes import UniqueUsername, UniqueEmail
