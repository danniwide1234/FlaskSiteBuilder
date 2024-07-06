from flask import render_template, redirect, flash, url_for, Blueprint
from app.reset_password import bp
from app.forms.forms import ResetPasswordForm  # Adjust path if necessary

reset_password_bp = Blueprint('reset_password', __name__)


@bp.route('/', methods=['GET', 'POST'])
def index():
    form = ResetPasswordForm()
    if form.validate_on_submit():
        # Handle reset password logic
        flash('Password reset successful!', 'success')
        return redirect(url_for('index.html'))  # Redirect to main index on successful password reset
    return render_template('reset_password/index.html', form=form)
