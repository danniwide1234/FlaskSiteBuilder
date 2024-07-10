import pytest
from app import create_app
from app.models.user import User
from extensions import db

@pytest.fixture(scope='module')
def test_app():
    app = create_app()
    app.config.update({
        'TESTING': True,
        'SQLALCHEMY_DATABASE_URI': 'sqlite:///:memory:',  # Use in-memory SQLite for testing
    })
    with app.app_context():
        yield app

@pytest.fixture(scope='module')
def init_database(test_app):
    with test_app.app_context():
        db.create_all()
        yield db
        db.drop_all()

@pytest.fixture
def user_data():
    return {
        'user_name': 'testuser',
        'first_name': 'Test',
        'last_name': 'User',
        'email': 'testuser@example.com',
        'password': 'password123'
    }

@pytest.fixture
def add_user(init_database, user_data):
    new_user = User(
        user_name=user_data['user_name'],
        first_name=user_data['first_name'],
        last_name=user_data['last_name'],
        email=user_data['email']
    )
    new_user.set_password(user_data['password'])

    init_database.session.add(new_user)
    init_database.session.commit()

    yield new_user

    init_database.session.delete(new_user)
    init_database.session.commit()

def test_create_user(init_database, user_data):
    new_user = User(**user_data)
    new_user.set_password(user_data['password'])

    db.session.add(new_user)
    db.session.commit()

    user = User.query.filter_by(email=user_data['email']).first()
    assert user is not None
    assert user.user_name == user_data['user_name']
    assert user.check_password(user_data['password'])

def test_update_user(add_user):
    add_user.first_name = 'Updated'
    db.session.commit()

    updated_user = User.query.filter_by(email=add_user.email).first()
    assert updated_user.first_name == 'Updated'

def test_delete_user(add_user):
    db.session.delete(add_user)
    db.session.commit()

    deleted_user = User.query.filter_by(email=add_user.email).first()
    assert deleted_user is None
