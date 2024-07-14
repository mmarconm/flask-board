from flask import (
    Blueprint,
    current_app,
    render_template,
    request,
    redirect,
    url_for,
    flash,
)

from werkzeug.security import generate_password_hash, check_password_hash


from flask_login import (
    login_user,
    current_user,
)

from app.models import User
from app.forms import LoginForm, UserForm

bp_core = Blueprint("core", __name__)


@bp_core.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect(url_for("create_todo"))
        else:
            flash("Login ou senha incorretos.", "danger")
    return render_template("login.html", form=form)


@bp_core.route("/register", methods=["GET", "POST"])
def register():
    form = UserForm()
    if request.method == "POST":
        if form.validate():
            username = form.username.data
            password = form.password.data
            user = User(
                username=username,
                password=generate_password_hash(password),
            )
            current_app.db.session.add(user)
            current_app.db.session.commit()
            flash("Usuário criado com sucesso!", "success")
            return redirect(url_for("login"))
    return render_template("register.html", form=form)
