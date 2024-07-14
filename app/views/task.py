from flask import (
    Blueprint,
    current_app,
    render_template,
    request,
    jsonify,
)
from flask_login import login_required

from app.models.task import Task, TaskItem

bp_task = Blueprint("task", __name__)


@bp_task.route("/about")
def about():
    return "about"


@bp_task.route("/")
@login_required
def index():
    tasks = Task.query.all()
    return render_template("task/index.html", tasks=tasks)


@bp_task.route("/addtask", methods=["POST"])
@login_required
def add_task():
    title = request.form.get("title")
    new_task = Task(title=title)
    current_app.db.session.add(new_task)
    current_app.db.session.commit()
    return jsonify({"id": new_task.id, "title": new_task.title})


@bp_task.route("/moveitem", methods=["POST"])
@login_required
def move_task_item():
    task_id = request.form.get("task_id")
    new_status = request.form.get("new_status")
    task = Task.query.get(task_id)
    task.status = new_status
    current_app.db.session.commit()
    return jsonify({"status": "success"})


@bp_task.route("/update_task_item", methods=["POST"])
@login_required
def update_task_item():
    data = request.get_json()
    print(data)
    task_item_id = data.get("task_item_id")
    new_task_id = data.get("new_task_id")

    task_item = TaskItem.query.get(task_item_id)
    if task_item:
        task_item.task_id = new_task_id
        current_app.db.session.commit()
        return jsonify({"message": "Task item updated successfully"}), 200
    return jsonify({"message": "Task item not found"}), 404
