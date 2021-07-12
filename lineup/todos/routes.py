from flask import Blueprint
from flask import url_for, redirect
from flask_login import current_user, login_required
from lineup import db
from lineup.models import ToDo

todos = Blueprint('todos', '__name__')

@todos.route('/todo/mark/<int:todo_id>/<int:sort_id>')
@login_required
def mark_todo(todo_id, sort_id):
	'''
	Route to mark todo as complete or incomplete
	'''
	todo = ToDo.query.get_or_404(todo_id)
	if todo.author != current_user:
		abort(403)
	todo.completion = not todo.completion
	db.session.commit()
	return redirect(url_for('main.home', sort_id=sort_id))


@todos.route('/todo/delete/<int:todo_id>/<int:sort_id>')
@login_required
def delete_todo(todo_id, sort_id):
	'''
	Route to delete todo
	'''
	todo = ToDo.query.get_or_404(todo_id)
	if todo.author != current_user:
		abort(403)
	db.session.delete(todo)
	db.session.commit()
	return redirect(url_for('main.home', sort_id=sort_id))