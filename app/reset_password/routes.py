from flask import render_template, redirect, url_for, flash, Blueprint
from app.forms.forms import ResetPasswordForm
from extensions import db

bp = Blueprint('reset_password', __name__)

@bp.route('/', methods=['GET', 'POST'])
def index():
    form = ResetPasswordForm()
    if form.validate_on_submit():
        # Handle password reset logic here (example: update user's password)
        flash('Password reset successful!', 'success')
        return redirect(url_for('login.index'))  # Redirect to the login page on successful password reset
    return render_template('reset_password/index.html', form=form)
