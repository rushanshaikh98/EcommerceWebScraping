from flask import Flask

from config import Config


def create_app():
    """A function for creating the app and configuring it, and it returns the configured app"""
    app = Flask(__name__)
    app.config.from_object(Config)

    from core.api.routes import api_routes

    app.register_blueprint(api_routes)

    return app
