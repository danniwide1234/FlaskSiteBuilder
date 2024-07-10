from flask import render_template, request, redirect, url_for, flash, Blueprint
from app.forms.forms import ContactForm  # Importing the ContactForm

bp = Blueprint('contact', __name__)

@bp.route('/', methods=['GET', 'POST'])
def index():
    form = ContactForm()
    if form.validate_on_submit():
        # Handle form submission logic here
        flash('Your message has been sent!', 'success')
        return redirect(url_for('contact.index'))
    return render_template('contact/index.html', form=form)
