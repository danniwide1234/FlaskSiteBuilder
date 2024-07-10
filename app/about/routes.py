from flask import render_template, Blueprint

bp = Blueprint('about', __name__)

@bp.route('/')
def index():
    return render_template('about/index.html')
