from flask_wtf import FlaskForm
from wtforms import SubmitField, IntegerField

class SortForm(FlaskForm):
	'''
	Form to update sort id
	'''
	sort_id = IntegerField()
	submit = SubmitField('Confirm')