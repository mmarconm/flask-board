from app.models.configure import db


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    created_at = db.Column(
        db.DateTime, nullable=False, default=db.func.current_timestamp()
    )
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    task_items = db.relationship("TaskItem", backref="task", lazy=True)

    def __str__(self) -> str:
        return self.title


class TaskItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(100), nullable=False)
    is_completed = db.Column(db.Boolean, default=False)
    created_at = db.Column(
        db.DateTime, nullable=False, default=db.func.current_timestamp()
    )
    updated_at = db.Column(db.DateTime, nullable=False)
    task_id = db.Column(db.Integer, db.ForeignKey("task.id"))

    def __str__(self) -> str:
        return self.title
