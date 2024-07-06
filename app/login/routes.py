from flask import render_template, redirect, url_for, flash, Blueprint
from app.forms.forms import LoginForm
from extensions import db

login_bp = Blueprint('login', __name__)

@login_bp.route('/', methods=['GET', 'POST'])
def index():
    form = LoginForm()
    if form.validate_on_submit():
        # Handle login logic here (example: check credentials, authenticate user)
        flash('Login successful!', 'success')
        return redirect(url_for('main.index'))  # Redirect to the main index on successful login
    return render_template('login/index.html', form=form)
