from flask import Blueprint, render_template, redirect, flash, url_for
from app.forms.forms import RegisterForm

register_bp = Blueprint('register', __name__)

@register_bp.route('/', methods=['GET', 'POST'])
def index():
    form = RegisterForm()
    if form.validate_on_submit():
        # Handle register logic here (example: create a new user)
        flash('Registration successful!', 'success')
        return redirect(url_for('index.html'))  # Redirect to the main index on successful registration
    return render_template('register/index.html', form=form)
