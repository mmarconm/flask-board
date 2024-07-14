from flask import (
    Blueprint,
    current_app,
    render_template,
    request,
    jsonify,
)

from app.models.task import Task

bp_task = Blueprint("task", __name__)


@bp_task.route("/about")
def about():
    return "about"


@bp_task.route("/")
def index():
    tasks = Task.query.all()
    return render_template("task/index.html")


@bp_task.route("/add", methods=["POST"])
def add_task():
    title = request.form.get("title")
    new_task = Task(title=title, status="Planejamento")
    current_app.db.session.add(new_task)
    current_app.db.session.commit()
    return jsonify(
        {"id": new_task.id, "title": new_task.title, "status": new_task.status}
    )


@bp_task.route("/move", methods=["POST"])
def move_task():
    task_id = request.form.get("task_id")
    new_status = request.form.get("new_status")
    task = Task.query.get(task_id)
    task.status = new_status
    current_app.db.session.commit()
    return jsonify({"status": "success"})
