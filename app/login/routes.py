from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_user, current_user, logout_user
from app import db
from app.models.user import User
from app.forms.forms import LoginForm

bp = Blueprint('login', __name__)

@bp.route('/', methods=['GET', 'POST'])
def index():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard.index'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid email or password', 'danger')
            return redirect(url_for('login.index'))
        login_user(user, remember=form.remember_me.data)
        flash('Logged in successfully', 'success')
        return redirect(url_for('dashboard.index'))

    return render_template('login/index.html', form=form)
