from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, RadioField, IntegerField
from wtforms.validators import DataRequired, Length

class TodoForm(FlaskForm):
	'''
	Form to update/add todo
	'''
	todo_id = IntegerField()
	title = StringField('Title', validators=[DataRequired()])
	dueDate = StringField('Due')
	priority = RadioField('Priority', choices=[0,1,2,3], default=0)
	note = TextAreaField('Note', validators=[Length(max=300)])
	submit = SubmitField('Add')