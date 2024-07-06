from flask import Blueprint, render_template, flash, redirect, url_for
from app.forms.forms import RequestResetForm

reset_request_bp = Blueprint('reset_request', __name__)

@reset_request_bp.route('/reset_request', methods=['GET', 'POST'])
def reset_request():
    form = RequestResetForm()
    if form.validate_on_submit():
        # Handle password reset request logic here
        flash('Password reset link sent!', 'info')
        return redirect(url_for('login.login'))
    
    return render_template('reset_request/index.html', form=form)
