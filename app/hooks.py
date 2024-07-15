from flask import g, request, redirect, url_for, g
from flask_login import current_user


def before_request():
    if not current_user.is_authenticated and request.endpoint not in [
        "core.login",
        "core.register",
    ]:
        return redirect(url_for("core.login"))


def after_request(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "SAMEORIGIN"
    response.headers["X-XSS-Protection"] = "1; mode=block"
    return response


def teardown_request(exception=None):
    db = getattr(g, "db", None)
    if db is not None:
        db.session.remove()


def teardown_appcontext(exception=None):
    db = getattr(g, "db", None)
    if db is not None:
        db.session.remove()
