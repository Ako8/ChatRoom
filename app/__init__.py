from flask import Flask
from app.config import Config
from app.extensions import db, migrate, socketio
from app.views import main_blueprint


BLUEPRINTS = [main_blueprint]
COMMANDS = []


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    register_exstensions(app)
    register_blueprints(app)
    register_commands(app)

    return app


def register_exstensions(app):
    # Flask SQLAlchemy
    db.init_app(app)

    # Flask-Migrate
    migrate.init_app(app)

    # Flask-SocketIO
    socketio.init_app(app)


def register_blueprints(app):
    for blueprint in BLUEPRINTS:
        app.register_blueprint(blueprint)


def register_commands(app):
    for command in COMMANDS:
        app.cli.add_command(command)
