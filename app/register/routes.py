from flask import Blueprint, render_template, redirect, url_for, flash
from app.forms.forms import RegistrationForm  # Import RegistrationForm
from app.models.user import User  # Import User model
from app import db

bp = Blueprint('register', __name__, url_prefix='/register')

@bp.route('/', methods=['GET', 'POST'])
def index():
    form = RegistrationForm()
    if form.validate_on_submit():
        new_user = User(user_name=form.username.data, first_name=form.first_name.data, last_name=form.last_name.data, email=form.email.data)
        new_user.set_password(form.password.data)

        db.session.add(new_user)
        db.session.commit()

        flash('Account created successfully! You can now log in.', 'success')
        return redirect(url_for('login.index'))  # Assuming 'login.index' is correct

    return render_template('register/index.html', form=form)
