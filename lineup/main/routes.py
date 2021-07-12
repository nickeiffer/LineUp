from flask import Blueprint
from flask import render_template, url_for, redirect
from flask_login import current_user, login_required
from lineup import db
from lineup.main.forms import SortForm
from lineup.main.utils import SortTodos
from lineup.models import ToDo
from lineup.todos.forms import TodoForm

main = Blueprint('main', '__name__')

@main.route('/', methods=['GET', 'POST'])
@main.route('/home', methods=['GET', 'POST'])
def _():
	'''
	Root route - redirections to home page
	'''
	return redirect(url_for('main.home', sort_id='0'))


@main.route('/home/<int:sort_id>', methods=['GET', 'POST'])
@login_required
def home(sort_id):
	'''
	Home page
	'''
	todo_form = TodoForm()
	sort_form = SortForm()

	if todo_form.validate_on_submit():
		if todo := ToDo.query.get(todo_form.todo_id.data):	# Edit existing todo
			if todo.author != current_user:
				abort(403)
			todo.title = todo_form.title.data
			todo.dueDate = todo_form.dueDate.data
			todo.priority = todo_form.priority.data
			todo.note = todo_form.note.data

		else:	# Add new todo
			new_todo = ToDo(title=todo_form.title.data, dueDate=todo_form.dueDate.data, priority=todo_form.priority.data, note=todo_form.note.data, author=current_user)
			db.session.add(new_todo)

		db.session.commit()

	if sort_form.validate_on_submit() and sort_form.sort_id.data != None: # Update sort id
		return redirect(url_for('main.home', sort_id=sort_form.sort_id.data))

	# Sort list of todos based on sort id
	SortTodos(sort_id)

	return render_template('home.html', todos=current_user.todos, todo_form=todo_form, sort_form=sort_form, sort_id=sort_id)