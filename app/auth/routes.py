from flask import Blueprint, render_template, redirect, url_for, flash
from app.extensions import db
from app.models.auth import User

bp = Blueprint('auth', __name__)

@bp.route('/login', methods=['GET', 'POST'])
def login():
    # Add your login logic here
    return render_template('auth/login.html')

@bp.route('/register', methods=['GET', 'POST'])
def register():
    # Add your registration logic here
    return render_template('auth/register.html')

@bp.route('/logout')
def logout():
    # Add your logout logic here
    return redirect(url_for('main.index'))

