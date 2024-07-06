from flask import Flask, render_template
from config import Config
from extensions import db, login_manager, migrate, init_app

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    init_app(app)

    # Register blueprints
    from app.main.routes import main_bp
    from app.about.routes import about_bp
    from app.contact.routes import contact_bp
    from app.dashboard.routes import dashboard_bp
    from app.forms.routes import forms_bp
    from app.login.routes import login_bp
    from app.register.routes import register_bp
    from app.reset_password.routes import reset_password_bp
    from app.reset_request.routes import reset_request_bp
    from app.validators.routes import validators_bp
    from app.errors.routes import errors_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(about_bp, url_prefix='/about')
    app.register_blueprint(contact_bp, url_prefix='/contact')
    app.register_blueprint(dashboard_bp, url_prefix='/dashboard')
    app.register_blueprint(forms_bp, url_prefix='/forms')
    app.register_blueprint(login_bp, url_prefix='/login')
    app.register_blueprint(register_bp, url_prefix='/register')
    app.register_blueprint(reset_password_bp, url_prefix='/reset_password')
    app.register_blueprint(reset_request_bp, url_prefix='/reset_request')
    app.register_blueprint(validators_bp, url_prefix='/validators')
    app.register_blueprint(errors_bp)

    # Register error handler, context processor, user loader
    from app.models.user import User

    @app.errorhandler(Exception)
    def handle_exception(e):
        return render_template('errors/500.html'), 500

    @app.context_processor
    def inject_user():
        from flask_login import current_user
        return dict(current_user=current_user)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    return app
