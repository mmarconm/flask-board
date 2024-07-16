from flask import (
    Blueprint,
    current_app,
    render_template,
    request,
    redirect,
    url_for,
    jsonify,
)
from flask_login import login_required

from app.models.task import Task, TaskItem
from app.forms import TaskItemForm, TaskForm

bp_task = Blueprint("task", __name__)


@bp_task.route("/")
@login_required
def index():
    tasks = Task.query.all()
    return render_template("task/index.html", tasks=tasks)

@bp_task.route('/add_task_modal', methods=['POST', "GET"])
def add_task_modal():
    task_id = request.values.get('task_id')
    print(task_id)
    form = TaskItemForm()
    if form.validate_on_submit():
        title = form.title.data
        status = form.status.data
        priority = form.priority.data
        owner = form.owner.data
        is_completed = form.is_completed.data
        task_item = TaskItem(
            title=title, 
            status=status, 
            priority=priority, 
            owner=owner, 
            is_completed=is_completed, 
            task_id=1
        )
        current_app.db.session.add(task_item)
        current_app.db.session.commit()
        return render_template('_partials/task_item.html', task_item=task_item)

    return render_template('_partials/add_task_modal.html', form=form)


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
    task_item_id = data.get("task_item_id")
    new_task_id = data.get("new_task_id")

    task_item = TaskItem.query.get(task_item_id)
    if task_item:
        task_item.task_id = new_task_id
        current_app.db.session.commit()
        return jsonify({"message": "Task item updated successfully"}), 200
    return jsonify({"message": "Task item not found"}), 404
