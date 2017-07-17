from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class SearchForm(Form):
    name = StringField('search for organizations', validators=[DataRequired()])
    submit = SubmitField('submit')