# FlaskSiteBuilder

FlaskSiteBuilder is a web application built using the Flask framework. This project serves as a template for building robust web applications with user authentication, a dashboard, and various other features.

## Project Structure


<pre>
FlaskSiteBuilder/
├── app/
│   ├── about/
│   │   ├── __init__.py
│   │   └── routes.py
│   ├── contact/
│   │   ├── __init__.py
│   │   └── routes.py
│   ├── dashboard/
│   │   ├── __init__.py
│   │   └── routes.py
│   ├── errors/
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   └── handlers.py
│   ├── forms/
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   └── forms.py
│   ├── login/
│   │   ├── __init__.py
│   │   └── routes.py
│   ├── main/
│   │   ├── __init__.py
│   │   └── routes.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── user.py
│   ├── register/
│   │   ├── __init__.py
│   │   └── routes.py
│   ├── reset_password/
│   │   ├── __init__.py
│   │   └── routes.py
│   ├── reset_request/
│   │   ├── __init__.py
│   │   └── routes.py
│   ├── validators/
│   │   ├── __init__.py
│   │   └── routes.py
│   ├── static/
│   │   ├── css/
│   │   ├── fonts/
│   │   ├── images/
│   │   └── js/
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── about/
│   │   │   └── index.html
│   │   ├── contact/
│   │   │   └── index.html
│   │   ├── dashboard/
│   │   │   └── index.html
│   │   ├── forms/
│   │   │   └── index.html
│   │   ├── login/
│   │   │   └── index.html
│   │   ├── register/
│   │   │   └── index.html
│   │   ├── reset_password/
│   │   │   └── index.html
│   │   ├── reset_request/
│   │   │   └── index.html
│   │   └── validators/
│   │       └── index.html
├── config.py
├── extensions.py
├── logging_config.py
├── run.py
├── .env
├── .flaskenv
├── instance/
│   └── app.db
├── migrations/
│   └── versions/
│       ├── alembic.ini
│       ├── env.py
│       ├── README
│       └── script.py.mako
├── my_env/
│   ├── include/
│   ├── lib/
│   ├── script/
│   └── pyeveng.cfg
├── test/
│   ├── conftest.py
│   ├── test_forms.py
│   └── test_models.py
├── README.md
└── LICENSE
</pre>



## Features

- User Authentication (Login, Register, Password Reset)
- User Dashboard
- About and Contact Pages
- Error Handling
- Forms with Validation
- Static File Management
- Logging Configuration

## Getting Started

### Prerequisites

- Python 3.x
- Virtual Environment (recommended)

### Installation

1. Clone the repository:

```bash
git clone https://github.com/https://github.com/danniwide1234/FlaskSiteBuilder
cd FlaskSiteBuilder
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Install the required packages:

```bash
pip install Flask SQLAlchemy Flask-Migrate Flask-Login Flask-WTF Flask-Mail
```

4. Set up the environment variables:

Create a `.env` file in the root directory with the following content:

```plaintext
FLASK_ENV=development
DEBUG=True
SECRET_KEY=99490c5b2922cd2dca58ba2efb8ea223
DATABASE_URI=sqlite:///instance/app.db
```

5. Initialize the database:

```bash
flask db upgrade
```

6. Run the application:

```bash
flask run
```

## Usage

- Access the application at `http://127.0.0.1:5000/`
- Register a new user, login, and explore the dashboard.
- Check out the about and contact pages.

## Testing

Run the tests using pytest:

```bash
pytest
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.




