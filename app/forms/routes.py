from flask import Blueprint, render_template, redirect, url_for, flash
from app.forms.forms import LoginForm, RegistrationForm
from app.validators.routes import UniqueUsername, UniqueEmail
from extensions import db

bp = Blueprint('forms', __name__)

bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Handle login logic here (example: check credentials, authenticate user)
        flash('Login successful!', 'success')
        return redirect(url_for('main.index'))  # Redirect to the main index on successful login
    return render_template('login/index.html', form=form)

bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # Handle registration logic here (example: create new user, store in database)
        flash('Registration successful!', 'success')
        return redirect(url_for('main.index'))  # Redirect to the main index on successful registration
    return render_template('register/index.html', form=form)

bp.route('/logout')
def logout():
    # Handle logout logic here (example: clear session, redirect to login)
    flash('You have been logged out.', 'info')
    return redirect(url_for('login.index'))  # Redirect to the login page after logout
