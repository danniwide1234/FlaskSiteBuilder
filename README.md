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
├── scripts/ │
         └── update_member_since.py

</pre>


## Features

- User Authentication: Includes functionalities for user registration, login, logout, and password reset.
- User Dashboard: Provides a customizable dashboard for each authenticated user.
- About and Contact Pages: Static pages with basic information about the application and contact details.
- Error Handling: Centralized error handling for better user experience.
- Forms with Validation: Implements forms with server-side validation using Flask-WTF.
- Static File Management: Organized handling of static assets like CSS, fonts, images, and JavaScript.
- Logging Configuration: Configured logging to track application events.

## Getting Started

### Prerequisites

- Python 3.x
- Virtual Environment (recommended)

### Installation
1. Clone the repository:

   ```bash
   git clone https://github.com/https://github.com/danniwide1234/FlaskSiteBuilder
   cd FlaskSiteBuilder
 

2. Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Install the required packages:
pip install Flask SQLAlchemy Flask-Migrate Flask-Login Flask-WTF Flask-Mail

4. Set up the environment variables:
Create a .env file in the root directory with the following content:
FLASK_ENV=development
DEBUG=True
SECRET_KEY=99490c5b2922cd2dca58ba2efb8ea223
DATABASE_URI=sqlite:///instance/app.db

5. Initialize the database
flask db upgrade

6. Run the application:
flask run


### Usage
Access the application at http://127.0.0.1:5000/
Register a new user, login, and explore the dashboard.
Check out the about and contact pages.

### Testing
Run the tests using pytest:
pytest

### Author
This project was created by Daniel Egbuluese, a chemical engineering graduate and tech enthusiast with a background in ISO consultancy. Daniel is currently pursuing a career in software engineering to develop tools that streamline ISO certification processes and solve real-world challenges.

### Contributing
Contributions are welcome! Please open an issue or submit a pull request.

### License
This project is licensed under the MIT License - see the LICENSE file for details.

### Contact
If you have any questions or feedback, feel free to contact Daniel at danniwide.1981@gmail.com or fidelismicheal12@gmail.com.



