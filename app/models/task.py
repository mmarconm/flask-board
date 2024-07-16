from datetime import datetime
from app.models.configure import db


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sequence = db.Column(db.Integer, default=0)
    title = db.Column(db.String(100), nullable=False)
    isAllowedTask = db.Column(db.Boolean, default=True)
    created_at = db.Column(
        db.DateTime, nullable=False, default=db.func.current_timestamp()
    )
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    task_items = db.relationship("TaskItem", backref="task", lazy=True)

    def __str__(self) -> str:
        return self.title

    @classmethod
    def get_task_count(cls):
        return cls.query.count()

    @classmethod
    def get_next_sequence(cls):
        return cls.get_task_count() + 1

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.sequence = self.get_next_sequence()


class TaskItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sequence = db.Column(db.Integer, default=0)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text(), nullable=True)
    priority = db.Column(db.String(100), nullable=False)
    created_at = db.Column(
        db.DateTime, nullable=False, default=db.func.current_timestamp()
    )

    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    task_id = db.Column(db.Integer, db.ForeignKey("task.id"))

    def __str__(self) -> str:
        return self.title

    @classmethod
    def get_taskitem_count(cls):
        return cls.query.count()

    @classmethod
    def get_next_sequence(cls):
        return cls.get_taskitem_count() + 1

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.sequence = self.get_next_sequence()
