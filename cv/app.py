from flask import Flask

from cv.api import routes
from cv.commands.cv import cv
from cv.settings import CV_DATA_FILEPATH
from cv.utils import read_cv_data_from_file


def create_app() -> Flask:
    """
    Create and configure an instance of the Flask application.

    This function initializes a Flask app instance, loads the CV data
    from a file, registers blueprints and CLI commands, and then returns
    the configured app.
    """

    app = Flask(__name__)
    app.config["data"] = read_cv_data_from_file(CV_DATA_FILEPATH)

    register_blueprints(app)
    register_commands(app)
    return app


def register_blueprints(app):
    """
    Register blueprints to the Flask app instance.
    """

    app.register_blueprint(routes.api_bp, url_prefix="/api")


def register_commands(app):
    """
    Register CLI commands to the Flask app instance.
    """

    app.cli.add_command(cv)
