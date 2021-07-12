from flask import url_for, redirect
from flask_login import current_user

def SortTodos(sort_id):
	'''
	Sorts current user's todo list based on value of sort id
	'''
	if sort_id == 1: # Sort by title ascending
		current_user.todos.sort(key=lambda x: x.title.lower())

	elif sort_id == 2: # Sort by title descending
		current_user.todos.sort(key=lambda x: x.title.lower(), reverse=True)

	elif sort_id == 3: # Sort by due date ascending
		current_user.todos.sort(key=lambda x: (int(x.dueDate[6:11]), int(x.dueDate[0:2]), int(x.dueDate[3:5])) if x.dueDate else (9999,99,99))

	elif sort_id == 4: # Sort by due date descending
		current_user.todos.sort(key=lambda x: (int(x.dueDate[6:11]), int(x.dueDate[0:2]), int(x.dueDate[3:5])) if x.dueDate else (0,0,0), reverse=True)

	elif sort_id == 5: # Sort by created date ascending
		current_user.todos.sort(key=lambda x: x.createdDate, reverse=True)

	elif sort_id == 6: # Sort by created date descending
		current_user.todos.sort(key=lambda x: x.createdDate)

	elif sort_id == 7: # Sort by priority ascending
		current_user.todos.sort(key=lambda x: x.priority, reverse=True)

	elif sort_id == 8: # Sort by priority descending
		current_user.todos.sort(key=lambda x: x.priority)

	elif sort_id == 0: # Sort by todo id
		current_user.todos.sort(key=lambda x: x.id)

	else: # Invalid sort id
		return redirect(url_for('main.home', sort_id='0'))