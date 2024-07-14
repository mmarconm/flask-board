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
    print(tasks)
    return render_template("task/index.html", tasks=tasks)


@bp_task.route("/addtask", methods=["POST"])
def add_task():
    title = request.form.get("title")
    new_task = Task(title=title)
    current_app.db.session.add(new_task)
    current_app.db.session.commit()
    return jsonify({"id": new_task.id, "title": new_task.title})


@bp_task.route("/moveitem", methods=["POST"])
def move_task_item():
    task_id = request.form.get("task_id")
    new_status = request.form.get("new_status")
    task = Task.query.get(task_id)
    task.status = new_status
    current_app.db.session.commit()
    return jsonify({"status": "success"})
