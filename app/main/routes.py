from flask import Blueprint, render_template
from app.extensions import db
from app.models.main import Post

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    posts = Post.query.all()
    return render_template('core/index.html', posts=posts)

@bp.route('/about')
def about():
    return render_template('core/about.html')

@bp.route('/dashboard')
def dashboard():
    return render_template('core/dashboard.html')

@bp.route('/contact')
def contact():
    return render_template('core/contact.html')

