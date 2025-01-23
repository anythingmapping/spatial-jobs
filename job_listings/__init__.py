from flask import Flask
from .api.jobs import jobs_bp


def create_app():
    app = Flask(__name__)

    # Register the jobs blueprint
    app.register_blueprint(jobs_bp)

    return app
