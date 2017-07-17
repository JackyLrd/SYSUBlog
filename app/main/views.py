from flask import render_template, session, redirect, url_for, request

from . import main
from .forms import SearchForm
from .. import db
from ..models import Organization

@main.route('/', methods=['GET', 'POST'])
def index():
    form = SearchForm()
    organizations = Organization.query.all()
    # organizations = db.session.query(Organization.name).all()
    if request.method == 'POST':
        if form.validate_on_submit():
            return redirect(url_for('.organization', name=form.name.data))
    return render_template('index.html', organizations=organizations, form=form)

@main.route('/organizations/<name>')
def organization(name):
    organizations = Organization.query.filter(Organization.name.like('%' + name + '%'))
    return render_template('organization.html', organizations=organizations)