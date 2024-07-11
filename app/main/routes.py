from flask import render_template, Blueprint, redirect, url_for
from flask_login import current_user

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/edit_profile')
def edit_profile():
    # Logic for editing profile can go here. For now, it just redirects to the dashboard.
    return redirect(url_for('dashboard.index'))
