from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from lineup.config import Config

# Flask
app = Flask(__name__)
app.config.from_object(Config)

# Database
db = SQLAlchemy()

# Password management
bcrypt = Bcrypt()

# Login management
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message = ('Please login to access this page.','')
login_manager.login_message_category = 'danger'

def create_app(config_class=Config):
	'''
	Creates instance of application
	'''
	app = Flask(__name__)
	app.config.from_object(Config)

	db.init_app(app)
	bcrypt.init_app(app)
	login_manager.init_app(app)

	from lineup.main.routes import main
	from lineup.users.routes import users
	from lineup.todos.routes import todos
	app.register_blueprint(main)
	app.register_blueprint(users)
	app.register_blueprint(todos)

	return app