import click
from datetime import datetime
from flask import current_app as app
from app.models.configure import db
from app.models.task import (
    Task,
    TaskItem,
)


@app.cli.command("populate_db")
def populate_db():
    """Populates the database with mock data."""
    click.echo("Populating the database with mock data...")

    tasks = [
        {"title": "Planejamento", "user_id": 1},
        {"title": "Desenvolvimento", "user_id": 1},
        {"title": "Testes", "user_id": 1},
        {"title": "Deploy", "user_id": 1},
        {"title": "Bugfix", "user_id": 1},
        {"title": "Cancelados", "user_id": 1},
    ]

    task_items = [
        {"title": "Subtask 1", "status": "Done", "is_completed": True, "task_id": 1},
        {
            "title": "Subtask 2",
            "status": "In Progress",
            "is_completed": False,
            "task_id": 1,
        },
        {
            "title": "Subtask 3",
            "status": "Pending",
            "is_completed": False,
            "task_id": 2,
        },
        {"title": "Subtask 4", "status": "Done", "is_completed": True, "task_id": 2},
        {
            "title": "Subtask 5",
            "status": "In Progress",
            "is_completed": False,
            "task_id": 3,
        },
        {
            "title": "Subtask 6",
            "status": "Pending",
            "is_completed": False,
            "task_id": 4,
        },
        {"title": "Subtask 7", "status": "Done", "is_completed": True, "task_id": 3},
        {
            "title": "Subtask 8",
            "status": "In Progress",
            "is_completed": False,
            "task_id": 4,
        },
        {
            "title": "Subtask 9",
            "status": "Pending",
            "is_completed": False,
            "task_id": 3,
        },
        {"title": "Subtask 10", "status": "Done", "is_completed": True, "task_id": 3},
    ]

    for task_data in tasks:
        task = Task(**task_data)
        db.session.add(task)

    for item_data in task_items:
        item_data["updated_at"] = datetime.now()
        task_item = TaskItem(**item_data)
        db.session.add(task_item)

    db.session.commit()
    click.echo("Database populated with mock data successfully.")
