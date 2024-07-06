from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

db = SQLAlchemy()
login_manager = LoginManager()
migrate = Migrate()

def init_app(app):
    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)

    login_manager.login_view = 'login.index'
    login_manager.login_message = "Please log in to access this page."
    login_manager.login_message_category = "info"

    # Handle unauthorized access
    from flask import flash, redirect, url_for, request
    from app.models.user import User

    @login_manager.unauthorized_handler
    def unauthorized():
        flash('You need to be logged in to access this page.', 'warning')
        return redirect(url_for('login.index', next=request.endpoint))

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
