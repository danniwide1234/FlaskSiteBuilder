from flask import render_template, Blueprint
from flask_login import current_user

bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    return render_template('index.html')
