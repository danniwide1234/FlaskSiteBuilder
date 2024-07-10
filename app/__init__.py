from flask import Flask
from config import Config
from extensions import db, login_manager, migrate, csrf
from logging_config import configure_logging
from datetime import datetime

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)
    csrf.init_app(app)

    with app.app_context():
        # Import models to ensure they are registered
        from app.models.user import User  # Ensure User model is imported
        # Create database tables for our data models
        db.create_all()

    # Set up user loader for Flask-Login
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Register blueprints
    from app.main.routes import bp as main_bp
    app.register_blueprint(main_bp)

    from app.login.routes import bp as login_bp
    app.register_blueprint(login_bp, url_prefix='/login')

    from app.register.routes import bp as register_bp
    app.register_blueprint(register_bp, url_prefix='/register')

    from app.reset_password.routes import bp as reset_password_bp
    app.register_blueprint(reset_password_bp, url_prefix='/reset_password')

    from app.reset_request.routes import bp as reset_request_bp
    app.register_blueprint(reset_request_bp, url_prefix='/reset_request')

    from app.dashboard.routes import bp as dashboard_bp
    app.register_blueprint(dashboard_bp, url_prefix='/dashboard')

    from app.about.routes import bp as about_bp
    app.register_blueprint(about_bp, url_prefix='/about')

    from app.contact.routes import bp as contact_bp
    app.register_blueprint(contact_bp, url_prefix='/contact')

    from app.errors.handlers import bp as errors_bp
    app.register_blueprint(errors_bp)

    # Additional setup
    configure_logging(app)

    # Inject current year into templates
    @app.context_processor
    def inject_current_year():
        return {'current_year': datetime.utcnow().year}

    return app
