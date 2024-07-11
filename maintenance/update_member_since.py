import os
import sys
from datetime import datetime, timezone

# Add the project directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app, db
from app.models.user import User

def set_member_since():
    users = User.query.filter_by(member_since=None).all()
    for user in users:
        user.member_since = datetime.now(timezone.utc)
    db.session.commit()

if __name__ == "__main__":
    # Load the Flask app context
    app = create_app(os.getenv('FLASK_CONFIG') or 'default')
    with app.app_context():
        set_member_since()
        print("Member since dates updated for users with None values.")
