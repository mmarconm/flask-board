from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField, SubmitField
from wtforms.validators import (
    DataRequired,
    Length,
    ValidationError,
    EqualTo,
)

from .models import User


class Task(FlaskForm):
    title = StringField("Title", validators=[DataRequired(), Length(min=2, max=100)])
    user_id = StringField("User ID")


class TaskItem(FlaskForm):
    title = StringField("Title", validators=[DataRequired(), Length(min=2, max=100)])
    status = BooleanField("Complete")
    is_completed = BooleanField("Is Completed")
    created_at = StringField("Created At")
    updated_at = StringField("Updated At")
    task_id = StringField("Task ID")


class UserForm(FlaskForm):
    username = StringField(
        "Username", validators=[DataRequired(), Length(min=4, max=150)]
    )
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField(
        "Confirm Password", validators=[DataRequired(), EqualTo("password")]
    )
    submit = SubmitField("Register")

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError(
                "Username already taken. Please choose a different one."
            )


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Login")
