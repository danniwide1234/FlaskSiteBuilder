from flask import render_template, redirect, url_for, flash, Blueprint
from app.forms.forms import RequestResetForm
from extensions import db

bp = Blueprint('reset_request', __name__)

@bp.route('/', methods=['GET', 'POST'])
def index():
    form = RequestResetForm()
    if form.validate_on_submit():
        # Handle password reset request logic here (example: send reset email)
        flash('Password reset request submitted!', 'info')
        return redirect(url_for('login.index'))  # Redirect to the login page on successful request
    return render_template('reset_request/index.html', form=form)
