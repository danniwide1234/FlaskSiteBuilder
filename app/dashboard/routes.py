from flask import render_template, Blueprint
from app.dashboard import bp

dashboard_bp = Blueprint('dashboard', __name__)

@bp.route('/')
def index():
    return render_template('dashboard/index.html')

