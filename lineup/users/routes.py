from flask import Blueprint
from flask import render_template, url_for, flash, redirect
from flask_login import login_user, logout_user, current_user
from lineup import db, bcrypt
from lineup.users.forms import RegistrationForm, LoginForm
from lineup.models import User

users = Blueprint('users', '__name__')

@users.route('/register', methods=['GET', 'POST'])
def register():
	'''
	User registration page
	'''	
	if current_user.is_authenticated:
		return redirect(url_for('main.home', sort_id=0))
	form = RegistrationForm()
	if form.validate_on_submit():
		hashed_pwd = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		user = User(username=form.username.data, password=hashed_pwd)
		db.session.add(user)
		db.session.commit()
		flash(('Your account has been created!', 'You may now login.'), 'success')
		return redirect(url_for('users.login'))
	return render_template('register.html', form=form, title='Register')


@users.route('/login', methods=['GET', 'POST'])
def login():
	'''
	User login page
	'''
	if current_user.is_authenticated:
		return redirect(url_for('main.home', sort_id=0))
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).first()
		if user and bcrypt.check_password_hash(user.password, form.password.data):
			login_user(user, remember=form.remember.data)
			return redirect(url_for('main.home', sort_id=0))
		flash(('Login Failed.', 'Please check your username and password.'), 'danger')
	return render_template('login.html', form=form, title='Login')


@users.route('/logout')
def logout():
	'''
	Route to logout user
	'''
	logout_user()
	return redirect(url_for('users.login'))