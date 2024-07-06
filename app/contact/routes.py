from flask import render_template, Blueprint

contact_bp = Blueprint('contact', __name__)

@contact_bp.route('/')
def index():
    return render_template('contact/index.html')
