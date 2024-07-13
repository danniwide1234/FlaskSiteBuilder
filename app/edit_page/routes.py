from flask import render_template, Blueprint, request, flash, redirect, url_for
from flask_login import login_required, current_user
from app.forms.forms import EditPageForm
from app.models.page import Page
from extensions import db

bp = Blueprint('edit_page', __name__)

@bp.route('/', methods=['GET', 'POST'])
@login_required
def index():
    form = EditPageForm()
    
    if form.validate_on_submit():
        page_title = form.page_title.data
        page_content = form.page_content.data
        
        # Retrieve the page object to edit
        # For demonstration, assuming you have a way to identify the page to edit, e.g., by ID
        page_id = request.args.get('page_id')  # Example: URL parameter or form hidden field
        
        if page_id:
            page = Page.query.get(page_id)
            if page:
                # Update page details
                page.title = page_title
                page.content = page_content
                try:
                    db.session.commit()
                    flash('Page updated successfully!', 'success')
                    return redirect(url_for('edit_page.index'))
                except Exception as e:
                    db.session.rollback()
                    flash(f'Error updating page: {str(e)}', 'danger')
            else:
                flash('Page not found!', 'danger')
        else:
            flash('Page ID not provided!', 'danger')

    # Render the form initially or with validation errors
    return render_template('edit_page/index.html', form=form)
