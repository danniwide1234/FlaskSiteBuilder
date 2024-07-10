from flask import render_template, Blueprint

bp = Blueprint('dashboard', __name__)

@bp.route('/')
def index():
    return render_template('dashboard/index.html')
