from flask_login import UserMixin

from .configure import db


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    is_staff = db.Column(db.Boolean, default=False)
    todos = db.relationship("Task", backref="user", lazy=True)

    def __str__(self) -> str:
        return self.username
