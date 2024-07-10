import pytest
from app import create_app
from app.forms.forms import RegistrationForm, RequestResetForm, ResetPasswordForm, LoginForm, ContactForm
from app.models.user import User
from extensions import db

@pytest.fixture(scope='module')
def test_app():
    app = create_app()
    app.config.update({
        'TESTING': True,
        'WTF_CSRF_ENABLED': False,
    })
    with app.app_context():
        yield app

@pytest.fixture(scope='module')
def client(test_app):
    return test_app.test_client()

@pytest.fixture(scope='module')
def runner(test_app):
    return test_app.test_cli_runner()

# Helper function to generate long strings
def long_string(length):
    return 'a' * length

# Common valid data for forms
@pytest.fixture
def valid_registration_data():
    return {
        'user_name': 'testuser',
        'email': 'testuser@example.com',
        'password': 'password123',
        'confirm_password': 'password123'
    }

@pytest.fixture
def valid_request_reset_data():
    return {'email': 'testuser@example.com'}

@pytest.fixture
def valid_reset_password_data():
    return {
        'password': 'password123',
        'confirm_password': 'password123'
    }

@pytest.fixture
def valid_login_data():
    return {
        'email': 'testuser@example.com',
        'password': 'password123'
    }

@pytest.fixture
def valid_contact_data():
    return {
        'name': 'Test User',
        'email': 'testuser@example.com',
        'message': 'This is a test message.'
    }

@pytest.fixture(scope='module')
def init_database(test_app):
    with test_app.app_context():
        db.create_all()
        yield db
        db.drop_all()

# Parameterized tests for RegistrationForm
@pytest.mark.parametrize("data, is_valid", [
    ({"user_name": "", "email": "testuser@example.com", "password": "password123", "confirm_password": "password123"}, False),
    ({"user_name": "testuser", "email": "invalid-email", "password": "password123", "confirm_password": "password123"}, False),
    ({"user_name": "testuser", "email": "testuser@example.com", "password": "password123", "confirm_password": "password321"}, False),
    ({"user_name": long_string(256), "email": "testuser@example.com", "password": "password123", "confirm_password": "password123"}, False),
])
def test_registration_form(data, is_valid, valid_registration_data, test_app, init_database):
    with test_app.app_context():
        form = RegistrationForm(data=data)
        assert form.validate() == is_valid

def test_registration_form_valid(valid_registration_data, test_app, init_database):
    with test_app.app_context():
        form = RegistrationForm(data=valid_registration_data)
        assert form.validate()

# Parameterized tests for RequestResetForm
@pytest.mark.parametrize("data, is_valid", [
    ({"email": "invalid-email"}, False),
    ({"email": ""}, False),
    ({"email": long_string(256) + "@example.com"}, False),
])
def test_request_reset_form(data, is_valid, valid_request_reset_data, test_app):
    with test_app.app_context():
        form = RequestResetForm(data=data)
        assert form.validate() == is_valid

def test_request_reset_form_valid(valid_request_reset_data, test_app):
    with test_app.app_context():
        form = RequestResetForm(data=valid_request_reset_data)
        assert form.validate()

# Parameterized tests for ResetPasswordForm
@pytest.mark.parametrize("data, is_valid", [
    ({"password": "password123", "confirm_password": "password321"}, False),
    ({"password": "", "confirm_password": "password123"}, False),
    ({"password": long_string(256), "confirm_password": long_string(256)}, False),
])
def test_reset_password_form(data, is_valid, valid_reset_password_data, test_app):
    with test_app.app_context():
        form = ResetPasswordForm(data=data)
        assert form.validate() == is_valid

def test_reset_password_form_valid(valid_reset_password_data, test_app):
    with test_app.app_context():
        form = ResetPasswordForm(data=valid_reset_password_data)
        assert form.validate()

# Parameterized tests for LoginForm
@pytest.mark.parametrize("data, is_valid", [
    ({"email": "invalid-email", "password": "password123"}, False),
    ({"email": "", "password": "password123"}, False),
    ({"email": "testuser@example.com", "password": ""}, False),
])
def test_login_form(data, is_valid, valid_login_data, test_app):
    with test_app.app_context():
        form = LoginForm(data=data)
        assert form.validate() == is_valid

def test_login_form_valid(valid_login_data, test_app):
    with test_app.app_context():
        form = LoginForm(data=valid_login_data)
        assert form.validate()

# Parameterized tests for ContactForm
@pytest.mark.parametrize("data, is_valid", [
    ({"name": "Test User", "email": "invalid-email", "message": "This is a test message."}, False),
    ({"name": "", "email": "testuser@example.com", "message": "This is a test message."}, False),
    ({"name": "Test User", "email": "testuser@example.com", "message": ""}, False),
    ({"name": "Test User", "email": "testuser@example.com", "message": long_string(5001)}, False),
])
def test_contact_form(data, is_valid, valid_contact_data, test_app):
    with test_app.app_context():
        form = ContactForm(data=data)
        assert form.validate() == is_valid

def test_contact_form_valid(valid_contact_data, test_app):
    with test_app.app_context():
        form = ContactForm(data=valid_contact_data)
        assert form.validate()
