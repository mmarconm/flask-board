from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate

from app.config import Config
from app.models.configure import configure_db
from app.models.core import User


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    login_manager = LoginManager()
    login_manager.login_view = "core.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    configure_db(app)
    Migrate(app, app.db)

    from app.hooks import (
        after_request,
        before_request,
        teardown_appcontext,
        teardown_request,
    )

    # Registering Hooks
    app.before_request(before_request)
    app.after_request(after_request)
    app.teardown_request(teardown_request)
    app.teardown_appcontext(teardown_appcontext)

    # Registering Commands
    with app.app_context():
        from app.scripts.pupulate_db import populate_db

        app.cli.add_command(populate_db)

    # Registering Blueprints
    from app.views.core import bp_core
    from app.views.task import bp_task

    app.register_blueprint(bp_task)
    app.register_blueprint(bp_core)

    return app
