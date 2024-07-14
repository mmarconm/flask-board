from flask import Flask
from flask_migrate import Migrate
from flask_login import LoginManager

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

    # Registering Commands
    with app.app_context():
        from app.scripts.pupulate_db import populate_db

        app.cli.add_command(populate_db)

    # Registering Blueprints
    from app.views.task import bp_task
    from app.views.core import bp_core

    app.register_blueprint(bp_task)
    app.register_blueprint(bp_core)

    return app
