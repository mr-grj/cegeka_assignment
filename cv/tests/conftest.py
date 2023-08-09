import pytest

from cv.app import create_app


@pytest.fixture()
def app():
    """
    Creates and configures a new instance of the Flask
    app for testing.
    """
    app = create_app()
    app.config.update({"TESTING": True})
    yield app


@pytest.fixture()
def client(app):
    """
    Provides a test client for the Flask app.

    This client allows sending HTTP requests to the application
    and receiving the responses for testing.
    """
    return app.test_client()


@pytest.fixture()
def runner(app):
    """
    Provides a test CLI runner for the Flask app.

    This runner allows invoking and testing CLI commands that are
    registered with the application.
    """
    return app.test_cli_runner()
