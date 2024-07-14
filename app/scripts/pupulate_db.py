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
        {
            "title": "Planejamento da Sprint",
            "status": "Pending",
            "is_completed": False,
            "task_id": 1,
        },
        {
            "title": "Desenvolvimento do Frontend",
            "status": "Pending",
            "is_completed": False,
            "task_id": 1,
        },
        {
            "title": "Desenvolvimento do Backend",
            "status": "Pending",
            "is_completed": False,
            "task_id": 1,
        },
        {
            "title": "Testes de Usabilidade",
            "status": "Pending",
            "is_completed": False,
            "task_id": 1,
        },
        {
            "title": "Testes de Performance",
            "status": "Pending",
            "is_completed": False,
            "task_id": 1,
        },
        {
            "title": "Deploy no Heroku",
            "status": "Pending",
            "is_completed": False,
            "task_id": 1,
        },
        {
            "title": "Deploy no AWS",
            "status": "Pending",
            "is_completed": False,
            "task_id": 1,
        },
        {
            "title": "Correção de Bug de Usuário",
            "status": "Pending",
            "is_completed": False,
            "task_id": 1,
        },
        {
            "title": "Correção de Bug de Admin",
            "status": "Pending",
            "is_completed": False,
            "task_id": 1,
        },
        {
            "title": "Task Cancelada",
            "status": "Pending",
            "is_completed": False,
            "task_id": 1,
        },
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
