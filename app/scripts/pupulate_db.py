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
        {"title": "Planejamento", "user_id": 1, "isAllowedTask": True},
        {"title": "Em Desenvolvimento", "user_id": 1, "isAllowedTask": False},
        {"title": "Em teste", "user_id": 1, "isAllowedTask": False},
        {"title": "Processo de deploy", "user_id": 1, "isAllowedTask": False},
        {"title": "Bugfix", "user_id": 1, "isAllowedTask": False},
        {"title": "Finalizados", "user_id": 1, "isAllowedTask": False},
        {"title": "Cancelados", "user_id": 1, "isAllowedTask": False},
    ]

    task_items = [
        {
            "title": "Planejamento da Sprint",
            "priority": "High",
            "description": "Inicio do planejamento da sprint 1.",
            "task_id": 1,
        },
        {
            "title": "Problema ao atualizar ambiente openshift",
            "priority": "High",
            "description": "Ao tentar instalar o ambiente openshift, o sistema não atualiza.",
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
