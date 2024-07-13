from flask import render_template, Blueprint, request, flash, redirect, url_for
from flask_login import login_required, current_user
from app.forms.forms import CreatePageForm, EditPageForm
from app.models.page import Page
from extensions import db

bp = Blueprint('create_page', __name__)

@bp.route('/', methods=['GET', 'POST'])
@login_required  # Ensure the user is logged in to access this page
def index():
    form = CreatePageForm()
    edit_form = EditPageForm()  # Create an instance of the EditPageForm

    if form.validate_on_submit():
        page_title = form.page_title.data
        page_content = form.page_content.data

        new_page = Page(title=page_title, content=page_content, author=current_user)

        try:
            db.session.add(new_page)
            db.session.commit()
            flash('Page created successfully!', 'success')
        except Exception as e:
            db.session.rollback()
            flash(f'Error creating page: {str(e)}', 'danger')

        return redirect(url_for('create_page.index'))

    pages = Page.query.all()

    return render_template('create_page/index.html', form=form, edit_form=edit_form, pages=pages)

@bp.route('/edit_page/<int:page_id>', methods=['GET', 'POST'])
@login_required
def edit_page(page_id):
    page = Page.query.get_or_404(page_id)
    edit_form = EditPageForm(obj=page)

    if edit_form.validate_on_submit():
        page.title = edit_form.page_title.data
        page.content = edit_form.page_content.data

        try:
            db.session.commit()
            flash('Page updated successfully!', 'success')
        except Exception as e:
            db.session.rollback()
            flash(f'Error updating page: {str(e)}', 'danger')

        return redirect(url_for('create_page.index'))

    return render_template('create_page/index.html', form=CreatePageForm(), edit_form=edit_form, pages=Page.query.all())
