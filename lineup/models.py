from datetime import datetime
from flask_login import UserMixin
from lineup import db, login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    '''
    User Table
    '''
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    todos = db.relationship('ToDo', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}')"


class ToDo(db.Model):
    '''
    Todo Table
    '''
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    createdDate = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    dueDate = db.Column(db.String(12))
    note = db.Column(db.String(300))
    priority = db.Column(db.Integer, nullable=False, default=0)
    completion = db.Column(db.Boolean, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"ToDo('{self.title}', '{self.createdDate}, priority')"